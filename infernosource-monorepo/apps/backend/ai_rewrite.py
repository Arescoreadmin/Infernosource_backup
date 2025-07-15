import os
from openai import OpenAI

client = OpenAI()

def rewrite_content(text):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a smart SEO rewriter."},
            {"role": "user", "content": f"Rewrite this: {text}"}
        ]
    )
    return {"original": text, "rewritten": response.choices[0].message.content}
