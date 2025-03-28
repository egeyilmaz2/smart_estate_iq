import random
import json
import os
import threading
from src.config import PROXY_FILE

# Global lock for proxy file operations
proxy_lock = threading.Lock()

def load_proxies():
    """
    Reads the proxy list from the PROXY_FILE.
    Returns an empty list if the file does not exist.
    """
    if os.path.exists(PROXY_FILE):
        with proxy_lock, open(PROXY_FILE, "r") as f:
            data = json.load(f)
            return data.get("proxies", [])
    return []

def get_random_proxy():
    """
    Selects and returns a random proxy from the saved proxy list.
    Returns None if no proxies are available.
    """
    proxies = load_proxies()
    if proxies:
        return random.choice(proxies)
    return None
