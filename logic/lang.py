import importlib

class Translator:
    def __init__(self, locale="en"):
        self.set_language(locale)

    def set_language(self, lang_code):
        try:
            lang_module = importlib.import_module(f"locales.{lang_code}")
            self.translations = lang_module.translations
        except (ImportError, AttributeError):
            self.translations = {}

    def t(self, key):
        return self.translations.get(key, key)