
sphinx-social
=============

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg?logo=opensourceinitiative&logoColor=white
    :target: LICENSE
    :alt: License: MIT

.. image:: https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg?logo=git&logoColor=white
   :target: https://conventionalcommits.org
   :alt: conventional commit

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black badge

.. image:: https://img.shields.io/badge/code_style-prettier-ff69b4.svg?logo=prettier&logoColor=white
   :target: https://github.com/prettier/prettier
   :alt: prettier badge

.. image:: https://img.shields.io/badge/pre--commit-active-yellow?logo=pre-commit&logoColor=white
    :target: https://pre-commit.com/
    :alt: pre-commit

.. image:: https://img.shields.io/pypi/v/sphinx-social?color=blue&logo=pypi&logoColor=white
    :target: https://pypi.org/project/sphinx-social/
    :alt: PyPI version

.. image:: https://img.shields.io/github/actions/workflow/status/12rambau/sphinx-social/unit.yaml?logo=github&logoColor=white
    :target: https://github.com/12rambau/sphinx-social/actions/workflows/unit.yaml
    :alt: build

.. image:: https://img.shields.io/codecov/c/github/12rambau/sphinx-social?logo=codecov&logoColor=white
    :target: https://codecov.io/gh/12rambau/sphinx-social
    :alt: Test Coverage

.. image:: https://img.shields.io/readthedocs/sphinx-social?logo=readthedocs&logoColor=white
    :target: https://sphinx-social.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/all_contributors-0-orange.svg
    :alt: All contributors
    :target: AUTHORS.rst

Overview
--------

Ths extention provide support to embed social media posts in your Sphinx based documentation.

each service is served by a custom directive like :

.. code-block:: rst

    .. twitter:: https://twitter.com/github/status/1638541174611779584

We currently support the following services:
- facebook
- linkedin
- mastodon
- twitter

If you want to see your favorite Social media in this list, please mention them in our `issue tracker <https://github.com/12rambau/sphinx-social/issues>`__.

Credits
-------

Initialy posted as a concept idea by `@choldgraf <https://github.com/choldgraf>`__ on his `blog <https://chrisholdgraf.com/blog/2023/social-directive/>`__.

This package was created with `Cookiecutter <https://github.com/cookiecutter/cookiecutter>`__ and the `12rambau/pypackage <https://github.com/12rambau/pypackage>`__ project template.
