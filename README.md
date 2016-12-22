# RushHour
to choose a board to run change the index on line 37 (games[X]) to the board you wish to run
	index 0 is our testing board
	1/7 are the cases
	extra boards can be added by adding a board (list of lists) to the list.
		in this list of lists of the board each list represents a 

calculate: boolean, if true the algorithem wil be run
		if false a predetermined path will be simulated (see path_sim)

path_sim allows you to paste a known pathway.
	adding the code: simulation(0.5, Board(game, orientation[0], orientation[1])) at the end of the file will run the simulation of 	that pathway

global variables:
	algorithem for choosing the algorithem to run
	loops, allow the setting of attempts at random search
	limit, the limit for the depth limited

