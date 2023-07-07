import os
import json
import boto3

excluded_accounts = ["<ACCOUNTS I DONT WANT TO RUN AGAINST"]
aws_region = os.getenv('AWS_REGION')
role_name = os.getenv('ROLE_NAME')

org = boto3.client('organizations')
accounts_paginator = org.get_paginator('list_accounts')
accounts = []
for page in accounts_paginator.paginate():
 accounts += page['Accounts']

# Example you could hard code for testing

# accounts = [{'Arn': 'arn:aws:organizations::<ORG ACCOUNT ID>:account/<OU ID>/<MEMBER ACCOUNT ID>',
#  'Email': 'user@email.com',
#  'Id': '<MEMBER ACCOUNT ID>',
#  'JoinedMethod': 'CREATED',
#  'JoinedTimestamp': 'SOMETIME',
#  'Name': '<ID OR NAME>',
#  'Status': 'ACTIVE'
#  }]

from pprint import pprint as pp
#pp(accounts)

providers = {
  "provider": {
    "aws": [] 
  },
  "module": {}
}

for account in accounts:
  if account['Id'] in excluded_accounts:
    continue
  print("Member account: "+account['Id'])
  provider = {
    "alias": "member_account-"+account['Id'],
    "region": aws_region,
    "assume_role":{
      "role_arn": "arn:aws:iam::"+account['Id']+":role/"+role_name,
    }
  }
  providers['provider']['aws'].append(provider)
  module = {
    "source": "./modules/member_account",
    "providers": {
      "aws": "aws.member_account-"+account['Id']
    },
    "aws_account_id": account['Id']
  }
  providers['module']["member_account-"+account['Id']] = module

pp(providers)
with open('./providers_generated.tf.json', 'w', encoding='utf-8') as f:
    json.dump(providers, f, ensure_ascii=False, indent=2)