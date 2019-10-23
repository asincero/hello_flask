"""
@file __init__.py
This package implements the Flask application.

@author Arcadio A. Sincero Jr., <arcadio.sincero@gmail.com>
@date 10/16/2019

Copyright () 2019 Arcadio A. Sincero Jr.
"""

import os
import sys
import typing
import logging
import flask

from . import views


NAME = 'hello_flask'
VERSION = '0.0.1'
AUTHOR = 'Arcadio A. Sincero Jr.'
LICENSE = 'Copyright (c) 2019 Arcadio A. Sincero Jr.'


def create_app() -> flask.Flask:
    """
    Factory function invoked by Flask to instantiate the application object.
    """
    class CustomFormatter(logging.Formatter):
        """Implements a custom log formatter."""

        def __init__(self) -> None:
            """Constructor."""
            super().__init__('%(levelname)s: %(message)s')

        def format(self, record: typing.Any) -> str:
            """Base class override."""
            # Every line of the log message will be prefixed with the name of
            # application.  This will help in distinguishing which log messages
            # are coming from the application and which messages are coming
            # from the WSGI container hosting the application.
            ret = ''
            for line in super().format(record).split('\n'):
                if ret:
                    ret += '\n'

                ret += f'[{NAME}] {line}'

            return ret

        def formatException(self, exc_info: typing.Any) -> str:
            """Base class override."""
            # For aesthetic reasons, every line of the traceback will be
            # prefixed with "ERROR".
            ret = ''
            for line in super().formatException(exc_info).split('\n'):
                if ret:
                    ret += '\n'

                ret += f'ERROR: {line}'

            return ret

    # Configure logging first.
    logging.getLogger().setLevel(logging.DEBUG)  # always log DEBUG messages
    handler = logging.StreamHandler()
    handler.setFormatter(CustomFormatter())
    logging.getLogger().addHandler(handler)

    # Then instantiate the Flask application object.  We always do this *after*
    # logging has been configured.
    ret = flask.Flask(__name__, instance_relative_config=True)

    # Hardcode some configuration settings, then read additional configuration
    # from a file.  Read the configuration file second so that settings in the
    # file will override the hardcoded settings.
    ret.config['SECRET_KEY'] = 'dev'
    ret.config.from_pyfile('config.py', silent=True)

    # Make sure the instance folder exists.
    os.makedirs(ret.instance_path, exist_ok=True)

    # Register view blueprints.
    ret.register_blueprint(views.sample.blueprint, url_prefix='/sample')
    ret.register_blueprint(views.sample2.blueprint, url_prefix='/sample2')

    # Redirect "/" to the 'sample' view.
    # pylint: disable=unused-variable
    @ret.route('/')
    def index() -> typing.Any:
        return flask.redirect('/sample')

    return ret


def application(env: typing.Any, start_response: typing.Any) -> typing.Any:
    """
    Function invoked by uWSGI to create the application WSGI entry point.
    """
    ret = create_app()
    return ret(env, start_response)
