
import os
from huggingface_hub import HfApi

api = HfApi(token=os.getenv("HF_TOKEN"))

api.upload_folder(
    folder_path="predictive_maintenance_project/deployment",
    repo_id="Shalini94/predictive-maintenance-app",
    repo_type="space",
    path_in_repo=""
)

print("Deployment files uploaded successfully to Hugging Face Space.")
