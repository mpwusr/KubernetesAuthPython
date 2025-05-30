import requests
import base64

API_SERVER = "https://api.openshift.example.com:6443"
NAMESPACE = "my-namespace"
SA_NAME = "my-sa"
USER_TOKEN = "your-admin-token"
CA_CERT = "/path/to/ca.crt"

headers = {"Authorization": f"Bearer {USER_TOKEN}"}

# Get service account details
sa_url = f"{API_SERVER}/api/v1/namespaces/{NAMESPACE}/serviceaccounts/{SA_NAME}"
sa_resp = requests.get(sa_url, headers=headers, verify=CA_CERT)
secret_name = next(s['name'] for s in sa_resp.json()['secrets'] if 'token' in s['name'])

# Get secret with token
secret_url = f"{API_SERVER}/api/v1/namespaces/{NAMESPACE}/secrets/{secret_name}"
secret_resp = requests.get(secret_url, headers=headers, verify=CA_CERT)
token_b64 = secret_resp.json()['data']['token']
token = base64.b64decode(token_b64).decode()

print("Retrieved Token:")
print(token)

