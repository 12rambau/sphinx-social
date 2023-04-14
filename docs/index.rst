:html_theme.sidebar_secondary.remove:


sphinx-social
=============

.. toctree::
   :hidden:

   usage
   contribute
   API <api/modules>

Overview
--------

Ths extention provides support to embed social media posts in your Sphinx based documentation.

each service is served by a custom directive like :

.. code-block:: rst

    .. twitter:: https://twitter.com/github/status/1638541174611779584

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


Documentation contents
----------------------

The documentation contains 3 main sections:

.. grid:: 1 2 3 3

   .. grid-item::

      .. card:: Usage
         :link: usage.html

         Usage and installation

   .. grid-item::

      .. card:: Contribute
         :link: contribute.html

         Help us improve the lib.

   .. grid-item::

      .. card:: API
         :link: api/modules.html

         Discover the lib API.
