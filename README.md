# fish

## game

Fish is a 6 player memory and strategy game.
There are 2 teams of 3 players. 
The teams compete to win **half suits**, which are sets of 6
cards. In particular, the 9 half suits are

- 2-7 of hearts, spades, diamonds, clubs
- 9-A of hearts, spades, diamonds, clubs
- 8's and jokers

Each round 1 person asks a person from the opposite team a
question of the form "do you have the X of SUIT?" where the
person asking the question **must** have at least 1 card in suit
SUIT.
The person asked responds either "yes" in which case they give
the card to the questioner, and the next round starts with the
questioner still being the questioner, or by responding "no" in
which case the next round starts with the questioned individual
becoming the new questioner.
Note that people are not allowed to lie.

If at any point in the game someone believes that they know that
their team has all the cards in a half suit, and furthermore that
person knows who has which cards of the half suit, that person
can **declare** that their team has that half suit, and say who
has which cards. If they are correct their team wins the half
suit, otherwise the opposing team wins the half suit. 

Once all half suits are claimed, whichever team with more half
suits wins.

## implementation details

## pages

homepage (create/join fish session) 
- create game 
- join game

gamepage (unique)
- shows cards you have
- all the players (whose turn it is and who they are asking => highlighted with different colors)





