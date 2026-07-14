variable "aws_region" {
  type        = string
  default     = "us-east-1"
  description = "WAF CLOUDFRONT exige us-east-1."
  validation {
    condition     = var.aws_region == "us-east-1"
    error_message = "Este lab global deve ser implantado em us-east-1."
  }
}
variable "project_name" {
  type    = string
  default = "saa-lab-03"
}
