def main():
    print(" Language Translator Tool")
    print("Supported languages: en, es, fr, am, hi, de, ar, zh, ru, etc.")
    
    source = input("From language (e.g. en): ")
    target = input("To language (e.g. am): ")
    text = input("Enter text to translate: ")

    try:
        translated = GoogleTranslator(source=source, target=target).translate(text)
        print(f"\n Translated ({source} → {target}): {translated}")
    except Exception as e:
        print(f" Error: {e}")

if name == "main":
    main()