import random
import string


def generate_id():
    """Generate unique id for the order"""

    alphabet = string.ascii_letters.upper() + string.digits
    order_id = ''.join(random.choice(alphabet) for i in range(8))
    return order_id
