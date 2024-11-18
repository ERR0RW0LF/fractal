import turtle
import numpy as np

t = turtle.Turtle()
shape = [[1,1,1],[1,0,1],[1,1,1]]
# get the size of the shape
height = len(shape)
width = len(shape[0])
details = {'length':600, 'repeats': 3}
speed = 0
t.speed(speed)
positions = {}
t.penup()
t.goto(-details['length']/2, details['length']/2)
t.pendown()
t.hideturtle()

def generate_pattern(shape, rep):
    shape = shape
    zero = [[0,0,0],[0,0,0],[0,0,0]]
    one = shape
    new_shape = []
    for i in range(rep):
        print(shape)
        # new_shape is always 3 times the size of the shape
        new_shape = np.zeros((len(shape)*3,len(shape[0])*3))
        
        # when in the first cell of the shape a 1 present is, the will have a the one shape in the first 3x3 cell of the new shape
        for x in range(len(shape)):
            for y in range(len(shape[0])):
                if shape[x][y] == 1:
                    for n in range(3):
                        for m in range(3):
                            new_shape[n+x*3][m+y*3] = one[n][m]
                else:
                    for n in range(3):
                        for m in range(3):
                            new_shape[n+x*3][m+y*3] = zero[n][m]
        shape = new_shape
    return shape

def draw_square(x,y, size, c:int):
    t.penup()
    t.goto(x,y)
    if c == 1:
        t.color('black')
        t.fillcolor('black')
    else:
        t.color('white')
        t.fillcolor('white')
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()
    #t.forward(size)

'''
1 1 1 1 1 1 1 1 1
1 0 1 1 0 1 1 0 1
1 1 1 1 1 1 1 1 1
1 1 1 0 0 0 1 1 1
1 0 1 0 0 0 1 0 1
1 1 1 0 0 0 1 1 1
1 1 1 1 1 1 1 1 1
1 0 1 1 0 1 1 0 1
1 1 1 1 1 1 1 1 1
'''

def find_square_size(x,y,shape):
    shape_size = len(shape)
    size = 1
    for i in range(1, shape_size):
        if x+i < len(shape) and y+i < len(shape[0]):
            if shape[x+i][y+i] == 1:
                size = i
                break
            
    return size

#draw_square(-100,100, 100)

x = -details['length']/2
y = details['length']/2
length = details['length']
shape = generate_pattern(shape, details['repeats'])
size = length/len(shape)
draw_square(x,y, length, 1)
for i, row in enumerate(shape):
    for j, cell in enumerate(row):
        if cell == 0:
            size_of_square = find_square_size(i,j,shape)
            
            size = length/len(shape)
            # check if the cell is already drawn
            if (i,j) not in positions:
                draw_square(x+j*size, y-i*size, size*size_of_square, 0)
                for n in range(size_of_square):
                    for m in range(size_of_square):
                        positions[(i+n,j+m)] = True
                
            
            




turtle.exitonclick()