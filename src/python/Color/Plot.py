import seaborn as sns
import matplotlib.pyplot as plt
from numpy.typing import ArrayLike

def plot_palette(palette:list[str])->None:
    sns.palplot(sns.color_palette(palette))

def hsv_imshow(img:ArrayLike,**kwargs)->None:
    plt.axis('off')
    plt.hsv()
    plt.imshow(img,**kwargs)