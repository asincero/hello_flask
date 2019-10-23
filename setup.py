"""
@file setup.py
Package setup file.

@author Arcadio A. Sincero Jr., <arcadiosincero@gmail.com>
@date 10/18/2019

Copyright (c) 2019 Arcadio A. Sincero Jr.
"""

# pylint: disable=invalid-name

import setuptools  # type: ignore
import setuptools.command.install  # type: ignore
import setuptools.command.develop  # type: ignore

import hello_flask


def common_prerun_tasks() -> None:
    """
    Performs the common tasks to be performed by both the CustomInstall.run()
    and CustomDevelop.run() methods before it is invoked.
    """


def common_postrun_tasks() -> None:
    """
    Performs the common tasks to be performed by both the CustomeInstall.run()
    and CustomDevelop.run() methods after it is invoked.
    """


class CustomInstall(setuptools.command.install.install):
    """Extends the stock 'install' command to performm custom build steps."""

    def run(self) -> None:
        """Base class override."""
        common_prerun_tasks()
        super().run()
        common_postrun_tasks()


class CustomDevelop(setuptools.command.develop.develop):
    """Extends the stock 'develop' command to performm custom build steps."""

    def run(self) -> None:
        """Base class override."""
        common_prerun_tasks()
        super().run()
        common_postrun_tasks()


packages = setuptools.find_packages()
setuptools.setup(
    name=hello_flask.NAME,
    version=hello_flask.VERSION,
    author=hello_flask.AUTHOR,
    license=hello_flask.LICENSE,
    packages=packages,
    include_package_data=True,
    zip_safe=False
)
