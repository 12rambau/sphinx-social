"""Directive dedicated to the mastodon platform."""


from sphinx.util import logging

from . import utils

logger = logging.getLogger(__name__)


class mastodon_node(utils.social_node):
    """same node new name."""

    def parse(self, url: str) -> str:
        """parse the url to transform it into a embed link."""
        url = super().parse(url)

        # TODO raise error if the website is not a mastodon one and skip the node

        # add embed at the end of the link
        return url + "/embed"


class Mastodon(utils.Social):
    """Custom version of the Social directive."""

    _node = mastodon_node
    _platform = "mastodon"
    _iframe = '<iframe src="{}" class="socialpost mastodon-embed" style="width: 100%; border: 0; border-radius: .5rem;" height="500" allowfullscreen="allowfullscreen"></iframe>'
