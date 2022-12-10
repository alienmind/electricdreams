import traceback

from PIL import Image

from electricdreams import Conversation, Painter


class ChatResponse:
    text: str
    image: Image
    last_prompt: str


class Chat:
    # Some constants
    PROMPT_HUMAN: str = "Human: "
    PROMPT_AI: str = "AI: "
    COMMAND_QUIT: str = "quit"

    # A Chat has a conversation and a Painter
    conversation: Conversation()
    painter: Painter()

    def __init__(self, has_images: bool = True, is_interactive: bool = True, input_fn=input):
        self.has_images = has_images
        self.is_interactive = is_interactive
        self.input_fn = input_fn
        self.conversation = Conversation()

        # With images requirement, we do need a painter
        if self.has_images:
            self.painter = Painter()
        else:
            self.painter = None
        pass

    def chat(self, prompt: str) -> ChatResponse:
        # An empty prompt will force interactive mode
        if prompt is None:
            prompt = self.input_fn(self.PROMPT_HUMAN)
            self.is_interactive = True

        # Iterate through the different prompts and responses
        while True:
            response = ChatResponse()
            try:
                # Get some text based on the prompt
                response.text = self.conversation.query(prompt)
                if len(response.text) == 0:
                    continue  # Sometimes it happens...

                # Paint the described situation
                if self.has_images:
                    response.image = self.painter.paint(response.text)

                # Return the response as in a generator
                response.last_prompt = prompt
                yield response

                # Non-interactive mode will end up here
                if not self.is_interactive:
                    break

                # Get additional prompts when in interactive mode
                prompt = self.input_fn(self.PROMPT_HUMAN)
                if len(prompt) == 0:
                    continue

                # Detect end of conversation
                if prompt == self.COMMAND_QUIT:
                    break

            except Exception as e:
                print("Exception!")
                print(str(e))
                print(traceback.format_exc())

        # Return last response
        return response
