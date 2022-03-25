# SEI Capstone Project Proposal

## Project Idea

Megaman Python Network. For this project I am attempting to make a game with
pygame by creating Megaman: Battle Network simulation. The actual game involves a lot of adventure, so this will simply just be a battle simulator to recreate a battle that occurs in the game.

## User Story

While the community is small, this game is for those who enjoy the megaman battle network games and would like to battle with a friend or an NPC.

The users are trying to have a little simple fighting fun without having to travel the gameboy and megaman universe in order to do so


### Key input

The player will use the keyboard in order to move around in both the menu and the battle itself. To start I will just use one player versus and NPC, and then as a post-mvp attempt to add a second player.

| Action             | Key       |
| ------------------ | --------- |
| Move Up            | W         |
| Move Left          | A         |
| Move Right         | D         |
| Move Left          | S         |
| Shoot              | Space Bar |
| Select Menu option | Enter     |

## Character selection

Current plan is just to get one sprite up and running correctly, and then from there try to work in 2 more playable characters.
Characters will use sprites that face in one direction and have a shooting motion.


## Battleground

The battleground for the most part is the same through the games, with eventually some obstacles occuring on a square or two.
For this game I will be using the basic battleground, a 9x9 grid with no obstacles. Possible post-MVP to make obstacles and let player choose different grids, or maybe a randomizer.

![Battleground](https://i.postimg.cc/jjQ0bjpt/MMBN-battleground.png)


## Sound and Music

Probable post-mvp, main focus on getting the battling down first and then i'd like to add the background music and shooting sound effects.


## MVP

| Step                               | Time Estimation |
| ---------------------------------- | --------------- |
| Battleground setup                 | 2 Hours         |
| Sprite Movement                    | 3 Hours         |
| Sprite Shoot action                | 3 Hours         |
| Create NPC (copy of player sprite) | 3 Hours         |
| Create health bars                 | 4 Hours         |
| Create Menu                        | 2 Hours         |

Total Time Approximation for MVP: 17 Hours

## Post MVP

- More characters
- Two player mode
- Sound and music
- Possible in game NPCs to fight
  - Boss fights
- Other battlegrounds
- Chip system


## Deployment

Have instructions in the readme (and will say it aloud when presenting)for installation of pygame and then direct users on how to initiate the game through the terminal.
