"""Directive dedicated to the twitter platform."""

from urllib.parse import urlparse

from docutils import nodes
from sphinx.util import logging

from . import utils

logger = logging.getLogger(__name__)


class twitter_node(utils.social_node):
    """same node new name."""

    def parse(self, url: str) -> str:
        """parse the url to transform it into a embed link."""
        url = super().parse(url)
        parsed = urlparse(url)
        if not parsed.netloc == "twitter.com":
            logger.warning(
                f'Ignoring: invalid facebook url: "{url}".',
                location=self.get("location"),
            )
            raise nodes.SkipNode

        return url


class Twitter(utils.Social):
    """Custom version of the Social directive."""

    _node = twitter_node
    _platform = "twitter"
    _iframe = '<blockquote class="twitter-tweet"><p lang="en" dir="ltr"><a href="{}">Tweet from @github</a></blockquote>'
