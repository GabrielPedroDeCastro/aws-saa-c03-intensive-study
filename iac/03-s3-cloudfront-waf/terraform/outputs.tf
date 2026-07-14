output "bucket_name" { value = aws_s3_bucket.content.id }
output "distribution_id" { value = aws_cloudfront_distribution.this.id }
output "website_url" { value = "https://${aws_cloudfront_distribution.this.domain_name}" }
output "web_acl_arn" { value = aws_wafv2_web_acl.this.arn }
