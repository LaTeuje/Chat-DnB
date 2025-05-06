import openai

# Remplace par ta propre clé d'API OpenAI
openai.api_key = "sk-..."

def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Tu es un expert de la Drum and Bass. Tu aides à découvrir les sous-genres, artistes et tracks."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]

# Exemple d'utilisation
question = input("Pose une question sur la Drum and Bass : ")
print(ask_gpt(question))
