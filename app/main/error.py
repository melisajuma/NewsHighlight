from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    function that will bring forth the 404 error page
    '''
    return render_template('fourOwfour.html'), 404