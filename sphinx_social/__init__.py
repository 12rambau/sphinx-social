"""The init file of the package."""

from typing import Any, Dict

from sphinx.application import Sphinx

from .facebook import Facebook, facebook_node
from .linkedin import Linkedin, linkedin_node
from .mastodon import Mastodon, mastodon_node
from .twitter import Twitter, twitter_node
from .utils import _NODE_VISITORS

__version__ = "0.0.0"
__author__ = "Pierrick Rambaud"
__email__ = "pierrick.rambaud49@gmail.com"


def setup(app: Sphinx) -> Dict[str, Any]:
    """Setup Sphinx application."""
    # add the node directives to the build
    socials = {
        "mastodon": [mastodon_node, Mastodon],
        "facebook": [facebook_node, Facebook],
        "linkedin": [linkedin_node, Linkedin],
        "twitter": [twitter_node, Twitter],
    }

    for platform, nodes in socials.items():
        app.add_node(nodes[0], **_NODE_VISITORS)  # type: ignore
        app.add_directive(platform, nodes[1])

    # add the javascript required by some providers
    js_params = {"async": "async", "charset": "utf-8"}
    app.add_js_file("https://platform.twitter.com/widgets.js", **js_params)  # type: ignore

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
