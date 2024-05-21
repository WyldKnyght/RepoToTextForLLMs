# utils/process_file.py
import os
from tqdm import tqdm
from utils.decode_content import decode_content

def process_file(content, path, binary_extensions):
    file_info = f"File: {path}/{content.name}\n"
    
    if any(content.name.endswith(ext) for ext in binary_extensions):
        return f"{file_info}Content: Skipped binary file\n\n"
    
    if content.encoding is None or content.encoding == 'none':
        return f"{file_info}Content: Skipped due to missing encoding\n\n"
    
    decoded_content, used_encoding = decode_content(content)
    if not decoded_content:
        return f"{file_info}Content: Skipped due to unsupported encoding\n\n"
    
    return f"{file_info}Content ({used_encoding} Decoded):\n{decoded_content}\n\n"
