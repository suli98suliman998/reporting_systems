from googletrans import Translator


def translate_to_arabic(text):
    translator = Translator(dest='ar')
    return translator.translate(text).text


def translate_to_english(text):
    translator = Translator(dest='en')
    return translator.translate(text).text
