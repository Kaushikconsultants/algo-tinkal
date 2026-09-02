import os
from dhanhq import dhanhq
from dotenv import load_dotenv

load_dotenv()
client_id = os.getenv("DHAN_CLIENT_ID")
access_token = os.getenv("DHAN_ACCESS_TOKEN")

print("Authenticating with DhanHQ...")
try:
    # In v2, we pass client_id and access_token directly or via DhanContext
    # Let's try the DhanContext approach if direct doesn't work, but actually
    # the docs say: dhanhq(client_id, access_token) for v2 as well in some examples.
    # Let's inspect the signature dynamically again.
    import inspect
    sig = inspect.signature(dhanhq.__init__)
    print(f"Signature: {sig}")
except Exception as e:
    print(e)
