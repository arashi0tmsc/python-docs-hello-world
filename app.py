from flask import Flask

app = Flask(__name__)

# Save KEY VAULT URL in the web app application settings
AZUE_KEY_VAULT_URL = "https://arashi22690kv02.vault.azure.net/"
#AZUE_KEY_VAULT_URL = os.environ.get('https://arashi22690kv02.vault.azure.net/', '')
#AZUE_KEY_VAULT_URL = os.environ.get('AZUE_KEY_VAULT_URL', '')
# AZUE_KEY_VAULT_URL = "https://keyvaultdemoapp.vault.azure.net/"

@app.route("/")
def hello():
    return "Hello, Azure!"
    
