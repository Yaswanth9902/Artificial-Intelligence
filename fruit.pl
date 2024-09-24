% Define the fruits
fruit(apple).
fruit(banana).
fruit(grape).
fruit(orange).
fruit(lemon).

% Define possible colors for the fruits
color(apple, red).
color(apple, green).
color(banana, yellow).
color(grape, purple).
color(grape, green).
color(orange, orange).
color(lemon, yellow).

% Rule to find the color of a fruit
fruit_color(Fruit, Color) :-
    fruit(Fruit),
    color(Fruit, Color).

% Example query to find color of a specific fruit
find_fruit_color(Fruit) :-
    fruit_color(Fruit, Color),
    write(Fruit), write(' is '), write(Color), nl.
