from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap


def create_app(config_name):
    """
    Initializing the app
    Function that takes configuration setting key as an argument
    Args:
        config_name: name of the configuration used
    """
    app = Flask(__name__)

    #initializing flask extention
    bootstrap = Bootstrap (app)

    #creating app configurations
    app.config.from_object(config_options[config_name])

    #registering the Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting up the request configurations
    from .requests import configure_request
    configure_request(app)

    return app