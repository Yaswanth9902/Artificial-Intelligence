% Facts
stole(john, car).
stole(mary, bike).
stole(mike, money).

% Rule: A person is a criminal if they stole something.
criminal(X) :- stole(X, _).

% Rule: A person is a suspect if they are a criminal.
suspect(X) :- criminal(X).
