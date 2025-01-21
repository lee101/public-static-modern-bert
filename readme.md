# Public Static ModernBERT Training

This repository contains code for training a static embedding model using ModernBERT-large as the base model.

This is a failed experiment.

I realized there are tokenization issues distilling the model from modern bert and gave up, 

I trained using the existing model created in https://huggingface.co/blog/static-embeddings

I wanted to try to optimize the model by removing the matryoshka embeddings and training for a hardcoded embedding size of 512 embeddings instead of 1024.

I feel this is a good embedding size, the training failed to generalize to a new task as i trained it on only one dataset and or because the model was already trained well on multiple datasets so the model is around the same to slightly worse when evaluated on BEIR so i reccommend using the existing models.

https://huggingface.co/sentence-transformers/static-retrieval-mrl-en-v1


https://huggingface.co/sentence-transformers/static-similarity-mrl-multilingual-v1


## Setup

1. Create and activate a virtual environment:
```
uv venv
. .venv/bin/activate
```

2. Install the required packages:
```
uv pip compile requirements.in -o requirements.txt && uv pip install -r requirements.txt  --python .venv/bin/python
```

3. Run the training script:
```
python training.py
```

4. Run the inference script (visualize embeddings using t-SNE):
```
python inference.py
```

5. Run the benchmark script:
```
python benchmark.py
```

# Notes

Ended up training for 512 embeddings instead of 1024.

# Plugs
Please support us!

You can support us using [netwrck](https://netwrck.com) for AI services.

Also checkout [AIArt-Generator.art](https://AIArt-Generator.art) and [Netwrck.com](https://netwrck.com) and [text-generator.io](https://text-generator.io) for unlimited AI API for smol/vision llms/speech
