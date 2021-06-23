import os

from flask import Flask

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

# Save KEY VAULT URL in the web app application settings
AZUE_KEY_VAULT_URL = os.environ.get('https://arashi22690kv02.vault.azure.net/', '')
#AZUE_KEY_VAULT_URL = os.environ.get('AZUE_KEY_VAULT_URL', '')
# AZUE_KEY_VAULT_URL = "https://keyvaultdemoapp.vault.azure.net/"

@app.route("/")
def hello():
    return "Hello, Azure!"
    
@app.route('/secret')
def index():
    """Fetch secret from Azure Key Vault

    Returns:
        str: Response message to be displayed.
    """
    # Use Default credential. This has fallback authentication mechanism
    credential = DefaultAzureCredential()
    # Authenticate to Azure Key Vault.
    secret_client = SecretClient(vault_url=AZUE_KEY_VAULT_URL, credential=credential)
    # Fetch secrets created in Azure Key Vault
    secrets = secret_client.get_secret('arashi22690testkey')
    name = secrets.name
    value = secrets.value
    # Show secret name and it's value in the response
    response = f'secret {name} value is {value}'
    return response

##
if __name__ == "__main__":
    app.run(debug=True)
