def text_to_binary(text):
    if isinstance(text, str):
        return ''.join(format(ord(char), '08b') for char in text)
    else:  # bytes
        return ''.join(format(byte, '08b') for byte in text)

def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join([chr(int(c, 2)) for c in chars])