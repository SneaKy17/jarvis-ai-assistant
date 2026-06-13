import speech_recognition as sr
from gtts import gTTS
from config import VOICE_RATE, VOICE_VOLUME, SPEECH_TIMEOUT, SPEECH_LANGUAGE
import time
import os
import subprocess

class InputHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
    
    def listen_to_voice(self):
        try:
            with sr.Microphone() as source:
                print("🎤 Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(source, timeout=SPEECH_TIMEOUT)
            
            text = self.recognizer.recognize_google(audio, language=SPEECH_LANGUAGE)
            print(f"📝 You said: {text}")
            return text
        except sr.UnknownValueError:
            error_msg = "I'm afraid I didn't quite catch that, Sir."
            self.speak(error_msg)
            return None
        except sr.RequestError as e:
            error_msg = f"Network error: {e}"
            self.speak(error_msg)
            return None
        except sr.Timeout:
            error_msg = "I'm waiting for your command, Sir."
            self.speak(error_msg)
            return None
    
    def get_text_input(self):
        try:
            user_input = input("\n📝 You: ").strip()
            if user_input:
                return user_input
            return None
        except KeyboardInterrupt:
            print("\n👋 Shutting down JARVIS...")
            return None
    
    def speak(self, text):
        try:
            print(f"\n🤖 JARVIS: {text}\n")
            
            # Generate speech with gTTS
            tts = gTTS(text=text, lang=SPEECH_LANGUAGE, slow=False)
            tts.save("jarvis_response.mp3")
            
            # Play with Windows built-in player
            mp3_path = os.path.abspath("jarvis_response.mp3")
            os.startfile(mp3_path, "play")
            
            # Wait for playback
            time.sleep(3)
            
            # Clean up
            try:
                if os.path.exists("jarvis_response.mp3"):
                    os.remove("jarvis_response.mp3")
            except:
                pass
                
        except Exception as e:
            print(f"Error in speech: {e}")
    
    def listen_for_command(self):
        print("\n🎙️ Choose input mode:")
        print("1. Voice (🎤)")
        print("2. Text (⌨️)")
        
        choice = input("Enter choice (1 or 2): ").strip()
        
        if choice == "1":
            return self.listen_to_voice()
        elif choice == "2":
            return self.get_text_input()
        else:
            print("Invalid choice. Using text mode.")
            return self.get_text_input()