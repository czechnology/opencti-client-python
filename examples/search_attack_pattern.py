# coding: utf-8

from pycti import OpenCTIApiClient

# Variables
api_url = "https://demo.opencti.io"
api_token = "YOUR_TOKEN"

# OpenCTI initialization
opencti_api_client = OpenCTIApiClient(api_url, api_token)

# Search
attack_patterns = opencti_api_client.attack_pattern.list(search="localgroup")

# Print
print(attack_patterns)
