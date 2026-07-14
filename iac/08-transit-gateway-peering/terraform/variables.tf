variable "aws_region" {
  type    = string
  default = "us-east-1"
}
variable "project_name" {
  type    = string
  default = "saa-lab-08"
}
variable "connectivity_mode" {
  type        = string
  default     = "Peering"
  description = "Peering (barato) ou TransitGateway (pago)."
  validation {
    condition     = contains(["Peering", "TransitGateway"], var.connectivity_mode)
    error_message = "Use Peering ou TransitGateway."
  }
}
