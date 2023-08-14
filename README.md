# gradio-blocks
Assortment of gradio features using nbdev and altair.

# 1. Set up environment
```
> git clone https://github.com/lukexyz/gradio-blocks.git
> cd gradio-blocks

> conda create -n gblocks python=3.11 pip jupyter
> conda activate gblocks
> pip install -r requirements.txt
```

# 2. Initialise `nbdev`
```
> nbdev_new
> nbdev_install_hooks
```

# 3. Magic `nb` cell magic
```py
#| default_exp core
```
```py
#| hide
import nbdev; nbdev.nbdev_export()
```