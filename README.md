[![Coverage Status](https://coveralls.io/repos/christabor/namebot/badge.svg?branch=master&service=github)](https://coveralls.io/github/christabor/namebot?branch=master)
[![Build Status](https://travis-ci.org/christabor/namebot.svg?branch=master)](https://travis-ci.org/christabor/namebot)
[![PyPI version](https://badge.fury.io/py/namebot.svg)](http://badge.fury.io/py/namebot)
![Donation badge](https://img.shields.io/gratipay/christabor.svg)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/christabor/namebot/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/christabor/namebot/?branch=master)
[![Code Climate](https://codeclimate.com/github/christabor/namebot/badges/gpa.svg)](https://codeclimate.com/github/christabor/namebot)

# Namebot
A company/product/whatever name generating tool written in Python.

This project is ongoing, but feel free to contribute! It's a full-fledged suite of tools that can help you get started generating real business names for your project or company!

## Modules:

### Metrics
A class of utilities for generating all kinds of linguistic metrics for a set of words.

### NLP
Natural language processing tools for finding word relationships - uses NLTK for all of the heavy-lifting.

### Normalization
Some tools for normalizing and formatting content for use with the rest of the library.

### Scoring
Some scoring algorithms, primarily for classifying pronunciation, such as Soundex or Double Metaphone.

### Techniques
The major chunk of work represented in this library. The many techniques I've created after researching hundreds of corporate names and naming agency techniques

### Language Techniques
Techniques that involve the use of language translation for stylistic name use, such as Latin.

### Strainer
Similar to normalization, but for filtering based on rules, like length, count, etc... good for mapping 1:1 with UI inputs or just calling from the functions directly.

## How to setup server and test:

```
sudo make install
```

Check out https://github.com/Automotron/namebot-flask to see an example app
and configuration setup to use namebot and generate results with test data.

## Library Dependencies
See [requirements.txt](requirements.txt) and [Makefile](Makefile) for details.

## Tests

```
sudo make install
make tests
```

Tests are available in the `tests/` folder. They are not super comprehensive, but there is coverage. Test runner is provided by nose and can be run via `make`.

## Versioning

Versioning style follows the semantic versioning convention. For more info, see http://semver.org/

----

### Support / donations
<div class="donate-button">
    <a class="donate-button-link" href="#">
        <img src="http://ef3ae845b6eed6ec4024-8a0a46e5f1a5cc9854958bc3503f0f88.r40.cf1.rackcdn.com/donate_64.png" alt="Donate Ƀitcoin" />
    </a>
    <div class="bitcoin-address">Ƀitcoin address: <code>1G5MdiPHCnPJUKXW1SJwWmUTDVjG1aG7xj</code></div>
</div>
