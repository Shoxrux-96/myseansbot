import requests

def ask_ai(prompt):
    API_URL = "https://api-inference.huggingface.co/models/bigscience/bloomz-560m"
    headers = {"Authorization": "Bearer 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"}

    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)

    try:
        return response.json()[0]['generated_text']
    except Exception as e:
        print("Xatolik:", e)
        print("Serverdan javob:", response.text)
        return "AI hozircha javob bera olmayapti."
