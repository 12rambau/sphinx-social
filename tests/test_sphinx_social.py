"""Test the sphinx_social package."""

import pytest
from bs4 import BeautifulSoup, formatter

fmt = formatter.HTMLFormatter(indent=2, void_element_close_prefix=" /")


@pytest.mark.sphinx("epub", testroot="providers")
def test_epub(app, status, warning):
    """Build a epub output (unsuported)."""
    app.builder.build_all()

    assert "unsupported output format (node skipped)" in warning.getvalue()


@pytest.mark.sphinx("latex", testroot="providers")
def test_latex(app, status, warning):
    """Build a latex output (unsuported)."""
    app.builder.build_all()

    assert "unsupported output format (node skipped)" in warning.getvalue()


@pytest.mark.sphinx("html", testroot="providers")
def test_facebook_html(app, status, warning, file_regression):
    """Build an facebook embed in HTML."""
    app.builder.build_all()

    html = (app.outdir / "_facebook.html").read_text(encoding="utf8")
    html = BeautifulSoup(html, "html.parser")

    iframe = html.select("iframe")[0].prettify(formatter=fmt)
    file_regression.check(iframe, basename="facebook", extension=".html")


@pytest.mark.sphinx("html", testroot="providers")
def test_linkedin_html(app, status, warning, file_regression):
    """Build an linkedin embed in HTML."""
    app.builder.build_all()

    html = (app.outdir / "_linkedin.html").read_text(encoding="utf8")
    html = BeautifulSoup(html, "html.parser")

    iframe = html.select("iframe")[0].prettify(formatter=fmt)
    file_regression.check(iframe, basename="linkedin", extension=".html")


@pytest.mark.sphinx("html", testroot="providers")
def test_twitter_html(app, status, warning, file_regression):
    """Build a twitter embed in HTML."""
    app.builder.build_all()

    html = (app.outdir / "_twitter.html").read_text(encoding="utf8")
    html = BeautifulSoup(html, "html.parser")

    blockquote = html.select("blockquote")[0].prettify(formatter=fmt)
    file_regression.check(blockquote, basename="twitter", extension=".html")


@pytest.mark.sphinx("html", testroot="providers")
def test_mastodon_html(app, status, warning, file_regression):
    """Build a mastodon embed in HTML."""
    app.builder.build_all()

    html = (app.outdir / "_mastodon.html").read_text(encoding="utf8")
    html = BeautifulSoup(html, "html.parser")

    iframe = html.select("iframe")[0].prettify(formatter=fmt)
    file_regression.check(iframe, basename="mastodon", extension=".html")
