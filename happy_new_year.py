from gtts import gTTS
import os

def create_audio_message():
    # The message to convert to audio
    message = "Happy New Year 2025 from Sherri Killough, I hope you have a great year and that all your dreams come true!"
    
    # Language for the speech
    language = 'en'
    
    # Create a gTTS object
    tts = gTTS(text=message, lang=language, slow=False)
    
    # Save the audio file
    tts.save("happy_new_year_2025.mp3")
    
    # Play the audio file
    os.system("afplay happy_new_year_2025.mp3")

if __name__ == "__main__":
    create_audio_message()