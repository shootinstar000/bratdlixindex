from pathlib import Path
import tempfile
import traceback
import json
import sys
import os






try:
    port = 8080
except Exception as e:
    print(e)
    port = -1
if not 1 <= port <= 65535:
    print(
        "Please make sure the PORT environment variable is an integer between 1 and 65535"
    )
    sys.exit(1)

try:
    api_id = 2557747
    api_hash = "3022e575059ce68696f4fa4120ae33a2"
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the API_ID and API_HASH environment variables correctly")
    print("You can get your own API keys at https://my.telegram.org/apps")
    sys.exit(1)

try:
   # index_settings_str = is
    index_settings = {
  "index_all": False,
  "index_private": False,
  "index_group": False,
  "index_channel": True,
  "exclude_chats": [],
  "include_chats": [-1001750092497, -1001477645865 ]
} 
except Exception:
    traceback.print_exc()
    print("\n\nPlease set the INDEX_SETTINGS environment variable correctly")
    sys.exit(1)

try:
    session_string = "1BVtsOHIBu6KX9fXTUMcEQrtQbm2zuHE1owgkmu7GTGd8eL3N5wgO2i_LjxU-bbkjhFdQVifDSGpJU0hLoO--CLQpAofaRHXIW4lti-am0r4IqPvUaV_V0aiNA3d0DKBVdoy12_BgKHbb1mjUE2SDWJn1ACgExOL35AFKy_9bfg9jQoM-QAEF6M6x6oQ_vqrQpysUsQWfjUqRsjvsKdYXO4sa5fSdtjghvCz1cQQK8NhXk6xTj0bpwNhM6yuw0uKQFv3ylRhATdB5Y-LmtXE07NoTJY_CorxII58u9mtUXivxfbKpfDBxZ5898ycuc6XTgNLKmdBsTZkQIzEGkftzo_mR95erwS4="
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the SESSION_STRING environment variable correctly")
    sys.exit(1)

host = os.environ.get("HOST", "0.0.0.0")
debug = bool(os.environ.get("DEBUG"))
block_downloads = bool(os.environ.get("BLOCK_DOWNLOADS"))
results_per_page = int(os.environ.get("RESULTS_PER_PAGE", "20"))
logo_folder = Path(os.path.join(tempfile.gettempdir(), "logo"))
logo_folder.mkdir(parents=True, exist_ok=True)
username = os.environ.get("TGINDEX_USERNAME", "")
password = os.environ.get("PASSWORD", "")
SHORT_URL_LEN = int(os.environ.get("SHORT_URL_LEN", 3))
authenticated = bool(username and password)
SESSION_COOKIE_LIFETIME = int(os.environ.get("SESSION_COOKIE_LIFETIME") or "60")
try:
    SECRET_KEY = os.environ["SECRET_KEY"]
    if len(SECRET_KEY) != 32:
        raise ValueError("SECRET_KEY should be exactly 32 charaters long")
except (KeyError, ValueError):
    if authenticated:
        traceback.print_exc()
        print("\n\nPlease set the SECRET_KEY environment variable correctly")
        sys.exit(1)
    else:
        SECRET_KEY = ""
