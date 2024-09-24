% Facts: name(Name, DOB).
name('John Doe', '1990-05-15').
name('Alice Smith', '1985-07-22').
name('Bob Johnson', '2000-11-03').
name('Emily Davis', '1995-02-10').

% Query to get the DOB of a person by name.
get_dob(Name, DOB) :- name(Name, DOB).

% Query to find people born on a specific date.
get_name_by_dob(DOB, Name) :- name(Name, DOB).
