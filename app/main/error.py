from flask import render_template
from . import main #importing the blueprint instance 'main' and use 2 define decorators

@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourowfour.html'),404