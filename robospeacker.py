# Import the Windows COM (Component Object Model) client library
import win32com.client as wincom

# Import time module for delay
import time

# Create a speech engine object using the Windows built-in SAPI (Speech API)
say = wincom.Dispatch("SAPI.SpVoice")

# Start an infinite loop
while True:
    # Ask user for input
    text = input("Enter your text (or 'q' to quit): ")

    # If user types 'q', break the loop and exit
    if text.lower() == 'q':
        break

    # say the entered text aloud
    say.Speak(text)

    # Wait 1 second before the next line
    time.sleep(1)

    # Speak this predefined line after the delay
    say.Speak("This text is read after 1 second")
