# Speech Recognition Program

## Description
This program utilizes the `speech_recognition` library to convert spoken audio into text. It captures audio from the microphone and processes it using Google Speech Recognition. The converted text can be manipulated for various text-processing tasks such as converting to lowercase and splitting into words.

## Features
- Captures audio using a microphone
- Converts speech to text using Google Speech Recognition
- Handles errors such as unrecognized speech and API request failures
- Processes the recognized text for further analysis

## How It Works
1. The program initializes a speech recognizer.
2. It records audio from the user's microphone.
3. The recorded audio is sent to Google Speech Recognition for transcription.
4. If successful, the transcribed text is displayed.
5. The text is further processed by converting it to lowercase and splitting it into words.
6. If speech is not recognized, an error message is displayed.

## Example Output
```
Speak something...
You said: Hello World
Lowercase text: hello world
Words: ['hello', 'world']
```

## Installation & Usage
### Prerequisites
- Python 3
- Install required library:
  ```sh
  pip install SpeechRecognition
  ```

### Running the Script
Save the script as `speech_recognition.py` and run:
```sh
python speech_recognition.py
```

## Notes
- Requires an internet connection for Google Speech Recognition.
- Ensure your microphone is enabled and working.
- Background noise may affect recognition accuracy.

## License
This project is open-source and free to use for learning and experimentation.

