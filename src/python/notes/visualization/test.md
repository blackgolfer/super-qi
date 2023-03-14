beginfig(1);
draw (-u,-u)--(11u,-u)--(11u,u)--(-u,u)
--cycle; % bounding box
pickup pencircle scaled 1/2u;
for i=0 upto 10:
  draw (i*u,0) withcolor i*0.1*white;
endfor;
endfig;

end;