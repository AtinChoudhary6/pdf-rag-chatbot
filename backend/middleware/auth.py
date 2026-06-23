import os
from fastapi import Header, HTTPException

API_KEY = os.getenv("BACKEND_API_KEY")


def verify_api_key(x_api_key: str = Header(...)):
    """
    Simple shared-secret check. The client must send the same key
    (set in BACKEND_API_KEY) in the 'x-api-key' header on every request
    to a protected route.
    """
    if not API_KEY:
        # If no key is configured on the backend, auth is effectively disabled.
        return
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
