from flask import Blueprint, render_template

loginmod = Blueprint('login', __name__, template_folder='templates')

@loginmod.route('/login')
def loginIndex():
    return render_template('login.html')