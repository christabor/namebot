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


app = Flask(__name__)
app.debug = True


# Generate all types of
# sample data for demoing and testing
example_data = examples.generate_all_examples()
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
        techniques=techniques,
        scoring=scoring,
        example_data=example_data,
        seed_data=seed_data,
        form=form)


@app.route('/name-generator/generate')
def generate_name():
    form = web_forms.NameGeneratorForm()

    return render_template(
        'generator.html',
        seed_data=seed_data,
        form=form,
        names=['TEST'],)


if __name__ == '__main__':
    app.run()
