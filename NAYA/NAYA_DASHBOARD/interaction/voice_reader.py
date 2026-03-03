
from NAYA_DASHBOARD.views.system_view import render_system_view
from NAYA_INTERFACE.transport.voice_output import speak

def speak_system_state() -> None:
    state = render_system_view()
    speak(f"État système actuel : {state}")
