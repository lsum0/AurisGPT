


<h1 align="center">🎙️ Voice AI Assistant</h1>
<p align="center">
  <i>Natural Language Conversational Assistant with Real-Time Speech Recognition and AI Response</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-active-brightgreen" alt="Project Status">
  <img src="https://img.shields.io/badge/python-3.7%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="License">
</p>

---

## 1.  Introduction

The **Voice AI Assistant** is a Python-powered virtual assistant that combines real-time voice recognition with OpenAI's language model to enable natural, seamless conversations. Speak into your microphone, and the assistant will understand, think, and respond — all in real time.

This solution demonstrates how voice-enabled AI can be built using open tools and APIs, bringing intelligence to the edge of human-computer interaction.



![](PIc-AI.png)
---

##  2. Features

-  **Real-Time Speech-to-Text**: Capture user speech and transcribe it using Google’s Speech Recognition API.
-  **AI-Powered Understanding**: Process input and generate intelligent replies using OpenAI GPT.
-  **Text-to-Speech Synthesis**: Speak back responses using the `pyttsx3` TTS engine.
-  **Continuous Conversation Loop**: Maintain a fluid conversation until user exits.
-  **Voice-Based Termination**: Say “exit” to end the session.

---

##  3. Project Structure

```bash
.
├── voice_ai_assistant.py   # Main assistant script (orchestrates interaction)
└── speech_to_text.py       # Speech recognition module (microphone -> text)
```



## 4. Installation :
 
 Ensure Python 3.7+ is installed. Then, install the dependencies: 
 - pip install openai
 - pip install pyttsx3
 - pip install SpeechRecognition


##  5. Configuration :

Before running the assistant, set your OpenAI API key inside voice_ai_assistant.py:

openai.api_key = "my_key_in_API"

## 6. Useg :

python3 (name the file).py
for Example : 
python3 voice_ai_assistant.py then Run 
now Talking with AI .. , To Stop The Assistant, Simply Say ( Exit) .

##  7. Example Flow : 

User: "What's artificial intelligence?"
Assistant: (Processes via GPT) → "Artificial intelligence is the simulation of human intelligence in machines..."
Assistant replies out loud.
![](another-pic.png)

## Flowchart : 
![](flowchartAI.png) 

The flowchart outlines a real-time Voice AI Assistant that integrates speech recognition, natural language processing, and text-to-speech. The system begins by prompting the user to speak, transcribes the input using Google’s API, and checks for an exit command. If not exiting, the input is processed by OpenAI’s GPT model, and the response is spoken aloud using pyttsx3. This loop continues until the user says “exit,” enabling natural, continuous interaction

 
