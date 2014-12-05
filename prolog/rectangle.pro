
/* rectangle Outline 20 by 10*/

rectangle:- rectanglewidth(0).
rectanglewidth(10).
rectanglelength(20).
rectanglelength2(20).

rectanglelength(Y):- write('*'), X is Y+1, rectanglelength(X).

rectanglelength2(Y):-(((Y is 0; Y is 19),write('*')) ; ((Y >0, Y<19), write(' '))), X is Y+1, rectanglelength2(X).

rectanglewidth(Y):- (((Y>0, Y<9), rectanglelength2(0)) ; rectanglelength(0)),  nl, X is Y+1, rectanglewidth(X). 
