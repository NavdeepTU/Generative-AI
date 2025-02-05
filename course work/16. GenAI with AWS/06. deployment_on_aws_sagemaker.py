import sagemaker
import boto3
from sagemaker.huggingface.model import HuggingFaceModel

sess = sagemaker.Session()
# sagemaker session bucket -> used for uploading data, models and logs
# sagemaker will automatically create this bucket if it not exists
sagemaker_session_bucket = None
if sagemaker_session_bucket is None and sess is not None:
    # set to default bucket if a bucket name is not given
    sagemaker_session_bucket = sess.default_bucket()

# role management
try:
    role = sagemaker.get_execution_role()
except ValueError:
    iam = boto3.client("iam")
    role = iam.get_role(RoleName="sagemaker_execution_role")["Role"]["Arn"]

session = sagemaker.Session(default_bucket=sagemaker_session_bucket)

print(f"sagemaker role arn:{role}")
print(f"sagemaker session region:{session.boto_region_name}")

hub = {
    "HF_MODEL_ID":"distilbert-base-uncased-distilled-squad", # model_id from hf.co/models
    "HF_TASK":"question-answering" # NLP task you want to use for predictions
}

# create hugging face model class
huggingface_model = HuggingFaceModel(
    env=hub, # configuration for loading model from hub
    role=role, # IAM role with permissions to create an endpoint
    transformers_version="4.26", # Transformers version used
    pytorch_version="1.13", # pytorch version used
    py_version="py39" # python version used
)

# deploy model to SageMaker Inference
predictor = huggingface_model.deploy(
    initial_instance_count=1,
    instance_type="ml.m5.xlarge"
)

# example request: you always need to define "inputs"
data = {
    "inputs": {
        "question": "What is used for inference?",
        "context": "My name is Navdeep and I live in Noida. This model is used with sagemaker for inference."
    }
}

# request
predictor.predict(data)