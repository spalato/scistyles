import pytest
import os.path as pth
from glob import glob
from itertools import chain
from scistyles import scistyles_dir, list_styles#, update_library
from matplotlib.style.core import library, available
from matplotlib.style import use

def test_files():
    # check that there is at least one style file
    files = list(chain([glob(d+"/*.mplstyle") for d in scistyles_dir]))
    assert len(files) > 0

def test_list_styles():
    files = list(chain([glob(d+"/*.mplstyle") for d in scistyles_dir]))
    listed = list_styles()
    assert len(files) == len(listed) # for now...

def test_autoupdate():
    # check all our styles got added to the list
    for stylename in list_styles():
        assert stylename in library

def test_available():
    # check this was synced into `available`
    for stylename in list_styles():
        assert stylename in available

def test_use():
    # check we can use the style
    for stylename in list_styles():
        use(stylename)
    assert True
