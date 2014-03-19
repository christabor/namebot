from wtforms import Form, TextAreaField, TextField, PasswordField, validators


class NameGeneratorForm(Form):
    field1 = TextField('Some descriptive word', [validators.Length(min=4, max=25)])
    field2 = TextField('another word', [validators.Length(min=4, max=25)])
    field3 = TextField('maybe some common jargon for your field', [validators.Length(min=4, max=25)])
    field4 = TextField('more phrases or jargon', [validators.Length(min=4, max=25)])
    field5 = TextField('another word', [validators.Length(min=4, max=25)])
    field6 = TextField('a final word', [validators.Length(min=4, max=25)])
    textarea = TextAreaField('Or just make a list...')
