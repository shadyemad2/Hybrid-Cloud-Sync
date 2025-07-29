resource "aws_s3_bucket" "shady_bucket" {
  bucket = "shady-hybrid-sync-2025"
  force_destroy = true

  tags = {
    Name        = "HybridSyncS3"
    Environment = "Dev"
  }
}
