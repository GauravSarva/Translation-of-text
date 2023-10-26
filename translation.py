from translate import Translator

input_text = input("Enter the text for translating it to different languages:\n\t")

language_selection = input("Enter the language for translation process: ")

translator = Translator(from_lang = "english", to_lang = language_selection)

if language_selection in ["sanskrit", "hindi", "marathi", "english", "french", "german", "spanish", "italian", "portuguese", "russian", "japanese", "korean", "chinese", "turkish", "vietnamese"]:
  print(translator.translate(input_text))
else:
  print("Invalid language code")
