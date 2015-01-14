
isList([], 1).

isList([H|Tl], X):-Y is X+1,isList(Tl, Y) ; write('Length of the List==> '),write(X).

member(E, []).
member(E, [E|_]).

member(X, [_|Tl]):- member(X, Tl).
