# -*- coding: utf-8 -*-
# quiz-orm/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, HiddenField, FieldList
from wtforms import SelectField, FormField, BooleanField
from wtforms.validators import Required

blad1 = 'To pole jest wymagane'


class UczenForm(FlaskForm):
    id = HiddenField('Uczen id')
    klasa = HiddenField('Klasa id')
    uczen = StringField('Uczeń:',
                             validators=[Required(message=blad1)],
                             render_kw={'class':'form-control'})
    odpok = BooleanField('Poprawna:')
