import requests
import base64

API_SERVER = "https://api.openshift.example.com:6443"
NAMESPACE = "my-namespace"
SA_NAME = "my-sa"
USER_TOKEN = "your-admin-token"
HEADERS = {"Authorization": f"Bearer {USER_TOKEN}"}

# Get secret name
sa_url = f"{API_SERVER}/api/v1/namespaces/{NAMESPACE}/serviceaccounts/{SA_NAME}"
sa_resp = requests.get(sa_url, headers=HEADERS, verify='/path/to/ca.crt')
secret_name = next(s['name'] for s in sa_resp.json()['secrets'] if 'token' in s['name'])

# Get token from secret
secret_url = f"{API_SERVER}/api/v1/namespaces/{NAMESPACE}/secrets/{secret_name}"
secret_resp = requests.get(secret_url, headers=HEADERS, verify='/path/to/ca.crt')
token_b64 = secret_resp.json()['data']['token']
token = base64.b64decode(token_b64).decode()

print("Token:", token)
