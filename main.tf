# I use HassiCorp's Free Cloud Accounts
# Configure it to be CLI driven and run locally
# and create a workspace to hold your state
terraform {
  cloud {
    organization = "Your-Terraform-Cloud-Organization"

    workspaces {
      name = "terraform-aws-all-accounts-example-workspace"
    }
  }
}

# This provider will not actually be used since we create a new one for each account
provider "aws" {
  region = var.aws_region
}
