% Facts
animal(dog).
animal(cat).
animal(bird).
has_legs(dog, 4).
has_legs(cat, 4).
has_legs(bird, 2).

% Pattern matching to check if an animal has a specific number of legs
legs(X, N) :- animal(X), has_legs(X, N).

% Find animals with a specific number of legs
find_animals_with_legs(N, Animal) :-
    legs(Animal, N).
