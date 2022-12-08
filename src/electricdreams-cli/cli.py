import traceback
import electricdreams as ed
import argparse

def main():
  # create an ArgumentParser object
  parser = argparse.ArgumentParser(description="AIs generated text adventure")
  
  # add an argument to the parser
  #parser.add_argument("-n", "--name", type=str, required=True, help="your name")

  # parse the arguments
  #args = parser.parse_args()

  conversation = ed.Conversation()
  #painter = ed.Painter()

  print("TO EXIT, TYPE: quit")
  prompt = "I want you to act as if you are a classic text adventure game and we are playing. I don’t want you to ever break out of your character, and you must not refer to yourself in any way. If I want to give you instructions outside the context of the game, I will use curly brackets {like this} but otherwise you are to stick to being the text adventure program. In this game, the setting is a fantasy adventure world. Each room should have at least 3 sentence descriptions. Start by displaying the first room at the beginning of the game, and wait for my to give you my first command."
  #print(prompt)
  while True:

    try:
      ret = conversation.query(prompt)
      if len(ret) == 0: continue
      #image = painter.paint(ret)
      print(ret)
    
      prompt = input("Human: ")
      if len(prompt) == 0:
        continue

      if prompt == "quit":
        print("... finishing game!")
        break
    except Exception as e:
      print(traceback.format_exc())
      #print("Exception!")
      #print(str(e))
      #print(".")
      #pass

if __name__ == "__main__":
  main()
