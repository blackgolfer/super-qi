from Color.Calc import foreground
import sys

def latex_palette(palette:list[str])->None:
    name=['primary','secondary','complement','tertiary']
    for (n,c) in zip(name,palette):
        print('\definecolor[named]{'+n+'}{HTML}{'+c[1:]+'}')
    for (n,c) in zip(name,tuple(map(lambda x:foreground(x),palette))):
        print('\definecolor[named]{'+n+'c}{HTML}{'+c[1:]+'}')
        
def latex_palette_file(palette:list[str],filename:str)->None:
    original_stdout = sys.stdout
    with open(filename,'w') as f:
        sys.stdout=f
        latex_palette(palette)
        sys.stdout=original_stdout
        f.close()
    