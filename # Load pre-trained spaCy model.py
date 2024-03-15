# Load pre-trained spaCy model
nlp = spacy.load("en_core_web_sm")

# Sample medical text
medical_text = "Patient presents with fever, cough, and shortness of breath."

# Process the text
doc = nlp(medical_text)

# Extract named entities
for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")


# Example: Using Mozilla DeepSpeech for STT
import deepspeech

# Load pre-trained DeepSpeech model
model_path = "path/to/deepspeech_model.pb"
ds = deepspeech.Model(model_path)

# Sample audio file
audio_file = "path/to/medical_audio.wav"
# Transcribe audio
with open(audio_file, "rb") as audio:
    audio_data = audio.read()
    transcription = ds.stt(audio_data)

print(f"Transcription: {transcription}")