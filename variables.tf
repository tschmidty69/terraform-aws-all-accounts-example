variable "resource_suffix" {
  description = "Suffix to append to created resources, eg. vpc-[region]-[environment]-[account-name]"
  type        = string
  default     = null
}

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-west-2"
}
