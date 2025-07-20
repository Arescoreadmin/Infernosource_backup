# backend/ai_rewrite.py

import os

# If you use OpenAI, install openai: pip install openai
# import openai

def rewrite_with_ai(text: str, persona: str = "default") -> str:
    """
    Dummy AI rewriting logic (replace with actual API call).
    """
    # For demonstration: prepend persona and "rewritten"
    return f"[Persona: {persona}] Rewritten: {text}"

# Example OpenAI (uncomment and configure if using)
# def rewrite_with_openai(text: str, persona: str = "default") -> str:
#     openai.api_key = os.getenv("OPENAI_API_KEY")
#     prompt = f"Rewrite the following text in the tone/persona of '{persona}':\n\n{text}"
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response.choices[0].message['content'].strip()

if __name__ == "__main__":
    sample_text = "This is the original input."
    persona = "edgy marketer"
    rewritten = rewrite_with_ai(sample_text, persona)
    print("Rewritten:", rewritten)
