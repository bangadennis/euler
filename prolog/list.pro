
start:-isList([1,2,3,4,5,4,5,5], 1).

isList([H|Tl], X):-Y is X+1,isList(Tl, Y) ; write('Length of the List==> '),write(X).
