% Define symptoms for diseases
disease(flu) :- has(fever), has(cough), has(fatigue).
disease(cold) :- has(runny_nose), has(cough).
disease(covid) :- has(fever), has(cough), has(shortness_of_breath).

% Ask if the patient has a symptom
ask(Symptom) :-
    write('Do you have '), write(Symptom), write('? (yes/no): '),
    read(Response),
    ( Response == yes -> assert(has(Symptom)) ; fail).

% Diagnose the disease based on symptoms
diagnose :-
    ( disease(Disease) -> write('You may have '), write(Disease), nl
    ; write('No diagnosis could be made.'), nl ).

% Start the diagnosis process (renamed to avoid conflict)
start_diagnosis :-
    ask(fever),
    ask(cough),
    ask(fatigue),
    ask(runny_nose),
    ask(shortness_of_breath),
    diagnose.
