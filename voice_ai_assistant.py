import speech_recognition as sr
import openai
import pyttsx3

openai.api_key = "the API Key"

engine = pyttsx3.init()
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("⏳ انتظر لحظة للمعايرة...")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("🎤 تكلم الآن...")
    audio = recognizer.listen(source)

try:
    user_input = recognizer.recognize_google(audio, language="ar-SA")
    print("📝 النص المحول:", user_input)

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "أنت مساعد ذكي يتحدث فقط بالعربية الفصحى وبأسلوب واضح ومختصر."},
            {"role": "user", "content": user_input}
        ],
        max_tokens=200
    )

    reply = response.choices[0].message.content.strip()
    print("🤖 رد الذكاء الاصطناعي:", reply)

    engine.say(reply)
    engine.runAndWait()

except sr.UnknownValueError:
    print("❌ ما تم التعرف على الصوت.")
except sr.RequestError as e:
    print("⚠️ مشكلة في الاتصال:", e)
