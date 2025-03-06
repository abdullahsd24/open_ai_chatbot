from openai import OpenAI


class ChatGPTBotAPI:
    def __init__(self, openai_api_key):
        """
        Initialize the OpenAI API with the provided API key.
        """
        self.client = OpenAI(api_key=openai_api_key)
        self.prompts = []

    def create_prompt(self, prompt):
        """
        Store the user-provided prompt.
        """
        self.prompts.append(prompt)
        return len(self.prompts) - 1

    def get_response(self, prompt_index):
        """
        Fetch the ChatGPT bot's response for the given prompt index.
        """
        if prompt_index < 0 or prompt_index >= len(self.prompts):
            raise ValueError("Invalid prompt index")

        prompt = self.prompts[prompt_index]
        try:
            response = self.client.chat.completions.create(model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7)
        except Exception as e:
            print(f"Error: {e}")
            return ""
        return response.choices[0].message.content

    def update_prompt(self, prompt_index, new_prompt):
        """
        Update the existing prompt at the given index with the new prompt.
        """
        if prompt_index < 0 or prompt_index >= len(self.prompts):
            raise ValueError("Invalid prompt index")
        self.prompts[prompt_index] = new_prompt

    def delete_prompt(self, prompt_index):
        """
        Delete the prompt at the given index.
        """
        if prompt_index < 0 or prompt_index >= len(self.prompts):
            raise ValueError("Invalid prompt index")
        self.prompts.pop(prompt_index)