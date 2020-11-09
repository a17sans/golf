# Golf API

This project aims at creating an API for a simple golf Android app coming soon.

## How does simple golf match works ?

A golf course is composed of several holes (6, 9 first, 9 last, 18).

Among a given course, holes can be sorted by complexity (*the s_index represents its complexity among the course*), and have a given *par* which represents the average number of strikes the players has.

Example of a golf course settings : 

| Hole number | Hole s-index | Hole Par |
| ----------- | ------------ | -------- | 
| 1           | 5            | 3        |
| 2           | 6            | 3        |
| 3           | 2            | 4        |
| 4           | 3            | 4        |
| 5           | 1            | 3        |
| 6           | 4            | 3        |

To know who wins during a match, players have to sum the difference between their actual score and their own par for each hole. The winner is the player with the smallest value (it can be negative, obvioulsy).

## How about handicaps ?

For a 6-hole course, handicaps goes from 0 to 18. 


A player with handicap 1 will have 1 extra strike for the hardest hole of the course (the one with the highest s-index).
A player with handicap 2 will have 2 extra strikes, for the 2 hardest holes.

A new player will be given a handicap of 18, meaning that he has 3 extra strikes for each hole (added to the original par).

For our previous example, this means that : 

| Hole number | Hole s-index | Hole Par | 18-Handicap | 12-Handicap | 15-Handicap |
| ----------- | ------------ | -------- | ----------- | ----------- | ----------- |
| 1           | 5            | 3        | 6           | 5           | 6           | 
| 2           | 6            | 3        | 6           | 5           | 6           | 
| 3           | 2            | 4        | 7           | 6           | 6           | 
| 4           | 3            | 4        | 7           | 6           | 6           | 
| 5           | 1            | 3        | 6           | 5           | 5           | 
| 6           | 4            | 3        | 6           | 5           | 6           | 

 ## Running the program 

 In order to run the API, you may want to follow the steps : 

 ``` 
 cd golf
 virtualenv .virtualenv
 source .virtualenv/bin/activate
 pip install -R requirements.txt
 python src/manage.py runserver 0.0.0.0:8080
 ```

 Then go to `localhost:8080`.