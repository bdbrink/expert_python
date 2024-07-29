import secrets

def main():
    
    tokenb = secrets.token_bytes(nbytes=None)
    print(tokenb)
    
    tokenh = secrets.token_hex(nbytes=None)
    print(tokenh)
    
    safe_url = secrets.token_urlsafe(nbytes=None)
    print(safe_url)
    
main()