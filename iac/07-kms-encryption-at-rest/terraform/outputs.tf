output "kms_key_arn" { value = aws_kms_key.data.arn }
output "kms_alias" { value = aws_kms_alias.data.name }
output "bucket_name" { value = aws_s3_bucket.encrypted.id }
output "table_name" { value = aws_dynamodb_table.encrypted.name }
output "queue_url" { value = aws_sqs_queue.encrypted.url }
