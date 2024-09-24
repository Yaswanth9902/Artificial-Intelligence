    sum(0, 0).  % Base case: sum of 0 is 0.
sum(N, Sum) :-
    N > 0,                  % Ensure N is positive
    N1 is N - 1,            % Decrease N by 1
    sum(N1, Sum1),          % Recursive call to find sum of N1
    Sum is N + Sum1.        % Calculate Sum by adding N to the sum of N1
.


