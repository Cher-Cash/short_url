from flask import Flask, render_template, request, abort, redirect
from short_url import ShortUrl

app = Flask(__name__)
links = {}
@app.route('/')
def index():
    global links
    url = request.args.get('url')
    if url:
        short_url_ = ShortUrl(url)
        generated_link = short_url_.generate_hash()
        links[generated_link] = url
        return render_template('index.html', generated_link=generated_link)
    return render_template('index.html')

@app.route('/<short_url_link>')
def short_url_route(short_url_link):
    global links
    long_url = links.get(short_url_link)
    print(links)
    print(long_url)
    print(short_url_link)
    if long_url:
        return redirect(long_url)
    return abort(404)


if __name__ == "__main__":
    app.run()