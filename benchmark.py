from beir import util, LoggingHandler
from beir.retrieval import models
from beir.datasets.data_loader import GenericDataLoader
from beir.retrieval.evaluation import EvaluateRetrieval
from sentence_transformers import SentenceTransformer
from beir.retrieval.search.dense import DenseRetrievalExactSearch as DRES
from tokenizers import Tokenizer
from sentence_transformers.models import StaticEmbedding

import logging
import pathlib, os

# Initialize logging
logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO,
                    handlers=[LoggingHandler()])

# Download scifact dataset if not already downloaded
dataset = "scifact"
url = "https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/{}.zip".format(dataset)
out_dir = os.path.join(pathlib.Path(__file__).parent.absolute(), "datasets")
data_path = os.path.join(out_dir, dataset)
if not os.path.exists(data_path):
    data_path = util.download_and_unzip(url, out_dir)
# Load the dataset
corpus, queries, qrels = GenericDataLoader(data_folder=data_path).load(split="test")

# Initialize model and retriever
# model = DRES(models.SentenceBERT("sentence-transformers/static-retrieval-mrl-en-v1"), batch_size=16)
# model = DRES(models.SentenceBERT("answerdotai/ModernBERT-large"), batch_size=16)
model = models.SentenceBERT("models/public-static-modern-bert")

# tokenizer_512 = Tokenizer.from_pretrained("models/public-static-modern-bert")
# static_embedding_512 = StaticEmbedding(tokenizer_512, embedding_dim=512)
# model_512 = SentenceTransformer(modules=[static_embedding_512])
# model.q_model = model_512
# model.doc_model = model_512
# go down to 512 embeds
model_512 = SentenceTransformer('sentence-transformers/static-retrieval-mrl-en-v1', truncate_dim=512)
model.q_model = model_512
model.doc_model = model_512


# Test inference to verify embedding dimension
test_text = "This is a test sentence to verify embedding dimension"
test_embedding = model.encode_queries([test_text])
print(f"Test embedding shape: {test_embedding.shape}")  # Should show (1, 512)


model = DRES(model, batch_size=16)
retriever = EvaluateRetrieval(model, score_function="dot")

# Retrieve results
results = retriever.retrieve(corpus, queries)

# Evaluate model performance
ndcg, _map, recall, precision = retriever.evaluate(qrels, results, retriever.k_values)
