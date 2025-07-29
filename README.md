## ☁️ Hybrid Cloud Sync: AWS S3 → Azure Blob
```
<img width="1980" height="1403" alt="overview" src="https://github.com/user-attachments/assets/f4c2c44a-2b14-473f-a55f-46f43c2c7f4e" />


This Python script automates one-way file synchronization from AWS S3 to Azure Blob Storage. It’s ideal for hybrid cloud use cases such as backup, migration, or cross-cloud redundancy.

<img width="1116" height="666" alt="Diagram" src="https://github.com/user-attachments/assets/d82a62fe-722c-4413-a46e-3eb21d97cd6f" />


## 📦 Features

- 🔄 Syncs files from AWS S3 to Azure Blob Storage
- 🌐 Supports AWS temporary session tokens
- 📝 Overwrites existing blobs to ensure latest version
- 🔒 Uses `.env` file for secure credential management
- ✅ Simple and easy to extend

## 📁 Project Structure

```
hybrid-cloud-sync/
├── aws/
│   └── terraform/                  # Terraform configs for AWs
│       ├── s3.tf
│       ├── provider.tf
│       ├── backend.tf
│       
│    
│
├── azure/
│   └── terraform/                 # Terraform configs for Azure (Storage Account, Blob Container)
│       ├── storage.tf
│       ├── provider.tf
│       └── terraform.tfstate*

├── sync-script/                  # Python sync logic (S3 → Azure)
│   ├── sync.py                   # Main sync script
│   ├── .env                      # Environment variables (not committed)
│   └── requirements.txt          # Python dependencies

├── README.md                     # Project documentation
```

```

## ⚙️ Setup

1. **Install dependencies**:

```bash
pip install -r requirements.txt
```

2. **Create `.env` file** with your cloud credentials:

```dotenv
# AWS Credentials
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_SESSION_TOKEN=your_aws_session_token  # Optional for long-term credentials
AWS_REGION=us-east-1
AWS_S3_BUCKET_NAME=your-s3-bucket-name

# Azure Credentials
AZURE_STORAGE_CONNECTION_STRING=your_azure_connection_string
AZURE_CONTAINER_NAME=your-azure-container
```

## 🚀 Usage

Run the script:

```bash
python sync.py
```

Expected output:

```
Syncing: file1.txt
Uploaded to Azure: file1.txt
Syncing: folder/file2.jpg
Uploaded to Azure: folder/file2.jpg
Sync complete!
```

## 🛡️ Security Notes

- Do not hardcode secrets inside the script.
- Add `.env` to your `.gitignore` file.
- Rotate keys regularly and use IAM best practices.

## 💡 Future Improvements

- [ ] Add reverse sync (Azure → S3)
- [ ] Detect unchanged files and skip
- [ ] Log sync history to a file
- [ ] Add progress bar or verbose mode
- [ ] Add cron support or scheduler integration

## 👤 Author

**Shady Emad**  
System Administrator & DevOps Engineer  

🔗 [GitHub](https://github.com/shadyemad2) 
