import os
from google.cloud import translate_v2 as translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'yourProteanKeywordFile'



translate_client = translate.Client()
target = 'tr'#Target Language 'tr' for Turkish

original_text="theFiletoTranslate"
target_text="translatedfile"
with open(original_text,"r",encoding="utf-8") as f:
    text = f.readlines()
with open(target_text,"w",encoding="utf-8") as o:
    for i in range(0,26):
        o.write(text[i])
    for i in range(26,len(text)):
        a=text[i]
        a.strip("\n")
        b=a.split(",,0,0,0,,")
        output=translate_client.translate(b[1], target_language=target)
        final = b[0] + ",,0,0,0,," + output["translatedText"] + "\n"
        o.write(final)

