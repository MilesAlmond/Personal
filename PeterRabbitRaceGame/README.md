This is a project I undertook to find out who the best character was in the Peter Rabbit Race Game, a game created in 1917 by Beatrix Potter, that has a concept similar to snakes and ladders, but with four different characters all on their own paths.
I did this by simulating the 10,000,000 games of each character, counting their amount of turns, and comparing these to each other.

NOTE: This project is still currently underway, and so the code is messy and lacks comments in some areas. The plan for this project is to eventually incorporate it into a Communicating Maths module at university, where I will create a video around the background and analysis of this project.

# Board

I made the board as both a visual aid and as a way to debug issues and check that the game was carrying out in the way that I had intended:

![Board](https://user-images.githubusercontent.com/80479216/154105632-cd8b0215-3279-4be6-bdc4-744faa1c8f0a.png)

# Console Readout

Print statements allowed me to see the rolls and positions at each point as the program ran:

![Console Readout](https://user-images.githubusercontent.com/80479216/154106138-5cc9e107-4afd-491d-bd79-7ac6d2fb6d71.png)

# Results

Preliminary results suggest that Jeremy Fisher is a few moves slower than the other characters on average, with Peter Rabbit having a very slight lead overall.

## Histograms

These are the histograms for the number of rolls for each character, with 0.025, 0.5, and 0.975 quantiles:

![Histograms for Each Character (with 0.025,0.5,and0.975 quantiles)](https://user-images.githubusercontent.com/80479216/154103797-787a8f05-c0c0-49ea-87c0-c93d2a7f69cb.png)

## Winning Probabilities

These are the winning probabilities for each character:

![Winning Probabilities for Each Character](https://user-images.githubusercontent.com/80479216/154101903-af0cdf95-003f-4e08-9e1d-19d12642f224.png)
