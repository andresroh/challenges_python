# The Snake — Area Filling

# This challenge is based on the classic videogame "Snake".

# Assume the game screen is an n * n square, and the snake starts the game with length 1 
# (i.e. just the head) positioned on the top left corner.

# For example, if n = 7 the game looks something like this:

# 1 0 0 0 0 0 0       0 1 0 0 0 0 0
# 0 0 0 0 0 0 0       0 0 0 0 0 0 0
# 0 0 0 0 0 0 0       0 0 0 0 0 0 0
# 0 0 0 0 0 0 0       0 0 0 0 0 0 0
# 0 0 0 0 0 0 0       0 0 0 0 0 0 0
# 0 0 0 0 0 0 0       0 0 0 0 0 0 0

# beginning           fist move

# In this version of the game, the length of the snake doubles each time it eats food 
# (e.g. if the length is 4, after eating it becomes 8).

# Create a function that takes the side n of the game screen and returns the number of 
# times the snake can eat before it runs out of space in the game screen.

# Examples
# snakefill(3) ➞ 3

# snakefill(6) ➞ 5

# snakefill(24) ➞ 9

# Notes
# The given number will always be a positive integer (there are no exceptions to handle)

def snakefill(n):
    mtx = n*n
    snk_len = 1
    times = 0
    while mtx//snk_len > 1:
        snk_len += snk_len
        times += 1
    return times


if __name__ == '__main__':
    print(snakefill(3))
    print(snakefill(6))
    print(snakefill(24))