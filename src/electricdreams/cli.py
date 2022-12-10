import argparse

from electricdreams import notebook
from electricdreams.chatter import Chat, ChatResponse


def main(prompt: str = None, interactive: bool = False, strict_args: bool = True):
    """
    CLI interface for electricdreams
    Has both argumentparse and main() args to allow it to be called
    from a different main() implementation (see "adventure.py" for an example)
    These will become argparse defaults
    """
    args: str = None
    parser: argparse.ArgumentParser = None
    chat: Chat = None
    response: ChatResponse = None

    # Initialize args - only if running from a proper shell
    if not notebook.is_notebook():
        parser = argparse.ArgumentParser(description="Chat GPT interface")
        parser.add_argument("-p", "--prompt", type=str, required=False, default=prompt, help="Initial prompt")
        parser.add_argument(
            "-i", "--interactive", type=bool, default=interactive, required=False, help="Interactive session"
        )
        if strict_args:
            args = parser.parse_args()
        else:
            args, extra = parser.parse_known_args()  # To allow chaining parsers
        prompt = args.prompt
        interactive = args.interactive

    # Create the chat session
    chat = Chat(has_images=False, is_interactive=interactive, input_fn=input)

    # Run the chat iteratively
    for response in chat.chat(prompt):
        print(response.text)
        if response.last_prompt == Chat.COMMAND_QUIT:
            print("... finishing!")
            break


if __name__ == "__main__":
    main()
