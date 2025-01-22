import json

# Load the JSON data from the file
with open("/Users/atulkumar/PycharmProjects/Bitgo2/payloads.json", 'r') as test:
    data = json.load(test)

# Print all response data of the Endpoint
print(data)

# Print all transaction IDs
for trans in data:
    print("Print all trx_id : " + trans['txid'])

# Check if there are at least 25 transactions and print the 5th transaction ID
if len(data) >= 25:
    print("Print 5th trx_id : " + data[4]['txid'])
else:
    print("There are less than 25 transactions in the data.")
