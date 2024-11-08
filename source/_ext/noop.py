from __future__ import annotations

from docutils import nodes

from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx.util.typing import ExtensionMetadata


class NoopDirective(SphinxDirective):
    """A directive to do nothing"""

    required_arguments = 0
    optional_arguments = 3
    has_content = True

    def run(self) -> list[nodes.Node]:
        return []


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_directive('badger', NoopDirective)
    app.add_directive('oddeven', NoopDirective)
    app.add_directive('contents', NoopDirective)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
