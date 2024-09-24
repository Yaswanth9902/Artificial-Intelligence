% Graph edges
edge(a, b).
edge(a, c).
edge(b, d).
edge(c, e).
edge(d, f).
edge(e, f).

% Bidirectional edges (to make it undirected)
connected(X, Y) :- edge(X, Y).
connected(X, Y) :- edge(Y, X).

% BFS search
bfs(Start, Goal, Path) :-
    bfs_search([[Start]], Goal, Path).

% BFS helper function
bfs_search([[Goal | Rest] | _], Goal, Path) :-
    reverse([Goal | Rest], Path).

bfs_search([[Node | Rest] | Others], Goal, Path) :-
    findall([Next, Node | Rest],
            (connected(Node, Next), \+ member(Next, [Node | Rest])),
            NewPaths),
    append(Others, NewPaths, Queue),
    bfs_search(Queue, Goal, Path).

% If there are no more nodes to explore and the goal hasn't been found
bfs_search([], _, _) :-
    write('No path found!'), fail.
