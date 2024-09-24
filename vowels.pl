% Define the vowels
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).

% Base case: An empty list has zero vowels
count_vowels([], 0).

% Recursive case
count_vowels([H|T], Count) :-
    count_vowels(T, CountTail),
    (   vowel(H) -> Count is CountTail + 1
    ;   Count is CountTail).

% Helper predicate to count vowels in a string
count_vowels_string(String, Count) :-
    atom_chars(String, CharList),  % Convert the string to a list of characters
    count_vowels(CharList, Count).
