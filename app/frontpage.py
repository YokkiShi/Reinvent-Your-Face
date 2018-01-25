from flask import render_template, redirect, url_for
from app import webapp, index

@webapp.route('/')
def frontpage():

    if index.get_username() is not None and index.get_auth() is True:
        username_session = index.get_username()
        #session['authenticated'] = True
        return redirect(url_for('index', username = username_session))
    else:
        return render_template('frontpage.html')
