import os
import boto3
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
from botocore.exceptions import NoCredentialsError

# Load environment variables from .env file
load_dotenv()

# AWS credentials
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")  # Needed for temporary credentials
AWS_REGION = os.getenv("AWS_REGION")
AWS_S3_BUCKET_NAME = os.getenv("AWS_S3_BUCKET_NAME")

# Azure credentials
AZURE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
AZURE_CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME")

# print("AWS Key:", AWS_ACCESS_KEY_ID)
# print("Azure container:", AZURE_CONTAINER_NAME)

# Initialize AWS S3 client with session token
s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN,
    region_name=AWS_REGION
)

# Initialize Azure Blob client
blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(AZURE_CONTAINER_NAME)

def sync_s3_to_blob():
    try:
        # Get list of objects in S3 bucket
        s3_objects = s3.list_objects_v2(Bucket=AWS_S3_BUCKET_NAME)
        if 'Contents' not in s3_objects:
            print("S3 bucket is empty or does not exist.")
            return

        # Iterate and sync files
        for obj in s3_objects['Contents']:
            s3_key = obj['Key']
            print(f"Syncing: {s3_key}")

            # Download from S3
            s3_response = s3.get_object(Bucket=AWS_S3_BUCKET_NAME, Key=s3_key)
            file_data = s3_response['Body'].read()

            # Upload to Azure Blob
            blob_client = container_client.get_blob_client(s3_key)
            blob_client.upload_blob(file_data, overwrite=True)
            print(f"Uploaded to Azure: {s3_key}")

        print(" Sync complete!")

    except NoCredentialsError:
        print(" AWS credentials not found.")
    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    sync_s3_to_blob()

