---
hide:
  - toc
---

# Known AWS Accounts

This repository contains known AWS Account IDs (those used by vendors and AWS services).  The purpose of this is so when a trust relationship or CloudTrail events show an AWS account ID that is unknown to you, you can more quickly identify the purpose of that account.

This is meant to be used with tools to remove the need for manual web searches.

## Contributing

!!! warning

    Account IDs need to be publicly documented.

    In some circumstances (please ask us first) IDs mentioned here may not have public references, but should have permission from the company.  

    The reasons for this are:

    1. We want to ensure these account IDs are really for who they say they are.
    1. Some companies may not want their account IDs mentioned publicly.


Each entry has the following schema:

| Field    | Type             | Notes |
| -------- | ---------------- | ----- |
| name     | String           | Vendor name |
| aliases  | Array[String]    | Additional names these accounts may go by (vendors sharing account IDs for different brands) |
| sources  | Array[String]    | List of URLs that publicly mentions the account ID in association with this vendor. |
| type     | Optional[String] | Optional parameter, mostly used to reference `aws` |
| accounts | Array[String]    | Array of 12-digit AWS account IDs |

Open a pull request on the `accounts.yaml` found in the root of this repository either updating, removing or adding a new entry.