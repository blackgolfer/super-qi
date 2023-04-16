# Configuration for Fonts and Style

## Fonts
### ttf, otf and ttc
1. Install font file into ~/.local/share/fonts. The installing directory could be any subdirectory but usually   under <font_name>/ttf for ttf fonts, similarly for other types.
2. In shell:
    ```bash
    $ fc-cach -f -v
    ```
### Non-free fonts
1. install getnonfreefonts (https://www.tug.org/fonts/getnonfreefonts/)
    ```bash
    $ wget https://www.tug.org/fonts/getnonfreefonts/install-getnonfreefonts
    $ texlua install-getnonfreefonts
    ```
2. create the binary:
    ```bash
    $ ln -s ln -s /opt/texlive/2022/texmf-dist/scripts/getnonfreefonts/getnonfreefonts.pl ~/.local/bin/getnonfreefonts
    ```
3. install font package, the following is the example to install webomints:
    ```bash
    $ getnonfreefonts webomints
    ```
## cls files
1. Install cls file into ~/texmf/tex/latex. The installing directory could be any subdirectory.
2. In shell:
    ```bash
    $ texhash
    ```