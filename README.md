Python TravisCI Deploys
======

[![Join the chat at https://gitter.im/jsvgoncalves/python-deploys](https://badges.gitter.im/jsvgoncalves/python-deploys.svg)](https://gitter.im/jsvgoncalves/python-deploys?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Testing out TravisCI deployments.

Development
------

To setup your virtualenv:

    $ mkvirtualenv myflaskapp
    $ setvirtualenvproject myflaskapp path_to_project

    # Optionally, create a new project with
    $ mkproject myflaskapp
    $ git clone git@github.com:jsvgoncalves/flask-starter-guide .

Then, everytime you work on the project, run:

    $ workon myflaskapp

To install the dependecies run:

    $ pip install -r requirements.txt

### Virtualenvwrapper cheatsheet

    # To stop working
    $ deactivate
    # To show all environments
    $ workon
    # To show installed packages
    $ lssitepackages
