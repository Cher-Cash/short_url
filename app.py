import short_url
from flask import Flask, render_template, request, abort, redirect, url_for
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
    counter = db.Column(db.Integer, default=0)


@app.route('/')
def index():
    url = request.args.get('url')
    if url:
        current_time = datetime.utcnow()
        generated_link = short_url.generate_hash(url, current_time)
        for i in range(8, 16):
            existing_url = URL.query.filter_by(short_hash=generated_link[:i]).first()
            if not existing_url:
                generated_link = generated_link[:i]
                break
        else:
            return redirect(url_for('index', url=url))
        new_url = URL(short_hash=generated_link, long_url=url, created_at=current_time)
        db.session.add(new_url)
        db.session.commit()
        return render_template('index.html', generated_link=generated_link)
    return render_template('index.html')


@app.route('/<short_url_link>')
def short_url_route(short_url_link):
    url_record = URL.query.filter_by(short_hash=short_url_link).first_or_404()

    url_record.counter += 1
    db.session.add(url_record)
    db.session.commit()
    print(f"Counter for {short_url_link}: {url_record.counter}")
    return redirect(url_record.long_url)


@app.route('/creation_time/<short_hash>')
def get_creation_time(short_hash):
    url_record = URL.query.filter_by(short_hash=short_hash).first_or_404()
    creation_time = url_record.created_at
    return f"The URL was created at: {creation_time}"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)