import requests
import sys
import json

if len(sys.argv) < 2:
	print('USAGE : python scope_pr.py [programm]')
	sys.exit()

programm = sys.argv[1]
file_path = None

if  len(sys.argv) >= 4 and sys.argv[2] == '-o':
	file_path = sys.argv[3]


url = 'https://hackerone.com/graphql'
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}
json_data = {
    "operationName": "PolicyScopes",
    "variables": {
        "handle": programm
    },
    "query": """
    query PolicyScopes($handle: String!) {
      team(handle: $handle) {
        structured_scopes {
          nodes {
            asset_identifier
            asset_type
            eligible_for_bounty
            instruction
          }
        }
      }
    }
    """
}

res = requests.post(url , json=json_data , headers=headers)
data = res.json()
nodes = data['data']['team']['structured_scopes']['nodes']

all_scopes = []
for scope in nodes:
	print(scope['asset_identifier'])
	all_scopes.append(scope['asset_identifier'])


if file_path:
	with open(file_path , 'w') as file:
		file.write("\n".join(all_scopes))
