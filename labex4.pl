%Propositions in item 1
female(scarlet).
female(peacock).
female(orchid).
female(white).

%Proposition in item 2
male(plum).
male(mustard).
male(green).

%Proposition in item 3
hates(scarlet, green).

%Proposition in item 4
hates(green, scarlet).

%Proposition in item 5
hates(plum, white).
hates(white, plum).

%Proposition in item 6
hates(mustard,X) :- female(X).
hates(mustard,plum).

%Proposition in item 7
likes(scarlet,orchid).
likes(peacock,orchid).

%Proposition in item 8
likes(orchid,peacock).

%Proposition in item 9
likes(scarlet,white).

%Proposition in item 10
likes(scarlet,plum).
likes(plum,scarlet).

%Proposition in item 11
likes(plum,X) :- hates(mustard,X).

%Proposition in item 12
enemies(X,Y) :- hates(X,Y), hates(Y,X).

%Proposition in item 13
friends(X,Y) :- likes(X,Y), likes(Y,X).

%Proposition in item 14
friends(X,Y) :- enemies(X,Z), enemies(Z,Y).