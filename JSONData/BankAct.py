# Dumps Lab
# Converts JSON to Python Dictionary

import json 

bank_account = {
    "custID": 8675309,
    "name": "Justin Jefferson",
    "account_number": 9876543210
}

bankjson = json.dumps(bank_account,indent=4)

print(bankjson)