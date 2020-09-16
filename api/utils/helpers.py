import os
import base64


def generate_id():
    character_id = base64.b64encode(os.urandom(6)).decode('ascii')
    return character_id.upper()
