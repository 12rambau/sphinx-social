"""Directive dedicated to the linkedin platform."""

import re
from urllib.parse import urlparse

from docutils import nodes
from sphinx.util import logging

from . import utils

logger = logging.getLogger(__name__)


class linkedin_node(utils.social_node):
    """same node new name."""

    def parse(self, url: str) -> str:
        """parse the url to transform it into a embed link."""
        url = super().parse(url)
        # raise error if the website is not a mastodon one and skip the node
        parsed = urlparse(url)
        if not parsed.netloc == "www.linkedin.com":
            logger.warning(
                f'Ignoring: invalid linkedin url: "{url}".',
                location=self.get("location"),
            )
            raise nodes.SkipNode

        # extract the post id from the link
        regex = r"^.*(\d{10,}).*$"
        id = re.search(regex, parsed.path).group(1)
        embed_url = "https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:{}"
        return embed_url.format(id)


class Linkedin(utils.Social):
    """Custom version of the Social directive."""

    _node = linkedin_node
    _platform = "linkedin"
    _iframe = '<iframe src="{}" allowfullscreen="" title="Embedded post" width="504" height="443" frameborder="0"></iframe>'
