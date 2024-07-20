import hashlib
from datetime import datetime

class ShortUrl:

    def __init__(self, long_url, explanation):
        self.explanation = explanation
        self.long_url = long_url
        self.creation_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    def write_to_db(self):
        return


    def generate_hash(self):
        hash_object = hashlib.sha256()
        hash_object.update(self.long_url.encode('utf-8'))
        hash_hex = hash_object.hexdigest()
        short_hash = hash_hex[:8]
        return short_hash

def app(long_url: str):
    url = ShortUrl(long_url, explanation='')
    hash_ = url.generate_hash()
    #url.write_to_db(short_url)
    print(hash_)


if __name__ == "__main__":
    app("https://example.com/some/very/long/url/that/needs/to/be/shortened")
