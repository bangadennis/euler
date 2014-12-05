/* My Program to print stars  Dennis Banga P15/1475/2012 */

/* to run, type triangle */

triangle:- trianglewidth(0). 
/*predicates*/
trianglewidth(10).
trianglelength(19, CurrentLine).
trianglelength2(19, CurrentLine).

/*for printing the last line of the triangle */
trianglelength(Y, CurrentLine):- ((CurrentLine is 9,write('*')) ; write(' ')) , X is Y+1, trianglelength(X, CurrentLine).

/* for printing the outline of the triangle */
trianglelength2(Y, CurrentLine):- (((Y is 9-CurrentLine ; Y is 9+CurrentLine ),write('*')) ; write(' ')), X is Y+1, trianglelength2(X, CurrentLine).

/*loop to print the 10 lines of the triangle*/
trianglewidth(Y):- (((Y<9), trianglelength2(0, Y)) ; trianglelength(0, Y)),  nl, X is Y+1, trianglewidth(X). 
