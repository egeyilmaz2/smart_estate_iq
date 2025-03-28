import json
import os
import threading
from src.config import CHECKPOINT_FILE

# Global lock to prevent concurrent file access
checkpoint_lock = threading.Lock()

def load_checkpoint(site_name: str) -> dict:
    """
    Loads the checkpoint data for the given site from the JSON file.
    If the file doesn't exist or the site has no checkpoint, returns a default record.
    """
    with checkpoint_lock:
        if not os.path.exists(CHECKPOINT_FILE):
            return {"last_page": 0, "last_link": "", "stage": ""}
        try:
            with open(CHECKPOINT_FILE, "r") as f:
                data = json.load(f)
        except Exception as e:
            # In case of error during file read/parse, return default record
            return {"last_page": 0, "last_link": "", "stage": ""}
    return data.get(site_name, {"last_page": 0, "last_link": "", "stage": ""})


def update_checkpoint(site_name: str, last_page: int, last_link: str, stage: str):
    """
    Updates or creates the checkpoint for the given site by directly overwriting the file.
    This method writes directly to the file without using a temporary file.
    Note: This approach is simpler but does not guarantee atomicity.
    """
    with checkpoint_lock:
        data = {}
        # If the checkpoint file exists, load its content
        if os.path.exists(CHECKPOINT_FILE):
            try:
                with open(CHECKPOINT_FILE, "r") as f:
                    data = json.load(f)
            except Exception:
                data = {}
        # Update the checkpoint for the given site
        data[site_name] = {
            "last_page": last_page,
            "last_link": last_link,
            "stage": stage
        }
        # Ensure the directory for the checkpoint file exists
        directory = os.path.dirname(CHECKPOINT_FILE)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        # Directly write the updated data to the checkpoint file
        with open(CHECKPOINT_FILE, "w") as f:
            json.dump(data, f, indent=4)
