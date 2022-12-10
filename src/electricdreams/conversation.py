import json
import os
from typing import List

import openai


class Conversation:
    def __init__(self, cache_dir=None):
        """
        Initialize a new conversation class with will allow for stateful queries
        This will set up openai api key and some key values.
        Among other things, this class has a state in respect to the previous sentences.
        If you wanted to get rid of the previous state, you need to reinstantiate
        """
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.start_sequence: str = " AI:"
        self.restart_sequence: str = " Human: "
        self.conversation: List[str] = []
        self.model: str = "text-davinci-003"
        self.temperature: float = 0.9
        self.max_tokens: int = 150
        self.top_p: int = 1
        self.frequency_penalty: float = 0.0
        self.presence_penalty: float = 0.6

    def query(self, prompt: str = None):
        # If not having an ending dot it will be added
        prompt = prompt.strip()
        if prompt[:-1] != ".":
            prompt += "."

        # This prompt will be added to the previous history
        # If first prompt, do not prepend the restart_sequence
        if len(self.conversation) > 0:
            self.conversation.append(self.restart_sequence + prompt)
        else:
            self.conversation.append(prompt)

        # print("\n*******\nDEBUG request: " + str(prompt))
        response = openai.Completion.create(
            prompt="\n".join(self.conversation),  # Construct a long sentence
            model=self.model,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            # stream = True,
            stop=[self.start_sequence, self.restart_sequence],
        )
        # print("DEBUG response: " + str(response))

        try:
            obj = json.loads(str(response))
            ret = str(obj["choices"][0]["text"]).strip()
        except Exception as e:
            print("Inner exception! " + str(e))
            ret = ""
            # print("\n**********\nDEBUG ret: " + ret)

        # AIs response will also be added to the previous history for completeness
        if len(ret) > 0:
            self.conversation.append(self.start_sequence + ret)
        return ret
