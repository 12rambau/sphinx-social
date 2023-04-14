"""Skeleton of the social directive ready to be extended for specific providers."""

from typing import List, Type
from urllib.parse import urlparse

from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.util import logging
from sphinx.util.docutils import SphinxTranslator

logger = logging.getLogger(__name__)

# -- node and directive definition ---------------------------------------------


class social_node(nodes.General, nodes.Element):
    """Video node."""

    def parse(self, url: str) -> str:
        """Parse the url according to the platform needs."""
        # raise error if the url is malformed
        parsed = urlparse(url)
        if not all([parsed.scheme, parsed.netloc]):
            logger.warning(
                f'Ignoring: invalid url: "{url}".', location=self.get("location")
            )
            raise nodes.SkipNode

        return url


class Social(Directive):
    """Abstract Video directive."""

    _node: Type[social_node] = social_node
    "Subclasses should replace with node class."

    _platform: str = ""
    "name of the platform"

    _iframe: str = ""
    "The template of the <iframe> component"

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False

    def run(self) -> List[nodes.Node]:
        """Setup the directive in the builder context."""
        return [
            self._node(
                url=self.arguments[0],
                platform=self._platform,
                iframe=self._iframe,
            )
        ]


# -- builder specific methods --------------------------------------------------


def visit_video_node_html(translator: SphinxTranslator, node: social_node) -> None:
    """Visit html video node."""
    url = node.parse(node["url"])
    translator.body.append(node["iframe"].format(url))


def visit_video_node_unsupported(
    translator: SphinxTranslator, node: social_node
) -> None:
    """Visit unsuported video node."""
    logger.warning(f"{node['platform']}: unsupported output format (node skipped)")
    raise nodes.SkipNode


def depart_social_node(translator: SphinxTranslator, node: social_node) -> None:
    """Depart any video node."""
    pass


_NODE_VISITORS = {
    "html": (visit_video_node_html, depart_social_node),
    "epub": (visit_video_node_unsupported, depart_social_node),
    "latex": (visit_video_node_unsupported, depart_social_node),
    "man": (visit_video_node_unsupported, depart_social_node),
    "texinfo": (visit_video_node_unsupported, depart_social_node),
    "text": (visit_video_node_unsupported, depart_social_node),
}
