% Facts: planet(Name, DistanceFromSun).
planet('Mercury', 57.9).
planet('Venus', 108.2).
planet('Earth', 149.6).
planet('Mars', 227.9).
planet('Jupiter', 778.3).
planet('Saturn', 1427).
planet('Uranus', 2871).
planet('Neptune', 4497.1).

% Query to get planet information.
get_planet(Name, Distance) :- planet(Name, Distance).
