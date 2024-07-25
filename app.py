import short_url
from flask import Flask, render_template, request, abort, redirect


app = Flask(__name__)
links = {}
@app.route('/')
def index():
    global links
    url = request.args.get('url')
    if url:
        generated_link = short_url.generate_hash(url)
        links[generated_link] = url
        return render_template('index.html', generated_link=generated_link)
    return render_template('index.html')

@app.route('/<short_url_link>')
def short_url_route(short_url_link):
    global links
    long_url = links.get(short_url_link)
    print(links)
    if long_url:
        return redirect(long_url)
    return abort(404)


if __name__ == "__main__":
    app.run()