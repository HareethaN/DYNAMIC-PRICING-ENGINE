import openai
from .config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_report(summary: dict) -> str:
    prompt = f"""
    You are a pricing analyst. Analyze this data and generate:
    1) Executive summary
    2) Observations
    3) Recommendations
    Data: {summary}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']
