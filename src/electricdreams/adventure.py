import traceback
import electricdreams.cli as edcli
import argparse

def main():

  # Parse arguments
  parser = argparse.ArgumentParser(description="AIs generated text adventure")
  parser.add_argument("-t", "--theme", type=str, required=False, help="Theme",
                      default = "fantasy adventure world")
  args = parser.parse_args()

  print("TO EXIT, TYPE: quit")
  theme : str = args.theme
  prompt = "" \
    "I want you to act as if you are a classic text adventure game and we are playing. "\
    "I don’t want you to ever break out of your character, and you must not refer to yourself in any way. "\
    "If I want to give you instructions outside the context of the game, I will use curly brackets {like this} "\
    "but otherwise you are to stick to being the text adventure program. "\
    f"In this game, the setting is a {args.theme}. "\
    "Each room should have at least 3 sentence descriptions. "\
    "Start by displaying the first room at the beginning of the game, "\
    "and wait for my to give you my first command."
  
  return edcli.main(prompt = prompt, interactive = True)

if __name__ == "__main__":
  main()
