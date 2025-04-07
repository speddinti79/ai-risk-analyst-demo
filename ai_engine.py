import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_insight(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response['choices'][0]['message']['content']
