variable "aws_region" {
  type    = string
  default = "us-east-1"
}
variable "project_name" {
  type    = string
  default = "saa-lab-02"
}
variable "instance_type" {
  type    = string
  default = "t3.micro"
}
variable "desired_capacity" {
  type    = number
  default = 2
  validation {
    condition     = var.desired_capacity >= 2 && var.desired_capacity <= 4
    error_message = "Use de 2 a 4 instancias."
  }
}
