from sentence_transformers import SentenceTransformer, SentenceTransformerTrainingArguments, InputExample
from sentence_transformers.models import StaticEmbedding
from tokenizers import Tokenizer
from sentence_transformers import SentenceTransformer, SentenceTransformerTrainingArguments
from sentence_transformers.losses import MultipleNegativesRankingLoss, MatryoshkaLoss
from sentence_transformers.evaluation import NanoBEIREvaluator
from datasets import load_dataset
from torch.utils.data import DataLoader, IterableDataset
from torch.utils.tensorboard import SummaryWriter
import os

# Initialize model with ModernBERT tokenizer randomized
# tokenizer = Tokenizer.from_pretrained("answerdotai/ModernBERT-large")

# static_embedding = StaticEmbedding(tokenizer, embedding_dim=1024)
# model = SentenceTransformer(modules=[static_embedding])
# static_embedding = StaticEmbedding.from_model2vec("minishlab/M2V_base_output")

# initialize with distilled embeddings from modernbert
# Adding arguments to try matching tokenizer and embeddings size
# doesnt actually work yet because of different token vocab size
# vocabulary = list(Tokenizer.from_pretrained("answerdotai/ModernBERT-large").get_vocab().keys())
# static_embedding = StaticEmbedding.from_distillation(
#     "answerdotai/ModernBERT-large",
#     # apply_zipf=False,
#     vocabulary=vocabulary,
#     # use_subword=False
# )
# model = SentenceTransformer(modules=[static_embedding])

# lets just keep training the model2vec model and see if we can make it better
model = SentenceTransformer('sentence-transformers/static-retrieval-mrl-en-v1')

# Training arguments
args = SentenceTransformerTrainingArguments(
    output_dir="models/public-static-modern-bert",
    num_train_epochs=15,
    per_device_train_batch_size=256,
    per_device_eval_batch_size=256, 
    learning_rate=2e-1,
    warmup_ratio=0.1,
    bf16=True,
    batch_sampler="no_duplicates",
    multi_dataset_batch_sampler="proportional",
    eval_strategy="steps",
    eval_steps=1000,
    save_strategy="steps",
    save_steps=1000,
    save_total_limit=2,
    logging_steps=1000,
    logging_first_step=True,
    run_name="public-static-modern-bert"
)

# Initialize loss function
base_loss = MultipleNegativesRankingLoss(model)
loss = MatryoshkaLoss(model, base_loss, matryoshka_dims=[512]) #lets only train for 512

# Load training datasets
from datasets import load_dataset
class TextDataset(IterableDataset):
    def __init__(self, ds_stream):
        self.ds_stream = ds_stream

    def __iter__(self):
        for item in self.ds_stream:
            yield InputExample(texts=item["texts"], label=0)  # Dummy label

