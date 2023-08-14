# `gradio-blocks` 🖥️
Assortment of [gradio](https://gradio.app/) features using [nbdev](https://nbdev.fast.ai/) and [altair](https://altair-viz.github.io/).


# 1. Set up environment 🛠️
```
> git clone https://github.com/lukexyz/gradio-blocks.git
> cd gradio-blocks

> conda create -n gblocks python=3.11 pip jupyter
> conda activate gblocks
> pip install -r requirements.txt
```

# 2. Initialise `nbdev` 🧪
```
> nbdev_new
> nbdev_install_hooks
```

# 3. `nb` cell magic ✨
① Label output module,  


```py
#| default_exp core
```
② Export cell funtion,  
```py
#| export
def foo(): pass
```
③ Run export command 
```py
#| hide
import nbdev; nbdev.nbdev_export()
```