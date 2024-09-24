hanoi(1, Source, Target, _) :-
    write('Move disk from '), write(Source), write(' to '), write(Target), nl.

hanoi(N, Source, Target, Aux) :-
    N > 1,
    M is N - 1,
    hanoi(M, Source, Aux, Target),
    hanoi(1, Source, Target, _),
    hanoi(M, Aux, Target, Source).
