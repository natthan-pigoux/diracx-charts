import secrets
import base64
import hashlib
token = secrets.token_bytes()
# This is the secret to include in the request by setting the
# /DiracX/LegacyExchangeApiKey CS option in your legacy DIRAC installation
print(f"API key is diracx:legacy:{base64.urlsafe_b64encode(token).decode()}")

# This is the environment variable to set on the DiracX server
print(f"DIRACX_LEGACY_EXCHANGE_HASHED_API_KEY={hashlib.sha256(token).hexdigest()}")
