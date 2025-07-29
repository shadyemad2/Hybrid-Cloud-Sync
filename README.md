
# ☁️ Hybrid Cloud Sync: AWS S3 → Azure Blob
<img width="1980" height="1403" alt="overview" src="https://github.com/user-attachments/assets/3e0cd154-5200-45e9-98e1-81b805a50382" />


This Python script automates **one-way file synchronization** from **AWS S3** to **Azure Blob Storage**.  
It’s ideal for hybrid cloud use cases such as backup, migration, or cross-cloud redundancy.

---

## 📦 Features

- 🔄 Syncs files from AWS S3 to Azure Blob Storage
- 🌐 Supports AWS temporary session tokens
- 📝 Overwrites existing blobs to ensure latest version
- 🔒 Uses `.env` file for secure credential management
- ✅ Simple and easy to extend

---

## 📁 Project Structure

```
hybrid-cloud-sync/
├── aws/
│   └── terraform/                  # Terraform configs for AWS
│       ├── s3.tf
│       ├── provider.tf
│       ├── backend.tf
│
├── azure/
│   └── terraform/                  # Terraform configs for Azure
│       ├── storage.tf
│       ├── provider.tf
│       └── terraform.tfstate*

├── sync-script/                   # Python sync logic (S3 → Azure)
│   ├── sync.py                    # Main sync script
│   ├── .env                       # Environment variables (not committed)
│   └── requirements.txt           # Python dependencies

├── README.md                      # Project documentation
└── .gitignore                     # Git ignore file
```

---

## ⚙️ Setup

1. **Install dependencies**:

```bash
pip install -r sync-script/requirements.txt
```

2. **Create `.env` file** inside `sync-script/` directory with your cloud credentials:

```dotenv
# AWS Credentials
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_SESSION_TOKEN=your_aws_session_token  # Optional
AWS_REGION=us-east-1
AWS_S3_BUCKET_NAME=your-s3-bucket-name

# Azure Credentials
AZURE_STORAGE_CONNECTION_STRING=your_azure_connection_string
AZURE_CONTAINER_NAME=your-azure-container
```

---

## 🚀 Usage

Run the sync script:

```bash
cd sync-script
python sync.py
```

Sample output:

```
Syncing: file1.txt
Uploaded to Azure: file1.txt
Syncing: folder/file2.jpg
Uploaded to Azure: folder/file2.jpg
Sync complete!
```

---

## 🛡️ Security Notes

- ❌ Never hardcode credentials inside Python scripts.
- ✅ Add `.env`, `.terraform/`, and `*.tfstate` to `.gitignore`.
- 🔁 Rotate keys periodically.
- 🧠 Use IAM roles and least privilege policies where possible.

---

## 💡 Future Improvements

- [ ] Add reverse sync (Azure → S3)
- [ ] Detect unchanged files and skip
- [ ] Log sync history to a file
- [ ] Add progress bar or verbose mode
- [ ] Integrate with cron or task scheduler

---

## 👤 Author

**Shady Emad**  
_System Administrator & DevOps Engineer_

🔗 [GitHub](https://github.com/shadyemad2)

---

## 📄 License

This project is licensed under the **MIT License**.
