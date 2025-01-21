from sentence_transformers import SentenceTransformer

# Load the trained model
model = SentenceTransformer('models/public-static-modern-bert')

# Push model to the Hugging Face Hub
model.save_to_hub(
    repo_name="public-static-modern-bert",
    organization=None,  # Change this to your organization name if needed
    private=False,
    commit_message="Add public static ModernBERT model"
)
