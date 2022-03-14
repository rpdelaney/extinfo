extinfo
======================
|LANGUAGE| |VERSION| |LICENSE| |MAINTAINED| |CIRCLECI| |MAINTAINABILITY|
|STYLE|

.. |CIRCLECI| image:: https://img.shields.io/circleci/build/gh/rpdelaney/extinfo
   :target: https://circleci.com/gh/rpdelaney/extinfo/tree/main
.. |LICENSE| image:: https://img.shields.io/badge/license-Apache%202.0-informational
   :target: https://www.apache.org/licenses/LICENSE-2.0.txt
.. |MAINTAINED| image:: https://img.shields.io/maintenance/yes/2022?logoColor=informational
.. |VERSION| image:: https://img.shields.io/pypi/v/extinfo
   :target: https://pypi.org/project/extinfo
.. |STYLE| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
.. |LANGUAGE| image:: https://img.shields.io/pypi/pyversions/extinfo
.. |MAINTAINABILITY| image:: https://img.shields.io/codeclimate/maintainability-percentage/rpdelaney/extinfo
   :target: https://codeclimate.com/github/rpdelaney/extinfo

Given a file extension, extinfo will scrape web sources for information about
what type of file is usually named with that extension.

If you want to know what's in an actual file you have on disk, you should use
the file command or another tool that leverages libmagic.

Installation
------------

.. code-block :: console

    pip3 install extinfo

Usage
-----

.. code-block :: console

    $ extinfo -h

============
Development
============

To install development dependencies, you will need `poetry <https://docs.pipenv.org/en/latest/>`_
and `pre-commit <https://pre-commit.com/>`_.

.. code-block :: console

    pre-commit install --install-hooks
    poetry install && poetry shell

`direnv <https://direnv.net/>`_ is optional, but recommended for convenience.
