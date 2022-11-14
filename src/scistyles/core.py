import os.path as pth
#import matplotlib.pyplot as plt
from matplotlib.style.core import read_style_directory, update_nested_dict, available, library

# check if this finds the resources when installing the module using pip.
scistyles_dir = [pth.abspath(pth.join(pth.dirname(__file__), "stylelib"))]

def list_styles(style_dirs: list=None) -> dict:
    style_dirs = scistyles_dir if style_dirs is None else style_dirs
    styles = dict()
    for stylelib_path in style_dirs:
        styles.update(read_style_directory(stylelib_path))
    return styles


def update_library(library, available, style_dirs=None):
    style_dirs = scistyles_dir if style_dirs is None else style_dirs
    update_nested_dict(library, list_styles(style_dirs))
    available[:] = sorted(library.keys())
    return library

update_library(library, available, scistyles_dir)
