import hashlib


def generate_hash(long_url: str):
    hash_object = hashlib.md5()
    hash_object.update(long_url.encode('utf-8'))
    hash_hex = hash_object.hexdigest()
    ascii_hash = [0] * 8
    for index_, i in enumerate(range(0, len(hash_hex), 4)):
        ascii_hash[index_] = process_byte(hash_hex[i:i + 4])
    hash_ = ''.join(ascii_hash)
    return hash_


def process_byte(num_line):
    num = int(num_line, 16)
    #гарантия что ascii_num будет в пределах 48-105 (диапазон который включает все цифры и многие буквы)
    ascii_num = (num % 58) + 48
    if (ascii_num >= 58 and ascii_num <= 64) or (ascii_num >= 91 and ascii_num <= 96):
        ascii_char = '_'
    else:
        ascii_char = chr(ascii_num)
    return ascii_char



def main(long_url: str):
    hash_ = generate_hash(long_url)
    print(hash_)
    return hash_

if __name__ == "__main__":
    main("https://example.com/some/very/long/url/that/needs/to/be/shortened")


