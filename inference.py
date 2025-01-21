from sentence_transformers import SentenceTransformer, SentenceTransformerTrainingArguments
from sentence_transformers.models import StaticEmbedding
from tokenizers import Tokenizer
import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
import plotly.express as px

# Initialize model with ModernBERT tokenizer
tokenizer = Tokenizer.from_pretrained("answerdotai/ModernBERT-large") 
static_embedding = StaticEmbedding(tokenizer, embedding_dim=1024)
model = SentenceTransformer(modules=[static_embedding])

# Load trained model
model = SentenceTransformer('models/public-static-modern-bert', truncate_dim=512)

# Example texts to embed
texts = [
    "What is the capital of France?",
    "Paris is the capital of France",
    "How tall is Mount Everest?", 
    "Mount Everest is 8,848 meters tall",
    "What is machine learning?",
    "Machine learning is a subset of artificial intelligence",
    "Who wrote Romeo and Juliet?",
    "Shakespeare wrote Romeo and Juliet",
    "What is photosynthesis?",
    "Photosynthesis is how plants convert sunlight to energy"
]

# Get embeddings
import time
start_time = time.time()
embeddings = model.encode(texts)
inference_time = time.time() - start_time
print(f"Inference time: {inference_time} seconds")
print(embeddings.shape)
# Reduce dimensions for visualization using TSNE
tsne = TSNE(n_components=2, random_state=42, perplexity=5) # Lower perplexity since we have few samples
embeddings_2d = tsne.fit_transform(embeddings)

# Create dataframe for plotting
df = pd.DataFrame({
    'x': embeddings_2d[:, 0],
    'y': embeddings_2d[:, 1],
    'text': texts
})

# Create interactive plot
fig = px.scatter(df, x='x', y='y', hover_data=['text'])
fig.show()
