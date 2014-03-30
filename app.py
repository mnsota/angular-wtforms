from __future__ import with_statement

from flask import (Flask, session, redirect, url_for, abort,
                   render_template, flash, request, jsonify)

from flask_wtf import Form

from wtforms import BooleanField, TextField, PasswordField, validators

import json

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.debug=True

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])

    def __init__(self, *args, **kwargs):
      Form.__init__(self, *args, **kwargs)



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form, csrf_enabled=False)
    if request.method == 'POST':
      if form.validate_on_submit():
        return json.dumps(form, default=lambda o: o.__dict__, sort_keys=True, indent=4), 200
      else:
        return json.dumps(form, default=lambda o: o.__dict__, sort_keys=True, indent=4), 400
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run()