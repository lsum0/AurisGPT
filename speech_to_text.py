import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("⏳ انتظر لحظة لتحسين الصوت...")
    recognizer.adjust_for_ambient_noise(source, duration=1)  # تحسين الجودة
    print("🎤 تكلم الآن...")
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ar-SA")
        print("📝 النص المحول:", text)
    except sr.UnknownValueError:
        print("❌ ما تم التعرف على الصوت.")
    except sr.RequestError as e:
        print("⚠️ مشكلة في الاتصال بخدمة Google:", e)

