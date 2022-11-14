# scistyles
Matplotlib stylesheets and figure design tools.

# Installation
Currently, git clone, then run
```
pip install -e .
```

# Usage
The stylesheets under `src/scistyles/stylelib` are loaded automatically. Therefore, just `use` them:
```python
import matplotlib.pyplot as plt
import scistyles

plt.style.use("presentation-sp")
# plot away!
```

# Contributing
Coming soon.

# TODO
todolist  
[ ] Add contribution guideliunes
[ ] setup distribution
[ ] release
[ ] add a few further design tools (colors, palettes...)
[ ] Add a test plot and autogenerated gallery.