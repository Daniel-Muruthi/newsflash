from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_zero_four(error):
    """
    Function To remder the 404 error passage
    """
    return render_template("fourzerofour.html"),404
