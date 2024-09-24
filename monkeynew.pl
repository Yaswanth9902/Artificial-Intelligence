% Initial state: (MonkeyLocation, BananaLocation, BoxLocation, MonkeyPosition, HasBanana)
initial_state(state(at_door, at_window, at_middle, on_floor, has_not)).

% Goal state
goal_state(state(_, _, _, _, has)).

% Monkey moves from one location to another
move(state(MonkeyLocation, BananaLocation, BoxLocation, on_floor, has_not),
     state(NewLocation, BananaLocation, BoxLocation, on_floor, has_not)) :-
    MonkeyLocation \= NewLocation,
    write('Monkey moves to '), write(NewLocation), nl.

% Monkey pushes the box to a new location
move(state(MonkeyLocation, BananaLocation, MonkeyLocation, on_floor, has_not),
     state(NewLocation, BananaLocation, NewLocation, on_floor, has_not)) :-
    write('Monkey pushes the box to '), write(NewLocation), nl.

% Monkey climbs on the box
move(state(MonkeyLocation, BananaLocation, MonkeyLocation, on_floor, has_not),
     state(MonkeyLocation, BananaLocation, MonkeyLocation, on_box, has_not)) :-
    write('Monkey climbs on the box'), nl.

% Monkey grabs the banana if on the box and at the same location as the banana
move(state(MonkeyLocation, MonkeyLocation, MonkeyLocation, on_box, has_not),
     state(MonkeyLocation, MonkeyLocation, MonkeyLocation, on_box, has)) :-
    write('Monkey grabs the banana'), nl.

% Solve the problem recursively until the goal is reached
solve(State) :-
    goal_state(State),
    write('Monkey has the banana!'), nl.

solve(State) :-
    move(State, NewState),
    solve(NewState).

% Start solving the problem from the initial state
start :-
    initial_state(InitialState),
    solve(InitialState).
