# this file must be loaded in jupyter notebook
# in order to be able to load IPython.core.magic
from IPython.core.magic import register_cell_magic
@register_cell_magic
def save2file(file, cell):
    'save python code block to a file'
    with open(file, 'w') as fd:
        fd.write(cell)
@register_cell_magic
def append2file(file,cell):
    with open(file,'a') as fd:
        fd.write(cell)
@register_cell_magic
def save2file_calc(file,cell):
    save2file(file,cell)
    code = compile(cell, file, 'exec')
    exec(code, globals())
