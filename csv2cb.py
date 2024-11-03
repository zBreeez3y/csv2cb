#!/usr/env/python3

import re
import csv
import json
import time
from datetime import date
import getpass
import requests

#Setting date
today = date.today().strftime('%m/%d/%Y')

#Authentication Information
apiKey = getpass.getpass("Enter the CarbonBlack API key: ")
appId = getpass.getpass("Enter CarbonBlack AppID: ")
orgKey = getpass.getpass("Enter CarbonBlack Organization Key: ")
cbApiKey = f'{apiKey}/{appId}'

#Empty hash  array, will be filled from hashes CSV
hashes = []

#CarbonBlack API Route
cbRoute = f'https://<CarbonBlackCloudURL>/appservices/v6/orgs/{orgKey}/reputations/overrides/'
if "<CarbonBlackCloudURL>" in cbRoute:
    print("Update your Carbon Black Cloud URL on line 24")
    exit()

#Parse hashes/URL's from hashes CSV
print("[+] Parsing CSV for hashes.")
with open("hashes.csv", "r") as f:
    csv = csv.reader(f)
    for i in csv:
        sha256 = re.findall('[a-z0-9]{64}$', i[1])
        if sha256:
            hashes.append(sha256[0])
f.close()

#Add SHA256's to CarbonBlack Blacklist
print("[+] Adding hashes to CarbonBlack blacklist.")
for sha256 in hashes:
    #HTTP data
    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-TOKEN': cbApiKey
    }

    data = {
        "filename": "Malicious Hash IOC",
        "description": f'Pulled from hashes.csv on {today}',
        "override_list": "BLACK_LIST",
        "override_type": "SHA256",
        "sha256_hash": f'{sha256}'
    }
    block = requests.post(cbRoute, headers=headers, data=json.dumps(data))

print("[+] All hashes added to the CB Console blacklist.")
