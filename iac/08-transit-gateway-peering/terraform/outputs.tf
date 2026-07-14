output "connectivity_mode" { value = var.connectivity_mode }
output "vpc_ids" { value = { for key, vpc in aws_vpc.this : key => vpc.id } }
output "peering_connection_id" { value = try(aws_vpc_peering_connection.this[0].id, "disabled") }
output "transit_gateway_id" { value = try(aws_ec2_transit_gateway.this[0].id, "disabled") }
output "route_table_ids" { value = { for key, rt in aws_route_table.this : key => rt.id } }
