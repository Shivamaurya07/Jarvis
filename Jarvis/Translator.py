from deep_translator import GoogleTranslator
import pyttsx3

def translate_text(text_to_translate=None):
    if text_to_translate is None:
        # Ask for the text to translate
        text_to_translate = input("Enter the text you want to translate: ")

    # Ask for the target language
    target_language = input("Enter the language code for translation (e.g., 'en' for English): ").strip().lower()

    # Translate the text
    print("Translating...")
    try:
        translation = GoogleTranslator(source='auto', target=target_language).translate(text_to_translate)
        print("Translation:", translation)

        # Speak the translated text
        engine = pyttsx3.init()
        engine.say(translation)
        engine.runAndWait()
    except Exception as e:
        print("Unable to translate or speak:", e)

# Test the function
if __name__ == "__main__":
    translate_text()
