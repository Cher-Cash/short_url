import short_url
from flask import Flask, render_template, request, abort, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shorturl.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class URL(db.Model):
    __tablename__ = 'urls'
    short_hash = db.Column(db.String, primary_key=True)
    long_url = db.Column(db.String, nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)


class URLCounter(db.Model):
    __tablename__ = 'url_counters'
    short_hash = db.Column(db.String, db.ForeignKey('urls.short_hash'), primary_key=True)
    counter = db.Column(db.Integer, default=0)


@app.route('/')
def index():
    url = request.args.get('url')
    if url:
        generated_link = short_url.generate_hash(url)
        new_url = URL(short_hash=generated_link, long_url=url)
        db.session.add(new_url)
        db.session.commit()
        new_counter = URLCounter(short_hash=generated_link, counter=0)
        db.session.add(new_counter)
        db.session.commit()

        return render_template('index.html', generated_link=generated_link)
    return render_template('index.html')


@app.route('/<short_url_link>')
def short_url_route(short_url_link):
    url_record = URL.query.filter_by(short_hash=short_url_link).first()
    if url_record:
        counter_record = URLCounter.query.filter_by(short_hash=short_url_link).first()
        counter_record.counter += 1
        db.session.commit()
        print(f"Counter for {short_url_link}: {counter_record.counter}")

        return redirect(url_record.long_url)
    return abort(404)


@app.route('/creation_time/<short_hash>')
def get_creation_time(short_hash):
    url_record = URL.query.filter_by(short_hash=short_hash).first()
    if url_record:
        creation_time = url_record.created_at
        return f"The URL was created at: {creation_time}"
    return "URL not found", 404


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)