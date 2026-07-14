variable "aws_region" {
  type    = string
  default = "us-east-1"
}
variable "project_name" {
  type    = string
  default = "saa-lab-01"
}
variable "per_az_nat" {
  type        = bool
  default     = false
  description = "false usa um NAT barato; true cria um NAT por AZ."
}
