from pathlib import Path
import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = openai.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="ideología: la creencia errónea de que tus errores no son creencias ni errores."
)
response.stream_to_file(speech_file_path)