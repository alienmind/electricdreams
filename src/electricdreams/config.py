""" Possible paths for configuration variables """
""" OPENAI and Huggingface API keys will be looked for here """

import os

CONFIG_LOCATIONS = [
    os.getenv("HOME") + "/.config/electricdreams/electric.env",
    "/etc/electricdreams/electric.env"
]