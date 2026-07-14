data "aws_availability_zones" "available" { state = "available" }
locals {
  subnets = {
    a = { cidr = "10.50.10.0/24", az = data.aws_availability_zones.available.names[0] }
    b = { cidr = "10.50.11.0/24", az = data.aws_availability_zones.available.names[1] }
  }
  dax_actions = [
    "dynamodb:BatchGetItem",
    "dynamodb:BatchWriteItem",
    "dynamodb:ConditionCheckItem",
    "dynamodb:DeleteItem",
    "dynamodb:DescribeTable",
    "dynamodb:GetItem",
    "dynamodb:PutItem",
    "dynamodb:Query",
    "dynamodb:Scan",
    "dynamodb:UpdateItem"
  ]
}
resource "aws_dynamodb_table" "orders" {
  name         = "${var.project_name}-orders"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "customerId"
  range_key    = "orderId"
  attribute {
    name = "customerId"
    type = "S"
  }
  attribute {
    name = "orderId"
    type = "S"
  }
  server_side_encryption { enabled = true }
  point_in_time_recovery { enabled = false }
  tags = { Name = "${var.project_name}-orders" }
}

resource "aws_vpc" "this" {
  cidr_block           = "10.50.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags                 = { Name = "${var.project_name}-vpc" }
}
resource "aws_subnet" "dax" {
  for_each          = local.subnets
  vpc_id            = aws_vpc.this.id
  cidr_block        = each.value.cidr
  availability_zone = each.value.az
  tags              = { Name = "${var.project_name}-dax-${each.key}" }
}
resource "aws_security_group" "client" {
  name_prefix = "${var.project_name}-client-"
  description = "Cliente DAX autorizado"
  vpc_id      = aws_vpc.this.id
  tags        = { Name = "${var.project_name}-client-sg" }
}
resource "aws_security_group" "dax" {
  name_prefix = "${var.project_name}-dax-"
  description = "DAX somente do client SG"
  vpc_id      = aws_vpc.this.id
  tags        = { Name = "${var.project_name}-dax-sg" }
}
resource "aws_vpc_security_group_ingress_rule" "dax" {
  security_group_id            = aws_security_group.dax.id
  referenced_security_group_id = aws_security_group.client.id
  ip_protocol                  = "tcp"
  from_port                    = 8111
  to_port                      = 8111
}
resource "aws_vpc_security_group_egress_rule" "client_to_dax" {
  security_group_id            = aws_security_group.client.id
  referenced_security_group_id = aws_security_group.dax.id
  ip_protocol                  = "tcp"
  from_port                    = 8111
  to_port                      = 8111
}
resource "aws_vpc_security_group_egress_rule" "dax" {
  security_group_id = aws_security_group.dax.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "-1"
}

data "aws_iam_policy_document" "dax_assume" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["dax.amazonaws.com"]
    }
  }
}
resource "aws_iam_role" "dax" {
  count              = var.enable_dax ? 1 : 0
  name               = "${var.project_name}-dax-role"
  assume_role_policy = data.aws_iam_policy_document.dax_assume.json
}
data "aws_iam_policy_document" "dax_table" {
  statement {
    actions   = local.dax_actions
    resources = [aws_dynamodb_table.orders.arn, "${aws_dynamodb_table.orders.arn}/index/*"]
  }
}
resource "aws_iam_role_policy" "dax" {
  count  = var.enable_dax ? 1 : 0
  name   = "OrdersTableAccess"
  role   = aws_iam_role.dax[0].id
  policy = data.aws_iam_policy_document.dax_table.json
}
resource "aws_dax_subnet_group" "this" {
  count      = var.enable_dax ? 1 : 0
  name       = "${var.project_name}-dax-subnets"
  subnet_ids = values(aws_subnet.dax)[*].id
}
resource "aws_dax_cluster" "this" {
  count              = var.enable_dax ? 1 : 0
  cluster_name       = "${var.project_name}-dax"
  iam_role_arn       = aws_iam_role.dax[0].arn
  node_type          = "dax.t3.small"
  replication_factor = var.dax_replication_factor
  security_group_ids = [aws_security_group.dax.id]
  subnet_group_name  = aws_dax_subnet_group.this[0].name
  server_side_encryption { enabled = true }
  depends_on = [aws_iam_role_policy.dax]
}
