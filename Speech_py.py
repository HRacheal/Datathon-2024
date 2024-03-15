import speech_recognition as sr
from pydub import AudioSegment

def main():
    # Load the audio file
    sound = AudioSegment.from_mp3(r"C:\Users\Admin\Downloads\Health care.mp4")
    
    # Convert MP3 to WAV if needed
    if sound.channels != 1 or sound.frame_rate != 16000:
        sound = sound.set_frame_rate(16000).set_channels(1)
        sound.export(r"C:\Users\Admin\Downloads\Health care.wav", format="wav")
    
    # Recognize speech from the audio file
    recognizer = sr.Recognizer()
    with sr.AudioFile(r"C:\Users\Admin\Downloads\Health care.wav") as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        print("Recognized text:", text)

if __name__ == "__main__":
    main()