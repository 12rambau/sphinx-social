Usage
=====

**sphinx-social** is an extention that provides support to embed social media posts in your Sphinx based documentation.

For each social media service, use the appropriate directive (the name of the service) and the link of the post you want to share, instruction for finding the links will be given for each social media.
The produce directive will be shaped as such:

.. code-block:: rst

    .. <service_name>:: social_link

We currently support the following services:

-   :ref:`usage:facebook`
-   :ref:`usage:linkedin`
-   :ref:`usage:mastodon`
-   :ref:`usage:twitter`

More specific information for each provider can be found in the following sections.

facebook
--------

For Facebook posts, find the publication on a facebook wall. In the top-right corner of the post panel, click on :btn:`<fa-solid fa-ellipsis>` and then on :btn:`<fa-solid fa-code> Embed`. A popup window will open. Click on :btn:`advance parameter` and Facebook will redirect you to a new page. There copy the link in the "Url of Post" field. See the following screenshots for more details:

.. thumbnail:: ./_static/usage/facebook_click.png
    :width: 32%
    :group: facebook

.. thumbnail:: ./_static/usage/facebook_advance.png
    :width: 32%
    :group: facebook

.. thumbnail:: ./_static/usage/facebook_copy.png
    :width: 32%
    :group: facebook

Once you have it use the `facebook` directive as in this example:

.. tab-set::

    .. tab-item:: rst

        .. code-block:: rst

            .. facebook:: https://www.facebook.com/GitHub/posts/pfbid0Qz2vi4kZsW9PwfB4uUEM9SbYP5KNr8ETcMKafabJUV4qXUgHrZ4hKsv1NunmNEGgl

    .. tab-item:: output

        .. facebook:: https://www.facebook.com/GitHub/posts/pfbid0Qz2vi4kZsW9PwfB4uUEM9SbYP5KNr8ETcMKafabJUV4qXUgHrZ4hKsv1NunmNEGgl

linkedin
--------

For linkedin posts, got to the linkedin page and find your post. In the top-right corner of the post panel, click on :btn:`<fa-solid fa-ellipsis>` and then on :btn:`<fa-solid fa-code> Embed this post`. A popup window will appear on screen, copy the link inside the iframe code. See the following screenshots for more details:

.. thumbnail:: ./_static/usage/linkedin_click.png
    :width: 49%
    :group: linkedin

.. thumbnail:: ./_static/usage/linkedin_copy.png
    :width: 49%
    :group: linkedin

Once you have it use the `linkedin` directive as in this example:

.. tab-set::

    .. tab-item:: rst

        .. code-block:: rst

            .. linkedin:: https://www.linkedin.com/video/embed/live/urn:li:ugcPost:7052479613825941504

    .. tab-item:: output

        .. linkedin:: https://www.linkedin.com/video/embed/live/urn:li:ugcPost:7052479613825941504

mastodon
--------

For mastodon, go to your mastodon instance (in this example https://hachyderm.io) and find your post. in the bottom-right side of the post icon bar, click on :btn:`<fa-solid fa-ellipsis>` and then on :btn:`copy the link`. See the following screenshot for more details:

.. thumbnail:: ./_static/usage/mastodon_copy.png
    :group: mastodon

Once you have it use the `mastodon` directive as in this example:

.. tab-set::

    .. tab-item:: rst

        .. code-block:: rst

            .. mastodon:: https://mstdn.social/@GitHub/103392841403991431

    .. tab-item:: output

        .. mastodon:: https://mstdn.social/@GitHub/103392841403991431

twitter
-------

For tweets, click on the :btn:`<fa-solid fa-ellipsis>` in the top-right corner of the tweet and click on :btn:`<fa-solid fa-code> Integrate`. This should open a second page where you'll find in the top text field the full linkt to the tweet. See the follwoing screenshot for more details.

.. thumbnail:: ./_static/usage/twitter_click.png
    :width: 49%
    :group: twitter

.. thumbnail:: ./_static/usage/twitter_copy.png
    :width: 49%
    :group: twitter

Once you have it use the `twitter`` directive as in this example:

.. tab-set::

    .. tab-item:: rst

        .. code-block:: rst

            .. twitter:: https://twitter.com/github/status/1638541174611779584

    .. tab-item:: output

        .. twitter:: https://twitter.com/github/status/1638541174611779584



