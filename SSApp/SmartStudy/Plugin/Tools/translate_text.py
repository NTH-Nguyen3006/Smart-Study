from mtranslate import translate

def translate_text(text, target_lang="en"):
    translation = translate(text, target_lang)
    return translation


