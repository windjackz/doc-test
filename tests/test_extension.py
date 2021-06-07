"""Test working of extension."""

import os

import pytest

from sphinx_search.extension import ASSETS_FILES
from tests import TEST_DOCS_SRC


@pytest.mark.sphinx(
    srcdir=TEST_DOCS_SRC,
    confoverrides={
        'rtd_sphinx_search_file_type': 'minified'
    }
)
def test_minified_static_files_injected_in_html(selenium, app, status, warning):
    """Test if the static files are correctly injected in the html."""
    app.build()
    path = app.outdir / 'index.html'

    selenium.get(f'file://{path}')
    page_source = selenium.page_source

    file_type = app.config.rtd_sphinx_search_file_type
    assert file_type == 'minified'

    for file in ASSETS_FILES[file_type]:
        file_path = os.path.join(app.outdir, '_static', file)
        assert (
            os.path.exists(file_path)
        ), f'{file_path} should be present in the _build folder'

        file_name = file.split('/')[-1]
        assert (
            page_source.count(file_name) == 1
        ), f'{file} should be present in the page source'


@pytest.mark.sphinx(
    srcdir=TEST_DOCS_SRC,
    confoverrides={
        'rtd_sphinx_search_file_type': 'un-minified'
    }
)
def test_un_minified_static_files_injected_in_html(selenium, app, status, warning):
    """Test if the static files are correctly injected in the html."""
    app.build()
    path = app.outdir / 'index.html'

    selenium.get(f'file://{path}')
    page_source = selenium.page_source

    file_type = app.config.rtd_sphinx_search_file_type
    assert file_type == 'un-minified'

    for file in ASSETS_FILES[file_type]:
        file_path = os.path.join(app.outdir, '_static', file)
        assert (
            os.path.exists(file_path)
        ), f'{file_path} should be present in the _build folder'

        file_name = file.split('/')[-1]
        assert (
            page_source.count(file_name) == 1
        ), f'{file} should be present in the page source'
