Tikz examples
=============

Basic examples
--------------

.. tikz:: [>=latex',dotted,thick] \draw[->] (0,0) -- (1,1) -- (1,0)
   -- (2,0);
   :libs: arrows


.. tikz:: An Example TikZ Directive with Caption
   :align: left

   \draw[thick,rounded corners=8pt]
   (0,0)--(0,2)--(1,3.25)--(2,2)--(2,0)--(0,2)--(2,2)--(0,0)--(2,0);

An example role :tikz:`[thick] \node[blue,draw] (a) {A};
\node[draw,dotted,right of=a] {B} edge[<-] (a);`

An example role :tikz:`[blue,thick] \node[draw] (a) {A}; \node[draw,dotted,right of=a] {B} edge[<-] (a);`

Example of a Tikz picture included from a file:

.. tikz::
   :include: example.tikz
   :align: right


A control loop example
----------------------

.. rst-class:: centered
.. tikz:: Control system principles (PGF/TikZ example)
   :include: ctrloop.tikz
   :libs: arrows,shapes

State diagrams
--------------

.. rst-class:: centered
.. tikz:: Finite state is always empty
   :include: fsm.tikz
   :libs: arrows,automata