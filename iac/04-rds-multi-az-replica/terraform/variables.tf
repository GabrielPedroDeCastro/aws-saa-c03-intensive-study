variable "aws_region" {
  type    = string
  default = "us-east-1"
}
variable "project_name" {
  type    = string
  default = "saa-lab-04"
}
variable "db_instance_class" {
  type    = string
  default = "db.t3.micro"
}
variable "create_read_replica" {
  type        = bool
  default     = false
  description = "false reduz custo e mantém apenas a instância Multi-AZ."
}
