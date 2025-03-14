import openai

OPENAI_API_KEY = "your-api-key"

def correct_query_with_llm(query):
    prompt = f"""The user said: "{query}". This is a spoken search query for YouTube. Fix any errors and make it a well-structured search query."""
    
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are an AI that corrects spoken YouTube search queries."},
                  {"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"].strip()
