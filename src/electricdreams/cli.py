import traceback
import electricdreams as ed
import argparse

def main(prompt : str = None, interactive : bool = False):
  """
  CLI interface for electricdreams
  Has both argumentparse and main() args to allow it to be called
  from a different main() implementation (see "adventure.py" for an example)
  These will become argparse defaults
  """
  args : str = None
  parser : argparse.ArgumentParser = None
  conversation : ed.Conversation() = None
  ret : str = None

  # Some constants
  PROMPT_HUMAN : str = "Human: "
  PROMPT_AI : str = "AI: "
  COMMAND_QUIT : str = "quit"
  
  # Initialize args
  parser = argparse.ArgumentParser(description="Chat GPT interface")
  parser.add_argument("-p", "--prompt", type=str, required=False, default=prompt, help="Initial prompt")
  parser.add_argument("-i", "--interactive", type=bool, default=interactive, required=False, help="Interactive session")
  args = parser.parse_args()

  # A session without an initial prompt will become instantly interactive
  # We need to ask for the prompt either
  if args.prompt == None:
    interactive = True
    prompt = input(PROMPT_HUMAN)
  else:
    interactive = args.interactive
    prompt = args.prompt

  # Initialize the conversation - will become a oneoff if interactive = False, will reuse previous
  # sentences if interactive = True
  conversation = ed.Conversation()
  #painter = ed.Painter() # "Imagine" the described text with stable difussion

  # Iterate in case of interactive mode
  while True:

    try:

      # Get some text based on the prompt
      ret = conversation.query(prompt)
      if len(ret) == 0: continue # Sometimes it happens...
      print(ret)

      # Paint the described situation
      #image = painter.paint(ret)

      # Non-interactive mode will end up here
      if interactive == False:
        break

      # Get additional prompts when in interactive mode
      prompt = input(PROMPT_HUMAN)
      if len(prompt) == 0:
        continue

      # Detect end of conversation
      if prompt == COMMAND_QUIT:
        print("... finishing!")
        break

    except Exception as e:
      print(traceback.format_exc())
      #print("Exception!")
      #print(str(e))
      #print(".")
      #pass

if __name__ == "__main__":
  main()