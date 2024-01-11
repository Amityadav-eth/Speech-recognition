import speech_recognition as sr
def audio_to_text(audio_source):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_source) as source:
        audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return "Could not process request; {0}".format(e)
def handle_file_upload():
    filename = input("Enter the path to the audio file: ")
    text = audio_to_text(filename)
    print("Transcribed text:", text)
def handle_real_time_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now:")
        audio_data = recognizer.listen(source)
    text = audio_to_text(audio_data)
    print("You said:", text)
def main():
    while True:
        choice = input("Choose an option:\n1. Upload a voice message\n2. Transcribe real-time audio\n3. Exit\nEnter your choice: ")
        if choice == "1":
            handle_file_upload()
        elif choice == "2":
            handle_real_time_audio()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
