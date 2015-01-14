/* My Program to print stars  Dennis Banga P15/1475/2012 */

/* to run, type triangle */

triangle:- trianglewidth(0). 
/*predicates*/
trianglewidth(10).
trianglelength(19).
trianglelength(19, CurrentLine).

/*for printing the last line of the triangle */

trianglelength(Y):-write('*'), X is Y+1, trianglelength(X).

/* for printing the outline of the triangle */
trianglelength(Y, CurrentLine):-check(Y, CurrentLine),
				 X is Y+1, trianglelength(X, CurrentLine).

check(Y, CurrentLine):-(Y is 9-CurrentLine ; Y is 9+CurrentLine), write('*') ; write(' ').

/*loop to print the 10 lines of the triangle*/
trianglewidth(Y):-(((Y<9), trianglelength(0, Y)) ; trianglelength(0)), 
		X is Y+1,nl, trianglewidth(X). 
