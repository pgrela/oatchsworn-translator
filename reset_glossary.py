from deepl import Translator


def reset_glossary_en_pl(translator: Translator, csv_file_name, glossary_name="oathsworn"):
    glossaries = translator.list_glossaries()
    glossary = next((g for g in glossaries if g.name == glossary_name), None)
    if glossary is not None:
        translator.delete_glossary(glossary)
    with open(csv_file_name, 'r', encoding="utf-8") as f:
        read = f.read()
        translator.create_glossary_from_csv(glossary_name, "en", "pl", read)
    glossaries = translator.list_glossaries()
    glossary = next((g for g in glossaries if g.name == glossary_name), None)
    if glossary is None:
        quit(1024)
    return glossary
