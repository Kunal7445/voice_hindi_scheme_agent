from gtts import gTTS
import os
import uuid

def speak(text):
    filename = f"response_{uuid.uuid4()}.mp3"
    tts = gTTS(text=text, lang="hi")
    tts.save(filename)

    # Windows-native audio playback
    os.system(f'start "" "{filename}"')
