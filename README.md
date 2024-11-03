# csv2cb
A simple Python3 script that takes a list of SHA256 hashes in a CSV and adds them to the Carbon Black Blacklist via the Carbon Black Reputations Override API endpoint.

## Setup
I recommend creating a custom API Access Level in Carbon Black with only 'Create' permissions on the Reputations permission name (org.reputations) and limiting the API key to authorized IP's. 
1. Create custom Access Level in CB with 'Create' permissions on the Reputations (org.reputations) name
2. Create Carbon Black API Key
    - Select custom Access Level
    - Set authorized IPs
3. Save your API Key, the associated API ID and your Org Key (Found under Settings -> General) to a secure location (such as a password manager)
4. Update the URL on line 24 to your Carbon Black Cloud instances Cloud URL

## Use
1. Create a CSV called 'hashes.csv' with the SHA256 hashes in the first column within this scripts PWD
2. Run the script
3. Provide API Key, API ID and Org Key (copy/paste)
    
