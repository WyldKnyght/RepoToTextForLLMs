# utils/load_binary_extensions.py
def load_binary_extensions(filename="config/binary_extensions.txt"):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]
