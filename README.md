# Known AWS Accounts

This repository contains known AWS Account IDs (those used by vendors and AWS services).  The purpose of this is so when a trust relationship or CloudTrail events show an AWS account ID that is unknown to you, you can more quickly identify the purpose of that account.

This is meant to be used with tools to remove the need for manual web searches.

## Contributing

Account IDs need to be publicly documented.

In some circumstances (please ask us first) IDs mentioned here may not have public references, but should have permission from the company.  

The reasons for this are:

1. We want to ensure these account IDs are really for who they say they are.
1. Some companies may not want their account IDs mentioned publicly.

Preview of Published Docs

For local development you will need Python 3.8+.

```shell
python3 -m venv .venv # create virtualenv
source .venv/bin/activate # activate virtualenv
pip install -r requirements.txt # install requirements
mkdocs serve 

## History

Copied from https://github.com/duo-labs/cloudmapper/blob/main/vendor_accounts.yaml which originally copied
https://github.com/dagrz/aws_pwn/blob/master/miscellanea/integrations.txt
