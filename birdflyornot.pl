% Declare discontiguous predicates
:- discontiguous can_fly/1.

% Facts about birds
can_fly(eagle).
can_fly(sparrow).
can_fly(parrot).
cannot_fly(ostrich).
cannot_fly(penguin).

% Rule to check if a bird can fly
check_flight(Bird) :-
    ( can_fly(Bird) ->
        write(Bird), write(' can fly.'), nl
    ; cannot_fly(Bird) ->
        write(Bird), write(' cannot fly.'), nl
    ).

% Example queries:
% To check if a specific bird can fly:
% ?- check_flight(eagle).
% ?- check_flight(ostrich).


