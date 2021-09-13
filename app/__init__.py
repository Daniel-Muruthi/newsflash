from app.config import DevConfig
from flask import Flask
from flask_bootstrap import Bootstrap
from app.config import DevConfig
# from . config import config_options



app = Flask(__name__,instance_relative_config = True)

#Creating the app configurations
app.config.from_object(DevConfig)

app.config.from_pyfile('config.py')

bootstrap = Bootstrap(app)




    

# def create_news_app(config_name):


    #Initializing flask extensions
    # bootstrap.init_app(app)

    #Will add the views and forms

    # from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    #setting config

    # from .requests import configure_request
    # configure_request(app)

    # return app

from app import views
# from app import error