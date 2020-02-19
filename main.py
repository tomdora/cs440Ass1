# Thomas Fiorilla
# Main file to execute the code.
# This version is made for Python 3; mainAT.py is for Python 2.

import board				# import code for creating the board
import draw					# import code for visually displaying the board on screen
import evaluate				# import code for bfs
import hill					# import code for hill-climbing

def main():
	userInput = input("Enter 5 or greater for a board of that size, or 0 to randomize the board. ")
	
	gameBoard = board.Board(userInput)											# builds a Board() object and assigns it to gameBoard
	
	bfs = evaluate.evaluate(gameBoard.boardBuilt, gameBoard.boardSize)		# creates the bfs object for the original board
	hillBoard = hill.Hill(gameBoard)										# creates a hill-climbing object with the original board
	
	print("Score for the board: " + str(bfs.value) + "; time for BFS (ms): " + str(bfs.evalTime))			# prints the score for the original board
	
	# create a loop for user input to make selections to view the original board, etc
	while True:
		print()
		userInput = input("Type '1' for the original board, '2' for number of steps on original board, '3' to implement Hill Climbing, '4' to view the Hill Board, '5' to view steps on Hill Board, 'q' to exit. ")
		
		if userInput == '1':
			draw.drawBoard(gameBoard.boardBuilt, gameBoard.boardSize)			# takes the created board and draws it with turtle, as visual output
			print("> Original game board displayed.")
		
		elif userInput == '2':
			draw.drawBoard(bfs.steps, gameBoard.boardSize)						# uses the draw module 
			print("> Number of steps to reach a tile displayed.")
		
		elif userInput == '3':
			userInput = int(input("> How many iterations would you like the hill-climbing to try? "))
			
			while userInput < 0:
				userInput = input("> How many iterations would you like the hill-climbing to try? ")
			
			hillBoard.climb(userInput)
			
			print("> New board score: " + str(hillBoard.score) + "; time for hill-climb (ms): " + str(hillBoard.evalTime))
		
		elif userInput == '4':
			draw.drawBoard(hillBoard.puzzle.boardBuilt, gameBoard.boardSize)			# takes the created board and draws it with turtle, as visual output
			print("> Hill-CLimbing game board displayed.")
		
		elif userInput == '5':
			hillBFS = evaluate.evaluate(hillBoard.puzzle.boardBuilt, hillBoard.puzzle.boardSize)			# creates a new bfs object for the hill-climbing board
			draw.drawBoard(hillBFS.steps, hillBoard.puzzle.boardSize)
			print("> Hill-Climbing board number of steps displayed")
		
		elif userInput == 'q':
			break



if __name__ == "__main__":
	main()
