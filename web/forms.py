from wtforms import Form, BooleanField, TextField, PasswordField, validators


class NameGeneratorForm(Form):
    field1 = TextField('Field 1', [validators.Length(min=4, max=25)])
    field2 = TextField('Field 2', [validators.Length(min=4, max=25)])
    field3 = TextField('Field 3', [validators.Length(min=4, max=25)])
    field4 = TextField('Field 4', [validators.Length(min=4, max=25)])
    field5 = TextField('Field 5', [validators.Length(min=4, max=25)])
