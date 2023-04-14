"""Directive dedicated to the facebook platform."""

from urllib.parse import urlparse

from docutils import nodes
from sphinx.util import logging

from . import utils

logger = logging.getLogger(__name__)


class facebook_node(utils.social_node):
    """same node new name."""

    def parse(self, url: str) -> str:
        """parse the url to transform it into a embed link."""
        url = super().parse(url)
        if not urlparse(url).netloc == "www.facebook.com":
            logger.warning(
                f'Ignoring: invalid facebook url: "{url}".',
                location=self.get("location"),
            )
            raise nodes.SkipNode

        # replace all the "/" by "%2F"
        return url.replace("/", "%2F")


class Facebook(utils.Social):
    """Custom version of the Social directive."""

    _node = facebook_node
    _platform = "facebook"
    _iframe = '<iframe src="https://www.facebook.com/plugins/post.php?href={}" width="500" height="686" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>'
