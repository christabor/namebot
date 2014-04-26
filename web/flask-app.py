import app_settings
if app_settings.CACHE_ENABLED:
    # See http://flask.pocoo.org/docs/patterns/caching/
    # for details about caching
    from werkzeug.contrib.cache import SimpleCache
    cache = SimpleCache()

from namebot import techniques
from namebot import metrics
from namebot import scoring
from namebot import examples as examples
from namebot import settings as defaults

import forms as web_forms
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect


app = Flask(__name__)
app.debug = True


# Redefine for shorter name
get_data = examples.generate_all_examples


@app.route('/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/visualization')
def visualization():
    return render_template(
        'visualization.html',
        metrics=metrics.generate_all_metrics(
            filename=None,
            words=defaults.TEST_DATA))


@app.route('/nltk-explorer')
def nltk():
    example = get_data(
        filename=None,
        words=defaults.TEST_DATA)
    return render_template(
        'nltk-explorer.html',
        seed_data=defaults.TEST_DATA,
        example_data=example['synsets'],
        test_data=defaults.TEST_DATA)


@app.route('/name-generator')
def generator():
    example = get_data(
        filename=None,
        words=defaults.TEST_DATA)
    form = web_forms.NameGeneratorForm()
    return render_template(
        'generator.html',
        form=form,
        techniques=techniques.generate_all_techniques(defaults.TEST_DATA),
        scoring=scoring.generate_all_scoring(defaults.TEST_DATA),
        example_data=example['synsets'],
        seed_data=defaults.TEST_DATA)


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
            return render_template(
                template,
                scoring=scoring.generate_all_scoring(word_vals),
                techniques=techniques.generate_all_techniques(word_vals),
                names='TEST')
        else:
            return redirect(request.path)


if __name__ == '__main__':
    app.run(debug=True)
