import os

def get_version():
    version_path = os.path.join(os.path.dirname(__file__), "VERSION")
    if os.path.exists(version_path):
        with open(version_path) as f:
            return f.read().strip()
    return "UNKNOWN"
