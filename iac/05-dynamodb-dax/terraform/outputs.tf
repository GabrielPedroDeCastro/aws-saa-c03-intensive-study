output "table_name" { value = aws_dynamodb_table.orders.name }
output "table_arn" { value = aws_dynamodb_table.orders.arn }
output "dax_enabled" { value = var.enable_dax }
output "dax_cluster_address" { value = try(aws_dax_cluster.this[0].cluster_address, "disabled") }
output "client_security_group_id" { value = aws_security_group.client.id }
