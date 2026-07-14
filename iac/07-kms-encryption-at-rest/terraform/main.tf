data "aws_caller_identity" "current" {}
data "aws_partition" "current" {}
data "aws_iam_policy_document" "kms" {
  statement {
    sid       = "EnableAccountPermissions"
    actions   = ["kms:*"]
    resources = ["*"]
    principals {
      type        = "AWS"
      identifiers = ["arn:${data.aws_partition.current.partition}:iam::${data.aws_caller_identity.current.account_id}:root"]
    }
  }
  statement {
    sid = "AllowSupportedServicesViaAccount"
    actions = [
      "kms:Decrypt",
      "kms:DescribeKey",
      "kms:Encrypt",
      "kms:GenerateDataKey",
      "kms:ReEncryptFrom",
      "kms:ReEncryptTo"
    ]
    resources = ["*"]
    principals {
      type        = "Service"
      identifiers = ["s3.amazonaws.com", "dynamodb.amazonaws.com", "sqs.amazonaws.com"]
    }
    condition {
      test     = "StringEquals"
      variable = "aws:SourceAccount"
      values   = [data.aws_caller_identity.current.account_id]
    }
  }
}
resource "aws_kms_key" "data" {
  description             = "${var.project_name} - chave de dados do lab"
  enable_key_rotation     = true
  deletion_window_in_days = 7
  policy                  = data.aws_iam_policy_document.kms.json
  tags                    = { Name = "${var.project_name}-data-key" }
}
resource "aws_kms_alias" "data" {
  name          = "alias/${var.project_name}"
  target_key_id = aws_kms_key.data.key_id
}

resource "aws_s3_bucket" "encrypted" {
  bucket_prefix = "${var.project_name}-"
  force_destroy = true
  tags          = { Name = "${var.project_name}-encrypted" }
}
resource "aws_s3_bucket_ownership_controls" "encrypted" {
  bucket = aws_s3_bucket.encrypted.id
  rule { object_ownership = "BucketOwnerEnforced" }
}
resource "aws_s3_bucket_public_access_block" "encrypted" {
  bucket                  = aws_s3_bucket.encrypted.id
  block_public_acls       = true
  ignore_public_acls      = true
  block_public_policy     = true
  restrict_public_buckets = true
}
resource "aws_s3_bucket_versioning" "encrypted" {
  bucket = aws_s3_bucket.encrypted.id
  versioning_configuration { status = "Enabled" }
}
resource "aws_s3_bucket_server_side_encryption_configuration" "encrypted" {
  bucket = aws_s3_bucket.encrypted.id
  rule {
    bucket_key_enabled = true
    apply_server_side_encryption_by_default {
      kms_master_key_id = aws_kms_key.data.arn
      sse_algorithm     = "aws:kms"
    }
  }
}

resource "aws_dynamodb_table" "encrypted" {
  name         = "${var.project_name}-secrets"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"
  attribute {
    name = "id"
    type = "S"
  }
  server_side_encryption {
    enabled     = true
    kms_key_arn = aws_kms_key.data.arn
  }
  tags = { Name = "${var.project_name}-secrets" }
}
resource "aws_sqs_queue" "encrypted" {
  name                              = "${var.project_name}-encrypted"
  kms_master_key_id                 = aws_kms_key.data.arn
  kms_data_key_reuse_period_seconds = 300
  message_retention_seconds         = 3600
}
