% Facts defining family relationships
parent(john, mary).
parent(john, robert).
parent(mary, alice).
parent(mary, charles).
parent(robert, david).

% Define gender
male(john).
male(robert).
male(charles).
male(david).
female(mary).
female(alice).

% Rule to check if X is a parent of Y
is_parent(X, Y) :- parent(X, Y).

% Rule to find siblings
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% Rule to find grandparents
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

% Example queries:
% ?- is_parent(john, mary).
% ?- sibling(alice, charles).
% ?- grandparent(john, david).
