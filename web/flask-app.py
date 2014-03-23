import app_settings
if app_settings.CACHE_ENABLED:
    # See http://flask.pocoo.org/docs/patterns/caching/
    # for details about caching
    from werkzeug.contrib.cache import SimpleCache
    cache = SimpleCache()

import namebot.examples as examples
import namebot.settings as defaults

import forms as web_forms
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect


app = Flask(__name__)
app.debug = True


# Generate all types of
# sample data for demoing and testing
example_data = examples.generate_all_examples(
    filename=None,
    words=defaults.TEST_DATA)
seed_data = defaults.TEST_DATA
metrics = example_data['metrics']
test_data = example_data['synsets']
scoring = example_data['scoring']
techniques = example_data['techniques']


@app.route('/')
def dashboard():
    return render_template(
        'dashboard.html',
        example_data=example_data,
        metrics=metrics)


@app.route('/visualization')
def visualization():
    return render_template(
        'visualization.html',
        example_data=example_data,
        metrics=metrics)


@app.route('/nltk-explorer')
def nltk():
    return render_template(
        'nltk-explorer.html',
        seed_data=seed_data,
        example_data=example_data,
        test_data=test_data)


@app.route('/name-generator')
def generator():
    form = web_forms.NameGeneratorForm()
    return render_template(
        'generator.html',
        form=form,
        techniques=techniques,
        scoring=scoring,
        example_data=example_data,
        seed_data=seed_data)


@app.route('/generate', methods=['GET', 'POST'])
def generate_name():
    template = 'generator-form.html'
    if request.method == 'GET':
        form = web_forms.NameGeneratorForm()
        return render_template(
            template,
            form=form)
    else:
        form = web_forms.NameGeneratorForm(request.form)
        if form.validate():
            word_vals = []
            word_vals.append(form.field1.data)
            word_vals.append(form.field2.data)
            word_vals.append(form.field3.data)
            word_vals.append(form.field4.data)
            word_vals.append(form.field5.data)
            free_list = form.field6.data.split(' ')
            word_vals = filter(None, word_vals + free_list)
            example_data = examples.generate_all_examples(
                filename=None,
                words=word_vals)
            return render_template(
                template,
                metrics=example_data['metrics'],
                test_data=example_data['synsets'],
                scoring=example_data['scoring'],
                techniques=example_data['techniques'],
                names='TEST')
        else:
            return redirect(request.path)


if __name__ == '__main__':
    app.run()
