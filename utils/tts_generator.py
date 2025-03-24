from gtts import gTTS
import os

def generate_hindi_speech(text, output_file="output/sentiment_summary.mp3"):
    try:
        print(f"🔹 Generating speech for text: {text[:50]}...")  # Debug: Print first 50 chars
        print(f"🔹 Output file path: {output_file}")  # Debug: Print file path
        
        # Generate and save speech file
        tts = gTTS(text=text, lang="hi")
        tts.save(output_file)  

        # Verify if the file was created successfully
        if os.path.isfile(output_file):
            print(f"✅ Speech successfully saved: {output_file}")
            return True  # Indicating success

        print(f"❌ Error: File not created!")
        return False  # Indicating failure

    except Exception as e:
        print(f"❌ Error generating speech: {e}")
        return False  # Indicating failure
