from pydoc import text
from tkinter.tix import TEXT
from unittest.mock import DEFAULT
import deepl
import os
#auth_key=6b607203-09ea-5614-7cc9-90eb69eb56e1
# Create a Translator object providing your DeepL API authentication key.
# To avoid writing your key in source code, you can set it in an environment
# variable DEEPL_AUTH_KEY, then read the variable in your Python code:
#files=[
#  ('file',('test.txt',open('D:/Documents/test.txt','rb'),'text/plain'))
#]
translator = deepl.Translator('51593884-62ed-5ce4-4a8e-9811fed3be82:fx')#,server_url='http://api.deepl.comv2/v2/translate?')

# Translate text into a target language, in this case, French
result = translator.translate_text("<p A Scottish Adventurer of the Eighteenth Century</span></p>", target_lang="zh",tag_handling= "xml")
#result = translator.translate_document(input_document=files,output_document=files,target_lang="zh")

print(result)  # "Bonjour, le monde !"

# Translate a formal document from English to German 
try:
    translator.translate_document_from_filepath(
        'D:/Documents/作业/test.txt',
        'D:/Documents/作业/fastapi/test2.doc',
        target_lang="zh",

        #formality="less"
    )
except deepl.DocumentTranslationException as error:
    # If an error occurs during translate_document_from_filepath() or
    # translate_document() and after the document was already uploaded, a 
    # DocumentTranslationException is raised. The document_handle property
    # contains the document handle to later retrieve the document or contact
    # DeepL support.
    doc_id = error.document_handle.id
    doc_key = error.document_handle.key
    print(f"Error after uploading document ${error}, id: ${doc_id} key: ${doc_key}")
except deepl.DeepLException as error:
    # Errors during upload raise a DeepLException
    print(error)
##import requests
##
#url = "http://api-free.deepl.com/v2/document"
#
#payload={'auth_key': '51593884-62ed-5ce4-4a8e-9811fed3be82:fx',
#'target_lang': 'zh'}
#files=[
#  ('file',('test.txt',open('D:/Documents/test.txt','rb'),'text/plain'))
#]
#headers = {}
#
#response = requests.request("POST", url, headers=headers, data=payload, files=files)
#
#print(response.text)

# Check account usage
usage = translator.get_usage()
if usage.character.limit_exceeded:
    print("Character limit exceeded.")
else:
    print(f"Character usage: {usage.character.count} of {usage.character.limit}")

# translator html
translator.translate_text()