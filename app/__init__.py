from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = '389100b3df9843'
app.config['MAIL_PASSWORD'] = '15bbb6a761700a'

mail = Mail(app)
from app import views