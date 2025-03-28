import os

# Directory for project resources (located at the project root)
RESOURCE_DIR = os.path.join("resources")

# Full paths for the JSON files
CHECKPOINT_FILE = os.path.join(RESOURCE_DIR, "checkpoints.json")
PROXY_FILE = os.path.join(RESOURCE_DIR, "proxies.json")
PROXY_API_LIST_FILE = os.path.join(RESOURCE_DIR, "proxy_apis.json")

# Other configuration values
TIMEOUT = 2                   # Timeout for page loads or requests (in seconds)
CONCURRENT_REQUESTS = 5        # Limit for concurrent requests (optional for Selenium usage)
