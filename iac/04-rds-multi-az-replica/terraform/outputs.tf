output "primary_endpoint" { value = aws_db_instance.primary.address }
output "primary_port" { value = aws_db_instance.primary.port }
output "read_replica_endpoint" { value = try(aws_db_instance.replica[0].address, "disabled") }
output "master_secret_arn" { value = aws_db_instance.primary.master_user_secret[0].secret_arn }
output "client_security_group_id" { value = aws_security_group.client.id }
