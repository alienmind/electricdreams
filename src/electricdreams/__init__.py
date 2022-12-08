# Import configs
from .config import CONFIG_LOCATIONS
import dotenv
import os

# Used for missing keys
class MissingAPIKeysError(ValueError):
    pass

# Initialize secrets as env variables
for c in CONFIG_LOCATIONS:
    dotenv.load_dotenv(os.path.join(c))

# We will actually error on missing keys - this is a no go
if os.getenv('OPENAI_API_KEY') == None or \
   os.getenv('HUGGINGFACE_API_KEY') == None:
   raise MissingAPIKeysError("\n\nEither OPENAI_API_KEY or HUGGINGFACE_API_KEY is missing.\n" \
                             "Go get your own keys from https://openai.com/api/\n" \
                             " and https://huggingface.co/inference-api\n" \
                             "This should be place in a file under the following locations:\n"\
                             + " ".join(CONFIG_LOCATIONS) + "\n\n File contents should be similar to:\n"
                             "OPENAI_API_KEY=\"sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\"\n" \
                             "HUGGINGFACE_API_KEY=\"hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\"\n" \
                             "")

# Import the classes and functions from the module
from .hasher import Hasher
from .painter import Painter
from .chatter import Conversation

# Export the classes and functions from the module
__all__ = [
    'Hasher',
    'Painter',
    'Conversation',
    'CONFIG_DIR',
]