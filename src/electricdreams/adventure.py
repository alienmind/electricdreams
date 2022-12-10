import traceback
from electricdreams import notebook, cli
import argparse

DEF_THEME = "cyberpunk"

def main():

  # What this adventure will be about
  theme : str

  # Parse arguments - only when not running from a notebook
  if not notebook.is_notebook():
    parser = argparse.ArgumentParser(description="AIs generated text adventure")
    parser.add_argument("-t", "--theme", type=str, required=False, help="Theme",
                        default = DEF_THEME)
    args,extra = parser.parse_known_args()
    theme = args.theme
  else:
    theme = DEF_THEME

  print("TO EXIT, TYPE: quit")

  prompt = "" \
    "I want you to act as if you are a classic text adventure game and we are playing. "\
    "I don’t want you to ever break out of your character, and you must not refer to yourself in any way. "\
    "If I want to give you instructions outside the context of the game, I will use curly brackets {like this} "\
    "but otherwise you are to stick to being the text adventure program. "\
    f"In this game, the setting is a {theme} world. "\
    "Each room should have at least 3 sentence descriptions. "\
    "Start by displaying the first room at the beginning of the game, "\
    "and wait for my to give you my first command."
  
  return cli.main(prompt = prompt, interactive = True, strict_args=False) # This will allow chaining argparsers

if __name__ == "__main__":
  main()
