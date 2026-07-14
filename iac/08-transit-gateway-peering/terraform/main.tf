data "aws_availability_zones" "available" { state = "available" }
locals {
  use_tgw = var.connectivity_mode == "TransitGateway"
  vpcs = {
    a = { cidr = "10.81.0.0/16", subnet_cidr = "10.81.1.0/24", az = data.aws_availability_zones.available.names[0], peer_cidr = "10.82.0.0/16" }
    b = { cidr = "10.82.0.0/16", subnet_cidr = "10.82.1.0/24", az = data.aws_availability_zones.available.names[1], peer_cidr = "10.81.0.0/16" }
  }
}
resource "aws_vpc" "this" {
  for_each             = local.vpcs
  cidr_block           = each.value.cidr
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags                 = { Name = "${var.project_name}-vpc-${each.key}" }
}
resource "aws_subnet" "this" {
  for_each          = local.vpcs
  vpc_id            = aws_vpc.this[each.key].id
  cidr_block        = each.value.subnet_cidr
  availability_zone = each.value.az
  tags              = { Name = "${var.project_name}-subnet-${each.key}" }
}
resource "aws_route_table" "this" {
  for_each = local.vpcs
  vpc_id   = aws_vpc.this[each.key].id
  tags     = { Name = "${var.project_name}-rt-${each.key}" }
}
resource "aws_route_table_association" "this" {
  for_each       = local.vpcs
  subnet_id      = aws_subnet.this[each.key].id
  route_table_id = aws_route_table.this[each.key].id
}

resource "aws_vpc_peering_connection" "this" {
  count       = local.use_tgw ? 0 : 1
  vpc_id      = aws_vpc.this["a"].id
  peer_vpc_id = aws_vpc.this["b"].id
  auto_accept = true
  tags        = { Name = "${var.project_name}-a-b" }
}
resource "aws_route" "peering" {
  for_each                  = local.use_tgw ? {} : local.vpcs
  route_table_id            = aws_route_table.this[each.key].id
  destination_cidr_block    = each.value.peer_cidr
  vpc_peering_connection_id = aws_vpc_peering_connection.this[0].id
}

resource "aws_ec2_transit_gateway" "this" {
  count                           = local.use_tgw ? 1 : 0
  description                     = "${var.project_name} hub de rede"
  amazon_side_asn                 = 64512
  auto_accept_shared_attachments  = "enable"
  default_route_table_association = "enable"
  default_route_table_propagation = "enable"
  dns_support                     = "enable"
  vpn_ecmp_support                = "enable"
  tags                            = { Name = "${var.project_name}-tgw" }
}
resource "aws_ec2_transit_gateway_vpc_attachment" "this" {
  for_each           = local.use_tgw ? local.vpcs : {}
  subnet_ids         = [aws_subnet.this[each.key].id]
  transit_gateway_id = aws_ec2_transit_gateway.this[0].id
  vpc_id             = aws_vpc.this[each.key].id
  tags               = { Name = "${var.project_name}-attach-${each.key}" }
}
resource "aws_route" "tgw" {
  for_each               = local.use_tgw ? local.vpcs : {}
  route_table_id         = aws_route_table.this[each.key].id
  destination_cidr_block = each.value.peer_cidr
  transit_gateway_id     = aws_ec2_transit_gateway.this[0].id
  depends_on             = [aws_ec2_transit_gateway_vpc_attachment.this]
}
