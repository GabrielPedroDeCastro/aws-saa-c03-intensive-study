variable "aws_region" {
  type    = string
  default = "us-east-1"
}
variable "project_name" {
  type    = string
  default = "saa-lab-05"
}
variable "enable_dax" {
  type        = bool
  default     = false
  description = "DAX custa por hora. O padrão usa somente DynamoDB."
}
variable "dax_replication_factor" {
  type    = number
  default = 1
  validation {
    condition     = contains([1, 3], var.dax_replication_factor)
    error_message = "Use 1 (estudo) ou 3 (HA)."
  }
}
