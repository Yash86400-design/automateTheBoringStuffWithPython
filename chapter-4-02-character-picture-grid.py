def pictureGridPrint(givenArray):
    arrayLength = len(givenArray)
    # In our case differenceInnerArrayLength it's 3, in other case it can be 10-11-12, whatever you know.
    differenceInnerArrayLength = len(givenArray) - len(givenArray[0])
    for row in range(0, arrayLength-differenceInnerArrayLength):
        for column in range(0, arrayLength):
            print(givenArray[column][row], end="")
        print("\n", end="")


grid = ([['.', '.', '.', '.', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['.', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.']])

# print(grid[1][2])

pictureGridPrint(grid)
