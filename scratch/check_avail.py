# investigating how the library of styles is built.
# Maybe we should just extend it directly
# the debugger has problem running matplotlib...

import matplotlib.pyplot as plt
from pprint import pprint
from copy import deepcopy
import os.path as pth

# objects to investigate:
# avail
avail = plt.style.available
print("- "*30)
print("avail", "type", type(avail)) # list
pprint(avail)

# library
print("- "*30)
print("library", "type", type(plt.style.library)) # a dict subtype
pprint(plt.style.library.keys())

# library
print("- "*30)
print("USER_LIBRARY_PATHS", "USER_LIBRARY_PATHS", type(plt.style.core.USER_LIBRARY_PATHS)) # a dict subtype
pprint(plt.style.core.USER_LIBRARY_PATHS)

# we can probably just append to library.
# there are a bunch of tools to help:
# read_style_directory
# update_user_library #  Do something like this.

# check if we can append.

test = deepcopy(plt.style.library["fast"])

print(type(test))
test['path.simplify_threshold']=0.8

plt.style.library["notsofast"] = test

plt.style.use("notsofast")
assert plt.rcParams['path.simplify_threshold'] == 0.8 

scistyle_path = pth.abspath(pth.join(pth.dirname(__file__), "..", "stylelib"))
print(scistyle_path)
new_ = {"scistyles-"+k: v for
        k, v in plt.style.core.read_style_directory(scistyle_path).items()
}
plt.style.core.update_nested_dict(plt.style.library, new_)

assert "scistyles-ACS_nano" in plt.style.library
# good. We have path to work with
# 1. organize a directory of styles
# 2. reproduce something like 'update_user_library', updating the library
# 3. ???
# 4. profit

