from flask import Flask
from views import views

app = Flask(__name__)
app.config['SECRET_KEY'] = 'soamcwbbx'

app.register_blueprint(views, url_prefix='/')
app.run(debug=False)

