import openai

def generate_code(feature_description):
    prompt = f"Generate Python code to implement the following feature: {feature_description}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']