\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{VictorianBook}[2023/03/26 The Victorian Book Class valpha]

\newif\if@cornerdeco
\@cornerdecofalse
\newif\if@bgimage
\@bgimagefalse

\RequirePackage{xkeyval}
\DeclareOptionX{cimage}[63]{\def\image@corner{#1}\@cornerdecotrue}
\DeclareOptionX{bimage}[images/a4/N-00.png]{\def\image@bg{#1}\@bgimagetrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{book}} % Pass through any options to the base class
%\ProcessOptions\relax % Process given options
\ProcessOptionsX
\LoadClass{book} % Load the base class

%---------------------------------------------------------------------------------------------
% page geometry
%---------------------------------------------------------------------------------------------
\usepackage[left=1.75cm,right=1.75cm,top=2.5cm,bottom=2.5cm,paper=a4paper]{geometry}

%=============================================================================================
% Package Dependencies
%=============================================================================================
%--headers and titles-------------
\RequirePackage{fancyhdr}
\RequirePackage[explicit]{titlesec}
%--background tiling--------------
\RequirePackage{wallpaper}
%-tools for drawing patterns------
\RequirePackage{tikzrput}
\RequirePackage{tikz}
\usetikzlibrary{chains,scopes}
%--ornaments----------------------
\RequirePackage{froufrou}
\RequirePackage{pgfornament}
\RequirePackage{eso-pic}
%--hyper links--------------------
\RequirePackage{hyperref}
%--main fonts---------------------
\RequirePackage{calligra}
\RequirePackage[T1]{fontenc}
%--lettrine-----------------------
\RequirePackage{fontspec}
\RequirePackage{lettrine}
\RequirePackage{GoudyIn}
%---------------------------------

%---------------------------------------------------------------------------------------------
% colors
%---------------------------------------------------------------------------------------------
\definecolor[named]{lightgray}{rgb}{0.75,0.75,0.75}
\definecolor[named]{gray}{rgb}{0.5,0.5,0.5}
\definecolor[named]{coverpagetitlecolor}{rgb}{0.72, 0.53, 0.04}

\definecolor{decocolor}{named}{lightgray}
\definecolor{titlecolor}{named}{gray}

%---------------------------------------------------------------------------------------------
% fonts
%---------------------------------------------------------------------------------------------
\newfontfamily{\titlePageTitleFont}[Extension=.ttf,ExternalLocation=fonts/]{MediciText}
\newfontfamily{\titleFont}{QTLinoscroll}
\def\sectionFont{\titleFont}
\setmainfont{QTGraphLite}

%---------------------------------------------------------------------------------------------
% titles
%---------------------------------------------------------------------------------------------
\titleformat{\chapter}{\filcenter}{}{0ex}{
    \begin{tikzpicture}
        \node[minimum size=4pt,inner sep=0] (A) at (0,0) {\color{titlecolor}\fontsize{29}{23}\sectionFont#1};
        %\coordinate (B) at (8,0);
        {
        [node distance=2pt,inner sep=0,color=decocolor]
        \node[below=1ex of A] (B) {\pgfornament[width=1.25cm]{70}};
        \node[right=of B]  {\pgfornament[width=1.25cm]{70}};
        \node [left=of B] {\pgfornament[width=1.25cm]{70}};
        %\node [on chain] {\pgfornament[width=1cm]{70}};
        }
    \end{tikzpicture}
}
\titleformat{\section}[block]
{\Large}
%{\color{titlecolor}\MakeUppercase{\roman{section}\hskip 1ex}}
{}
{0pt}
{\color{titlecolor}\sectionFont#1}

\newcommand{\chapterend}{
    {\color{decocolor}\froufrou[fleuron]}
}
\newcommand{\introend}{
    {
            \color{decocolor}\froufrou[
                \pgfornament[height=0.1cm]{87}
                \pgfornament[height=0.1cm]{87}
                \pgfornament[height=0.1cm]{87}
            ]
        }
}

%---------------------------------------------------------------------------------------------
% page decorations
%---------------------------------------------------------------------------------------------
\newcommand\AtPageUpperRight[1]{\AtPageUpperLeft{%
        \put(\LenToUnit{\paperwidth},\LenToUnit{0\paperheight}){#1}%
    }}%
\newcommand\AtPageLowerRight[1]{\AtPageLowerLeft{%
        \put(\LenToUnit{\paperwidth},\LenToUnit{0\paperheight}){#1}%
    }}%
\makeatletter
\if@cornerdeco
\AddToShipoutPicture{%
  \begingroup
    \def\@mydima{2}%
    \def\@mydimb{17}%
    \def\@mydimc{30}%
    \AtPageUpperLeft{\put(\@mydima,-\@mydimb){\pgfornament[color=decocolor,width=1cm]{\image@corner}}}
    \AtPageUpperRight{\put(-\@mydimc,-\@mydimb){\pgfornament[color=decocolor,width=1cm,symmetry=v]{\image@corner}}}
    \AtPageLowerLeft{\put(\@mydima,\@mydimb){\pgfornament[color=decocolor,width=1cm,symmetry=h]{\image@corner}}}
    \AtPageLowerRight{\put(-\@mydimc,\@mydimb){\pgfornament[color=decocolor,width=1cm,symmetry=c]{\image@corner}}}
  \endgroup
}
\fi
\if@bgimage
\TileWallPaper{1cm}{1cm}{\image@bg}% 
\fi
\makeatother

%---------------------------------------------------------------------------------------------
% droppedcaps
%---------------------------------------------------------------------------------------------
\def\Drop {\DroppedCaps
  {} {Sans} {3\baselineskip}
  {2pt} {1\baselineskip} {2}}
\def\chap#1/#2/{\Drop #1{\sc#2}}

%---------------------------------------------------------------------------------------------
% initial and lettrine
%---------------------------------------------------------------------------------------------
\renewcommand{\LettrineFontHook}{\color{titlecolor}\GoudyInfamily{}}
\LettrineTextFont{\titleFont}
\setcounter{DefaultLines}{3}
\setlength{\DefaultNindent}{0pt}
\setlength{\DefaultFindent}{1pt}

%---------------------------------------------------------------------------------------------
% hyperref
%---------------------------------------------------------------------------------------------
\hypersetup{
    colorlinks,
    citecolor=titlecolor,
    filecolor=titlecolor,
    linkcolor=titlecolor,
    urlcolor=titlecolor
}

%---------------------------------------------------------------------------------------------
% title page
%---------------------------------------------------------------------------------------------
\renewcommand{\titlepage}[3]{
	\thispagestyle{empty} % Suppress headers and footers on the title page

	\begin{tikzpicture}[remember picture, overlay]
		\node [inner sep=0pt] at (current page.center) {#1}; % Background image
		%\node [anchor=west, inner sep=0pt, rectangle, fill=#3, fill opacity=0.4] at (current page.center) {};
    \node[anchor=west,inner sep=0pt, rectangle, fill=#3, fill opacity=0.2,
      text opacity=1, minimum height=0.2\paperheight, minimum width=.52\paperwidth, 
      text width=0.52\paperwidth,text centered,] at (current page.west) {#2}; % Title highlight box with title(s) and author(s)
	\end{tikzpicture}
	
	\newpage
}
