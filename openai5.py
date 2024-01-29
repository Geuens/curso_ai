
from openai import OpenAI
from dotenv import load_dotenv
import os
# Cargar variables de entorno
load_dotenv()
# Configurar el motor de OpenAI
engine ="gpt-3.5-turbo"
client = OpenAI(api_key="-")

def get_completion(prompt):
    completion = client.chat.completions.create(
    model=engine,
    messages=[
    {"role": "user", "content": f"{prompt}"}
    ]
    )
    return completion
texto = f"""
<alumno> Enséñame sobre paciencia
<profesor> La paciencia, bro, es aguantarse la movida sin flipar. Es como, "tranqui,
colega, no pierdas la cabeza". \
En el rollo diario, cuando todo va fatal, la paciencia es esa onda que te mantiene
chido, sin volverte loco. No es solo \
esperar, es dominar el juego, ser el crack que controla el rollo, no el que se va de
la olla por cualquier cosa. La paciencia es poder, tío.
<alumno> Enséñame sobre la inteligencia artificial
"""
prompt = f"""
Te proporcionaré un texto en comillas triples
Tu tarea es contestar en un estilo consecuente:
\"\"\"{texto}\"\"\"
"""
response = get_completion(prompt)
print("Respuesta para texto:")
print(response)