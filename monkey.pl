% Initial state: monkey is in room1 with a banana and a box
initial_state(state(monkey, room1, [banana, box])).

% Goal state: monkey has the banana
goal_state(state(monkey, room1, [banana])).

% Define moves
move(state(monkey, room1, Objects), state(monkey, room1, NewObjects)) :-
    select(banana, Objects, NewObjects),
    write('Monkey grabs the banana.'), nl.

move(state(monkey, room1, Objects), state(monkey, room2, Objects)) :-
    write('Monkey moves to room2.'), nl.

move(state(monkey, room2, Objects), state(monkey, room1, Objects)) :-
    write('Monkey moves back to room1.'), nl.

% Solve the problem
solve(State) :-
    goal_state(Goal),
    solve(State, Goal).

solve(State, Goal) :-
    State = Goal,
    write('Goal reached: '), write(State), nl.
solve(State, Goal) :-
    move(State, NewState),
    solve(NewState, Goal).

% Example query to start solving the problem:
% ?- initial_state(Initial), solve(Initial).