datasets = [
    # gooaq
    # Dataset: gooaq at b089f72
    # Size: 3,012,496 training samples
    # Columns: question and answer
    TextDataset(load_dataset("sentence-transformers/gooaq", split="train").map(lambda x: {"texts": [x["question"], x["answer"]]})),
    
    # msmarco
    # Dataset: msmarco at 84ed2d3 
    # Size: 502,939 training samples
    # Columns: query, positive, and negative
    # TextDataset(load_dataset("sentence-transformers/msmarco", split="train").map(lambda x: {"texts": [x["query"], x["passage"]]})["texts"]),
    
    # squad
    # Dataset: squad at d84c8c2
    # Size: 87,599 training samples
    # Columns: question and answer
    # TextDataset(load_dataset("sentence-transformers/squad", split="train", streaming=True, keep_in_memory=False).map(lambda x: {"texts": [x["question"], x["answer"]]})),
    
    # s2orc
    # Dataset: s2orc at 8cfc394
    # Size: 90,000 training samples
    # Columns: title and abstract
    # TextDataset(load_dataset("sentence-transformers/s2orc", split="train", streaming=True, keep_in_memory=False).map(lambda x: {"texts": [x["title"], x["abstract"]]})),
    
    # allnli
    # Dataset: allnli at d482672
    # Size: 557,850 training samples
    # Columns: anchor, positive, and negative
    # TextDataset(load_dataset("sentence-transformers/allnli", split="train", streaming=True, keep_in_memory=False).map(lambda x: {"texts": [x["premise"], x["hypothesis"]]})),
    
    # paq
    # Dataset: paq at 74601d8
    # Size: 64,371,441 training samples
    # Columns: query and answer
    # TextDataset(load_dataset("sentence-transformers/paq", split="train", streaming=True, keep_in_memory=False).map(lambda x: {"texts": [x["query"], x["answer"]]})),
    
    # trivia_qa
    # Dataset: trivia_qa at a7c36e3
    # Size: 73,346 training samples
    # Columns: query and answer
    # TextDataset(load_dataset("sentence-transformers/trivia_qa", split="train", streaming=True, keep_in_memory=False).map(lambda x: {"texts": [x["query"], x["answer"]]})),
    
    # # msmarco_10m
    # TextDataset(load_dataset("sentence-transformers/msmarco_10m", split="train", streaming=True, keep_in_memory=False).map(lambda x: {"texts": [x["query"], x["passage"]]})),
    
    # swim_ir
    # Dataset: swim_ir at 834c20f
    # Size: 501,538 training samples
    # Columns: query and text
    # TextDataset(load_dataset("sentence-transformers/swim_ir", split="train", streaming=True, keep_in_memory=False).map(lambda x: {"texts": [x["query"], x["passage"]]})),
    
    # pubmedqa
    # Dataset: pubmedqa at a1ef0b5
    # Size: 1,660 training samples
    # TextDataset(load_dataset("sentence-transformers/pubmedqa", 'triplet', split="train").map(lambda x: {"texts": [x["question"], x["answer"]]})),
    
    # miracl
    # Dataset: miracl at 07e2b62
    # Size: 789,900 training samples
    # Columns: anchor, positive, and negative
    # TextDataset(load_dataset("sentence-transformers/miracl", "en-triplet-all", split="train", streaming=True, keep_in_memory=False).map(lambda x: {"texts": [x["query"], x["passage"]]})),
    
    # mldr
    # Dataset: mldr at 40ad767
    # Size: 200,000 training samples
    # Columns: anchor, positive, and negative
    # TextDataset(load_dataset("sentence-transformers/mldr", 'en-triplet-all', split="train", streaming=True, keep_in_memory=False).map(lambda x: {"texts": [x["query"], x["passage"]]})),
    
    # mr_tydi
    # Dataset: mr_tydi at abbdf55
    # Size: 354,700 training samples
    # Columns: anchor, positive, and negative
    # TextDataset(load_dataset("sentence-transformers/mr_tydi", split="train", streaming=True, keep_in_memory=False).map(lambda x: {"texts": [x["query"], x["passage"]]})),
]
# test epoc w small dataset
# datasets = [
#     TextDataset(load_dataset("sentence-transformers/squad", split="train").select(range(100)).map(lambda x: {"texts": [x["question"], x["answer"]]})["texts"]),
# ]

# Initialize evaluator
evaluator = NanoBEIREvaluator()

# Initialize TensorBoard writer
tensorboard_dir = os.path.join(args.output_dir, "tensorboard")
writer = SummaryWriter(log_dir=tensorboard_dir)

# Train the model
model.fit(
    train_objectives=[(DataLoader(dataset, batch_size=args.per_device_train_batch_size, shuffle=False), loss) for dataset in datasets],
    evaluator=evaluator,
    epochs=int(args.num_train_epochs),
    warmup_steps=int(args.warmup_ratio * args.num_train_epochs),
    output_path=args.output_dir,
    show_progress_bar=True,
    checkpoint_path=args.output_dir,
    checkpoint_save_steps=int(args.save_steps),
    checkpoint_save_total_limit=int(args.save_total_limit),
    use_amp=args.bf16,
    # logging_steps=args.logging_steps,
    # logging_first_step=args.logging_first_step,
    callback=lambda step, loss, epoch: writer.add_scalar('training_loss', loss, step)
)

# Close TensorBoard writer
writer.close()

# save the model
model.save("models/public-static-modern-bert")