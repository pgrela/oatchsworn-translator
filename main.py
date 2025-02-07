import os.path
import xml.etree.ElementTree as ET
import deepl
import torch
from TTS.api import TTS
from pydub import AudioSegment
import json

from deepl_auth import deepl_auth_key
from reset_glossary import reset_glossary_en_pl

strings_xml_input_file = "input\\strings.xml"
map_json_file = 'input\\path-map.json'
target_language = "pl"
output_dir = f"output-{target_language}"
strings_xml_output_file = f"{output_dir}\\strings.xml"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    os.makedirs(f"{output_dir}\\raw-txt")
    os.makedirs(f"{output_dir}\\raw-wav")
    os.makedirs(f"{output_dir}\\raw")
chapter = 11

with open(map_json_file) as f_in:
    translated_resources = [entry.get("alias").replace('res/raw/', '').replace('.mp3', '') for entry in json.load(f_in) if entry.get("alias").startswith(f'res/raw/chp{chapter}')]

tts = None
translator = None
glossary = None


def translate_xml(input_file, output_file):
    global tts, translator, glossary
    # Parse XML
    tree = ET.parse(input_file)
    root = tree.getroot()

    counter = 0
    for elem in root.iter():
        if elem.text:
            name = elem.get("name")
            if name is not None and (name.startswith(f"chp{chapter}")
                                     #or name.startswith(f"pop{chapter}")
                                     #or name.startswith(f"btn{chapter}")
                                     #or name.startswith(f"btn_")
                                     or name in ["yes", "no","open_popup", "open_instructions", "new_campaign", "go_to_location", "continue_campaign"]):
                if name.startswith("chp") and name not in translated_resources:
                    continue

                txt_filename = f"{output_dir}\\raw-txt\\{name}.txt"
                wav_filename = f"{output_dir}\\raw-wav\\{name}.wav"
                mp3_filename = f"{output_dir}\\raw\\{name}.mp3"

                if os.path.isfile(txt_filename):
                    with open(txt_filename, 'r', encoding="utf-8") as file:
                        translated_text = file.read()
                else:
                    print(f"Translating text '{name}'.")
                    if translator is None:
                        translator = deepl.Translator(deepl_auth_key)
                        glossary = reset_glossary_en_pl(translator, "glossary.csv")
                    translated_text = str(translator.translate_text(elem.text, source_lang="EN", target_lang=target_language.upper(), glossary=glossary))
                    with open(txt_filename, "w", encoding="utf-8") as text_file:
                        print(translated_text, file=text_file)
                if name.startswith("chp"):
                    if not os.path.isfile(wav_filename):
                        print(f"Reading text '{name}'.")
                        text_to_read = translated_text.replace('"','')
                        if tts is None:
                            tts = get_tts()
                        tts.tts_to_file(text=text_to_read, speed=2, emotion="Happy", speaker_wav="speaker.wav", language=target_language, file_path=wav_filename)
                    if not os.path.isfile(mp3_filename):
                        AudioSegment.from_wav(wav_filename).export(mp3_filename, format="mp3")
                elem.text = translated_text.strip()
                counter += 1
    print(counter)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

def get_tts():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print("Usings {}".format(device))

    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v1.1").to(device)
    return tts

if __name__ == "__main__":
    translate_xml(strings_xml_input_file, strings_xml_output_file)
