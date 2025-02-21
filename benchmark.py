from typing import Dict, List, Union
from beir import util, LoggingHandler
from beir.retrieval import models
from beir.datasets.data_loader import GenericDataLoader
from beir.retrieval.evaluation import EvaluateRetrieval
from sentence_transformers import SentenceTransformer
from beir.retrieval.search.dense import DenseRetrievalExactSearch as DRES
import torch
import torch.nn as nn
import logging
import pathlib, os
import numpy as np

# Initialize logging
logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO,
                    handlers=[LoggingHandler()])

# Download dataset
dataset = "scifact"
url = f"https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/{dataset}.zip"
out_dir = os.path.join(pathlib.Path(__file__).parent.absolute(), "datasets")
data_path = os.path.join(out_dir, dataset)
if not os.path.exists(data_path):
    util.download_and_unzip(url, out_dir)

# Load data
corpus, queries, qrels = GenericDataLoader(data_folder=data_path).load(split="test")
class DualStaticModel(nn.Module):
    def __init__(self, model1, model2):
        super().__init__()
        self.model1 = model1
        self.model2 = model2
        
    def encode_queries(self, queries: Union[List[str], Dict[str, str]], batch_size: int, **kwargs):
        sentences = list(queries.values()) if isinstance(queries, dict) else queries
        emb1 = self.model1.encode(sentences, batch_size=batch_size, **kwargs)
        emb2 = self.model2.encode(sentences, batch_size=batch_size, **kwargs)
        # Convert to tensors and average on same device
        return (torch.tensor(emb1).to(self.model1.device) + 
                torch.tensor(emb2).to(self.model2.device)) / 2
    
    def encode_corpus(self, corpus: Union[List[Dict[str, str]], Dict[str, List]], batch_size: int, **kwargs):
        if isinstance(corpus, dict):
            sentences = [(corpus["title"][i] + " " + corpus["text"][i]).strip() 
                        for i in range(len(corpus['text']))]
        else:
            sentences = [(doc["title"] + " " + doc["text"]).strip() for doc in corpus]
            
        emb1 = self.model1.encode(sentences, batch_size=batch_size, **kwargs)
        emb2 = self.model2.encode(sentences, batch_size=batch_size, **kwargs)
        # Convert to tensors and average on same device
        return (torch.tensor(emb1).to(self.model1.device) + 
                torch.tensor(emb2).to(self.model2.device)) / 2

# Initialize two instances of static model with different truncation
static_model_512 = SentenceTransformer(
    'sentence-transformers/static-retrieval-mrl-en-v1', 
    truncate_dim=512
)

static_model_multilingual = SentenceTransformer(
    'sentence-transformers/static-similarity-mrl-multilingual-v1',
    truncate_dim=512 
)

# Create dual model
combined_model = DualStaticModel(static_model_512, static_model_multilingual)

# Initialize retriever
model = DRES(
    combined_model,
    batch_size=16,
    corpus_chunk_size=50000,
    show_progress_bar=True
)

# Verification test
test_text = ["This is a test sentence"]
test_embedding = model.model.encode_queries(test_text, batch_size=1)
print(f"Combined embedding shape: {test_embedding.shape}")  # Should be (1, 768)

# Initialize evaluator
retriever = EvaluateRetrieval(model, score_function="dot")

# Run evaluation pipeline
results = retriever.retrieve(corpus, queries)
ndcg, _map, recall, precision = retriever.evaluate(qrels, results, retriever.k_values)

# Print results
print("\nEvaluation Results:")
for metric in [ndcg, _map, recall, precision]:
    print(f"{metric['metric']}:")
    for k, v in metric.items():
        if k != "metric":
            print(f"\t{k}: {v:.4f}")