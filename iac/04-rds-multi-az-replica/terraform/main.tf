data "aws_availability_zones" "available" { state = "available" }
locals {
  subnets = {
    a = { cidr = "10.40.10.0/24", az = data.aws_availability_zones.available.names[0] }
    b = { cidr = "10.40.11.0/24", az = data.aws_availability_zones.available.names[1] }
  }
}
resource "aws_vpc" "this" {
  cidr_block           = "10.40.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags                 = { Name = "${var.project_name}-vpc" }
}
resource "aws_subnet" "database" {
  for_each          = local.subnets
  vpc_id            = aws_vpc.this.id
  cidr_block        = each.value.cidr
  availability_zone = each.value.az
  tags              = { Name = "${var.project_name}-db-${each.key}" }
}
resource "aws_db_subnet_group" "this" {
  name       = "${var.project_name}-subnets"
  subnet_ids = values(aws_subnet.database)[*].id
  tags       = { Name = "${var.project_name}-db-subnets" }
}
resource "aws_security_group" "client" {
  name_prefix = "${var.project_name}-client-"
  description = "Anexe somente ao cliente autorizado"
  vpc_id      = aws_vpc.this.id
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = { Name = "${var.project_name}-client-sg" }
}
resource "aws_security_group" "database" {
  name_prefix = "${var.project_name}-db-"
  description = "PostgreSQL somente do client SG"
  vpc_id      = aws_vpc.this.id
  tags        = { Name = "${var.project_name}-db-sg" }
}
resource "aws_vpc_security_group_ingress_rule" "postgres" {
  security_group_id            = aws_security_group.database.id
  referenced_security_group_id = aws_security_group.client.id
  ip_protocol                  = "tcp"
  from_port                    = 5432
  to_port                      = 5432
  description                  = "Cliente autorizado"
}
resource "aws_vpc_security_group_egress_rule" "database" {
  security_group_id = aws_security_group.database.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "-1"
}

resource "aws_db_instance" "primary" {
  identifier                   = "${var.project_name}-primary"
  engine                       = "postgres"
  instance_class               = var.db_instance_class
  allocated_storage            = 20
  max_allocated_storage        = 40
  storage_type                 = "gp3"
  storage_encrypted            = true
  multi_az                     = true
  publicly_accessible          = false
  db_subnet_group_name         = aws_db_subnet_group.this.name
  vpc_security_group_ids       = [aws_security_group.database.id]
  username                     = "labadmin"
  manage_master_user_password  = true
  backup_retention_period      = 1
  auto_minor_version_upgrade   = true
  deletion_protection          = false
  skip_final_snapshot          = true
  delete_automated_backups     = true
  performance_insights_enabled = false
  apply_immediately            = true
  copy_tags_to_snapshot        = true
  tags                         = { Name = "${var.project_name}-primary" }
}
resource "aws_db_instance" "replica" {
  count                        = var.create_read_replica ? 1 : 0
  identifier                   = "${var.project_name}-replica"
  replicate_source_db          = aws_db_instance.primary.identifier
  instance_class               = var.db_instance_class
  db_subnet_group_name         = aws_db_subnet_group.this.name
  vpc_security_group_ids       = [aws_security_group.database.id]
  publicly_accessible          = false
  multi_az                     = false
  auto_minor_version_upgrade   = true
  skip_final_snapshot          = true
  delete_automated_backups     = true
  performance_insights_enabled = false
  apply_immediately            = true
  tags                         = { Name = "${var.project_name}-replica" }
}
