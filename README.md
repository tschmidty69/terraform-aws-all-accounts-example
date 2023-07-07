# README #

Organization Backup Policies and Roles to configure Enterprise wide AWS Backup

### What is this repository for? ###

* This repository is used to configure AWS Backup Policies to support 5 tiers of backup criticality
  Member accounts will be configured by AFT Global Customizations

### How do I get set up? ###

Changes are pushed to the management account via a bitbucket pipeline

### Installation steps

* Create cross account backup roles
* Create keys
* Create vaults

### Running scripts

Because we are attempting to run against all accounts in the organization, we have to jump through a few hoops.
These steps will be part of the bitbucket pipeline.

cd utils
export AWS_REGION="us-west-2"
export OIDC_ROLE_NAME="BitbucketPipelineRole"
pip install --user -r utils/requirements.txt
python utils/generate_providers.py



### Making changes

Run the aws-invoke-customizations to push new changes from aft_global_customizations to accounts

I use this event to push to the two sandbox accounts

{
  "include": [
    {
      "type": "accounts",
      "target_value": [
        "765776808422",
        "461086180594"
      ]
    }
  ]
}

### Who do I talk to? ###

* tschmidt@tnc.org