# PythonandDragons
## A collection of functions for DND systems!


### install
```
 pip install gonna go here
```

### usage

```python
import PythonandDragons as PaD
```

#### Roll function

```python
#number represents a interger greater then 1

Print(PaD.roll(number))
```
Gives a random number between 1 and number

#### Makechar
```python
PaD.makechar(name, clas, level, race, background, str, dex, con, int, wis, cha, inventorylist, classlist, racelist)
```
name: str name of character

clas: class of character

level: level of character

race: race of character

background: background of character

str: set strength of character; put "no" for the stat to have it generate one using core rules for 5e

dex: set dexterity of character; put "no" for the stat to have it generate one using core rules for 5e

con: set constituion of character; put "no" for the stat to have it generate one using core rules for 5e

int: set intelligence of character; put "no" for the stat to have it generate one using core rules for 5e

wis: set wisdom of character; put "no" for the stat to have it generate one using core rules for 5e

cha: set charisma of character; put "no" for the stat to have it generate one using core rules for 5e

inventorylist: the list that contains the players inventory; make the list blank to have a blank inventory; have the list contain items if you want the character to start with items

classlist: a list of classes that the player can choose

racelist: a list of races that the player can choose

### class player
only use this for manuel setting classes
```python
playername = PaD.player()
```

the class that holds stats for the player
