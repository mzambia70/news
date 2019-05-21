from flask import Blueprint
main = Blueprint('main',__name__) #initialize the class by crearint a variable 'main'
from . import views, error