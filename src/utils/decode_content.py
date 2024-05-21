# utils/decode_content.py
import codecs

def decode_content(content):
    encodings = ['utf-8', 'latin-1']
    for encoding in encodings:
        try:
            return codecs.decode(content.decoded_content, encoding), encoding
        except UnicodeDecodeError:
            continue
    return None, None
