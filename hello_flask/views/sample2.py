"""
@file sample2.py
Implements the 'sample2' view.

@author Arcadio A. Sincero Jr., <arcadio.sincero@gmail.com>
@date 10/17/2019

Copyright (c) 2019 Arcadio A. Sincero Jr.
"""

# pylint: disable=invalid-name

import typing
import flask

# The blueprint that defines the view this module implements.
blueprint = flask.Blueprint(__name__.split('.')[-1], __name__)


@blueprint.route('/')
def main() -> typing.Any:
    """Renders the main view."""
    return flask.render_template('sample2/sample-template2.html',
                                 message='This is sample template page #2.')
