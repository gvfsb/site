from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager

app = Flask(__name__)
#URI é o caminho local no computador. 'sqlite:///site.db' == criar banco de dados no mesmo local que tá o programa.

app.config['SECRET_KEY'] = '812f368abbaa06efd8c77c63ea33b303'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'


from projetoflask import routes

