# NAYA_DASHBOARD/voice/tts.py

try:
    import pyttsx3
    _engine = pyttsx3.init()
    _engine.setProperty("rate", 165)

    def speak(text: str):
        _engine.say(text)
        _engine.runAndWait()

except Exception as e:
    def speak(text: str):
        print(f"[VOICE DISABLED] {text}")
