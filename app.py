from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku

app = Flask(__name__)
app.config['SQLACHEMY_DATABASE_URI'] = 'postgres://wizjkjznpuirhk:0834c14ce2ec097307293f65d5e9467624aaf5d924750b43745793e3f9988aa7@ec2-54-243-61-194.compute-1.amazonaws.com:5432/denuiu1akum3hh'
heroku = heroku(app)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Interger, primary_key = True)
    email = db.Column(db.String(120), unique = True)

    def __init__(self, email):
        self.email = email
    
    def __repr__(self):
        return '<E-mail %r>' % self.email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show')
def show():
    return render_template('show.html')

@app.route('/collect')
def collect():
    return render_template('collect.html')

@app.route('/prereg', methods=['POST'])
def prereg():
    email = None
    if request.method == 'POST':
        email = request.form['email']
        reg = User(email)
        sb.session.add(reg)
        db.session.commit()
        return render_template('success.html')
    return render_template('collect.hmtl')

@app.route('/return_emails', methods=['GET'])
def return_emails():
    all_emails = db.session.query(User.email).all()
    return jsonify(all_emails)


if __name__ == '__main__':
    app.debug = True
    app.run()