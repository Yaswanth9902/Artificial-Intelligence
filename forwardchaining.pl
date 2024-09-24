% Initial facts (known knowledge)
fact(educated(john)).
fact(has_job(john)).

% Rule 1: If someone is educated and has a job, they are a scholar.
rule(scholar(X)) :- fact(educated(X)), fact(has_job(X)).

% Apply forward chaining
apply_rule :-
    rule(NewFact),
    \+ fact(NewFact),  % Check if the fact is not already known
    assert(fact(NewFact)),  % Add the new fact to the knowledge base
    write('Inferred: '), write(NewFact), nl,
    fail.

% Stop when no more facts can be inferred
apply_rule.

% Start the forward chaining process
start :-
    write('Known facts:'), nl,
    list_facts,
    write('Applying forward chaining...'), nl,
    apply_rule,
    write('Final facts:'), nl,
    list_facts.

% Helper function to list all facts
list_facts :-
    fact(F),
    write(F), nl,
    fail.
list_facts.

