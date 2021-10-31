#encode a string to base64
import base64
def encode(string):
    return base64.b64encode(string.encode('utf-8'))

print(encode('hello world'))

def decode(string):
    return base64.b64decode(string).decode('utf-8')

print(decode('aGVsbG8gd29ybGQ='))