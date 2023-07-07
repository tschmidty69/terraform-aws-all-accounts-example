terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

variable "aws_account_id" {
  description = "account_id"
  type        = string
|}

# Add terraform here