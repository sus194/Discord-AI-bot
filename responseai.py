import os
import openai
openai.api_key = os.environ['AI_API_KEY']

#openai response to a prompt
def get_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0,
    )
    message = response["choices"][0]["text"].strip()
    return message