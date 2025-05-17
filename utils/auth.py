from authlib.integrations.flask_client import OAuth
from flask import url_for, redirect, session
import os

oauth = OAuth()

google = oauth.register(
    name='google',
    client_id='236254793539-g12v8kin4omrj967359rf85rrg2j2anq.apps.googleusercontent.com',
    client_secret='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',
    access_token_url='https://oauth2.googleapis.com/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    client_kwargs={
        'scope': 'openid email profile',
        # Note: do NOT set redirect_uri here, set it dynamically below
    }
)

def login():
    # Use url_for with _external=True to get full redirect URI
    redirect_uri = url_for('auth', _external=True)  # e.g. http://127.0.0.1:5000/auth
    return google.authorize_redirect(redirect_uri)

def authorize():
    token = google.authorize_access_token()
    user = google.parse_id_token(token)
    session['user'] = user
    return redirect('/')
