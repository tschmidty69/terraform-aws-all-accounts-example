# README #

### What is this repository for? ###

One way to configure a terraform repository to run against all accounts in an AWS organization.
This is just one way to do this, but I really like avoiding 3rd party programs as much as possible
and wanted to have something where others could just develop a standard terraform module and have it run
without worrying about the "all accounts" part.

This runs a python script that outputs a json formatted list of providers and modules for each account
that is not explicitly excluded in the python script. Terraform will then read that and run the specified
module (member_account) against all of the accounts.

The providers/modules exported will look something like this:

```
{
  "provider": {
    "aws": [
      {
        "alias": "member_account-1234567890",
        "region": "us-west-2",
        "assume_role": {
          "role_arn": "arn:aws:iam::1234567890:role/role_name",
        }
      }
    ]
  },
  "module": {
    "member_account-1234567890": {
      "source": "./modules/member_account",
      "providers": {
        "aws": "aws.member_account-1234567890"
      },
      "aws_account_id": "1234567890"
    }
  }
}
```

### Configuration

For terraform you really don't need to set the region since it is set via environment variables as below.
In fact, the provider will not be used and main.tf is just there to provide a place for a backend, for which I 
use Terraform Cloud. You could also use any other backend type just please don't store your state file locally. 

Configure the accounts to exclude in the python script
Koalato
NOTE: This is set to run against one region only. You could add multiple providers per account in the python file
      to run against multiple regions or use a list of regions to run against. Or something else entirely, your call.

### Running steps

NOTE: THE ROLE_NAME YOU PASS MUST ALREADY EXIST AND WHATEVER CREDENTIALS YOU RUN THIS AS MUST HAVE RIGHTS TO ASSUME THAT ROLE!

NOTE: I use SSO, so I just export temporary credentials into the shell I am running from. 
      There are other ways to authenticate, but this is the way.

Because we are attempting to run against all accounts in the organization, we have to run a python script
before running the terraform module.

In reality, I run these steps as part of a bitbucket pipeline or github actions using OIDC tokens. In that case
you would use assume_role_with_web_identity in the python script and a few more variables. Shoot me message if that 
is something you would like to see an example of.

```
export AWS_REGION="us-west-2"
export ROLE_NAME="<Name of role to assume in each member account>"
pip install --user -r utils/requirements.txt
python utils/generate_providers.py
terraform init
terraform plan
terraform apply
```

### Things you could make better

Multiple regions would be nice to have. You could also easily pass things like the OU or Account Name to the module
as variables or have the python script parse it and configure different modules to customize the module behavior or selection.