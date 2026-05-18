import random
import string
#creates unique alphanumeric short code for the url
def generate_short_code(length=5):
    characters = string.ascii_letters + string.digits

    return ''.join(
        random.choice(characters)
        for _ in range(length)
    )