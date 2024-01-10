import whisper
import json
import argparse

def transcribe_with_whisper(audio_file):

    model = whisper.load_model("large")

    result = model.transcribe(audio_file)

    transcriptions = result['segments']

    json_output = {
        "transcriptions": [
            {
                "start": segment['start'],
                "end": segment['end'],
                "text": segment['text']
            } for segment in transcriptions
        ]
    }
    return json_output

def main():
    parser = argparse.ArgumentParser(description="Transcribe an audio file using Whisper")
    parser.add_argument("audio_file", help="Path to the audio file to transcribe")
    args = parser.parse_args()

    # Transcribe the audio file
    json_data = transcribe_with_whisper(args.audio_file)

    # Save to JSON file
    with open('transcription.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print("Transcription completed and saved to 'transcription.json'")

if __name__ == "__main__":
    main()