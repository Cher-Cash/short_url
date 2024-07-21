import hashlib
from datetime import datetime

class ShortUrl:

    def __init__(self, long_url):
        self.long_url = long_url
        self.creation_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.hash = None


    def generate_hash(self):
        hash_object = hashlib.md5()
        hash_object.update(self.long_url.encode('utf-8'))
        hash_hex = hash_object.hexdigest()
        ascii_hash = []
        for i in range(0, len(hash_hex),4):
            num = hash_hex[i:i+4]
            ascii_hash.append(ShortUrl.process_byte(num))
        self.hash = ''.join(ascii_hash)
        return self.hash

#91-96, 58-64 _

    @staticmethod
    def process_byte(num_line):
        num = int(num_line, 16)
        #гарантия что ascii_num будет в пределах 48-105 (диапазон который включает все цифры и многие буквы)
        ascii_num = (num % 58) + 48
        invalid_chars = set(range(58, 65)) | set(range(91, 97))
        if ascii_num in invalid_chars:
            ascii_char = '_'
        else:
            ascii_char = chr(ascii_num)
        return ascii_char


def main(long_url: str):
    url = ShortUrl(long_url)
    hash_ = url.generate_hash()
    print(hash_)

if __name__ == "__main__":
    main("https://example.com/some/very/long/url/that/needs/to/be/shortened")


