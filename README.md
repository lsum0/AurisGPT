

pro_readme = """
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

##  Introduction

The **Voice AI Assistant** is a Python-powered virtual assistant that combines real-time voice recognition with OpenAI's language model to enable natural, seamless conversations. Speak into your microphone, and the assistant will understand, think, and respond — all in real time.

This solution demonstrates how voice-enabled AI can be built using open tools and APIs, bringing intelligence to the edge of human-computer interaction.

---

##  Features

-  **Real-Time Speech-to-Text**: Capture user speech and transcribe it using Google’s Speech Recognition API.
-  **AI-Powered Understanding**: Process input and generate intelligent replies using OpenAI GPT.
-  **Text-to-Speech Synthesis**: Speak back responses using the `pyttsx3` TTS engine.
-  **Continuous Conversation Loop**: Maintain a fluid conversation until user exits.
-  **Voice-Based Termination**: Say “exit” to end the session.

---

##  Project Structure

```bash
.
├── voice_ai_assistant.py   # Main assistant script (orchestrates interaction)
└── speech_to_text.py       # Speech recognition module (microphone -> text)
