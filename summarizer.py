# summarizer.py
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary(df):
    titles = df["title"].tolist()
    preview = "\n".join(titles[:5])

    prompt = f"""Summarize the key trends based on the following news titles:

{preview}

What themes or patterns do you notice?"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    summary = response.choices[0].message.content.strip()
    with open("outputs/summary.txt", "w") as f:
        f.write(summary)
    return summary
