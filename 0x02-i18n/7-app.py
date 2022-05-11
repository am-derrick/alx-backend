#!/usr/bin/env python3
"""Route module for App"""
from flask import Flask, render_template
from flask_babel import Babel
from typing import Union
from os import getenv
from pytz import timezone
import pytz.exceptions


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)

class Config(object):
    """Configures available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE ="en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('7-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """GET /
    Return:
    - 7-index.html
    """
    return render_template('7-index.html')


@babel.localeselector
def get_locale() -> str:
    """determines best match for supported languages"""
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
        
    elif g.user and g.user.get('locale')\
         and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    else:
        return request.accept_languages.best_match(Config['LANGUAGES'])

def get_user() -> Union[dict, None]:
    """Returns user dict if ID is found"""
    if request.args.get("login_as"):
        user = int(request.args.get('login_as'))
        if user in users:
            return users.get(user)

    else:
        return None


@app.before_request
def before_request():
    """Finds user and sets global on flask.g.user"""
    g.user = get_user()


@babel.timeselector
def get_timezone() -> Optional[str]:
    """determines best match supported timezones"""
    if request.args.get('timezone'):
        timezone = request.args.get('timezone')
        try:
            return timezone(timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None

    elif g.user and g.user.get('timezone'):
        try:
            return timezone(g.user.get('timezone')).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None

    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
