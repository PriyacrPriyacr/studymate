import requests

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"

# No authorization header needed for public access (limited rate)
headers = {
    "Content-Type": "application/json"
}

def generate_answer(context, question):
    prompt = f"Answer the question based on the context.\nContext: {context}\nQuestion: {question}"
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        return f"❌ Request failed with status code {response.status_code}: {response.text}"

    try:
        result = response.json()
        print("Debug: raw response:", result)  # Debug output
        # The response for T5 is usually a dict with 'generated_text'
        # Or sometimes a list with one dict — check and adapt accordingly
        if isinstance(result, list):
            return result[0].get("generated_text", "No generated_text found")
        elif isinstance(result, dict):
            return result.get("generated_text", "No generated_text found")
        else:
            return str(result)
    except Exception as e:
        return f"❌ Failed to parse response: {e}"

# Test run
if __name__ == "__main__":
    context = "Python is a popular programming language."
    question = "What is Python?"
    answer = generate_answer(context, question)
    print("Answer:", answer)
