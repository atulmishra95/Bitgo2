import requests


def get_transactions(trans):
    url = f'https://blockstream.info/api/block/{trans}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)

        transactions = data['tx_count']
        assert transactions == 2875, f"Expected 2875 transactions, but got {transactions}"

        transactions_id = data['id']
        print(f"Transaction Id is: {transactions_id}")

        assert transactions_id == '1234', f"Expected transaction ID '1234', but got {transactions_id}"
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")


trans = '000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732'
get_transactions(trans)
