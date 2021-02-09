# bitcoin mining is process guessing a nonce (gen hash with first X number of zeros)
from hashlib import sha256
MAX_NONCE_VALUE = 100000000000
text = "Minh"


def SHA256(text):
    return sha256(text.encode('ascii')).hexdigest()


def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range(MAX_NONCE_VALUE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Bitcoin mined for nonce value of {nonce}")
            return new_hash


if __name__ == '__main__':
    print(SHA256("Minh"))
    new_hash = mine(2, "coin", SHA256("Minh"), 5)
    print(new_hash)