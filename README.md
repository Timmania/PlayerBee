# Player Bee

![alt text](logo.png)

# Bronnen
* https://github.com/OpenTaal/opentaal-wordlist/blob/master/basiswoorden-gekeurd.txt
* https://nl.wiktionary.org/wiki/Categorie:Scheldwoord_in_het_Nederlands
* 

# Description of the project
A short description of the project.
Player Bee, contains a spelling bee game that purposes learning and entertainment while guessing Dutch words.
You will learn how to spell words, expand your vocabulary and push you to go on until you completed the hive.
Player Bee is important for those who will compete in an actual Dutch spelling bee contest or for those who would like to get comfortable with Dutch words.
The game displays a hive with 7 letters, 6 on the outside and 1 in the middle.
The player needs to make (Dutch) words that are at least 4 letters long and contain the middle letter, the letters can be used more than once.
For every 4 word letter that they guess right, they get 1 point.
When the guess has 5 or more letters and it's right, the player gets 1 point for each letter.
The hive will automatically renew when the player guesses all the words in the hive.
Player bee is made by three information science students at the RUG.

#Installation and running
Download or clone the repository into a folder.\
Install the required packages.
```shell script
pip install -r requirements.txt
```
Run the main python script
```shell script
python main.py
```


# Who did what?
Korne Venema did everything that had to with the front end.\
Tim Roorda did the game mechanics\
Huub Exel did everything that had to do with the word list.

All three students did the debugging.
All the three students helped each other with idea's and coding.
We tried to divide the workload as fair as possible among our group.

# Want to cheat?
Run puzzle_solver.py as followed:
```shell script
python puzzle_solver.py middle_letter letter2 letter3 ... letter7
```
It tries to randomly guess a correct word for you.\
This may take a while...\
...\
..\
.
