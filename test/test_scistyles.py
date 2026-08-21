import pytest
import os.path as pth
from glob import glob
from itertools import chain
import scistyles
from matplotlib.style import use

scistyles_dirs = scistyles.__path__


@pytest.fixture(
    params=[
        pth.splitext(pth.basename(filename))[0]
        for directory in scistyles_dirs
        for filename in glob(pth.join(directory, "*.mplstyle"))
    ]
)
def stylename(request):
    return request.param


def test_files():
    # check that there is at least one style file
    files = list(
        chain.from_iterable(
            glob(pth.join(directory, "*.mplstyle"))
            for directory in scistyles_dirs
        )
    )
    assert len(files) > 0


# def test_available():
#     # check this was synced into `available`
#     for stylename in list_styles():
#         assert stylename in available

def test_use(stylename):
    # check we can use the style
    use(f"scistyles.{stylename}")
    assert True
