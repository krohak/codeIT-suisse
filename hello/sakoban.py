from array import array
from collections import deque
#import psyco
global data, nrows, sdata, ddata, px, py
data = []
nrows = 0
px = py = 0
sdata = ""
ddata = ""

def init(board):

    data = filter(None, board.splitlines())
    nrows = max(len(r) for r in data)

    maps = {' ':' ', '.': '.', '@':' ', '#':'#', '$':' '}
    mapd = {' ':' ', '.': ' ', '@':'@', '#':' ', '$':'*'}

    for r, row in enumerate(data):
        for c, ch in enumerate(row):
            sdata += maps[ch]
            ddata += mapd[ch]
            if ch == '@':
                px = c
                py = r

def push(x, y, dx, dy, data):
    if sdata[(y+2*dy) * nrows + x+2*dx] == '#' or \
       data[(y+2*dy) * nrows + x+2*dx] != ' ':
        return None

    data2 = array("c", data)
    data2[y * nrows + x] = ' '
    data2[(y+dy) * nrows + x+dx] = '@'
    data2[(y+2*dy) * nrows + x+2*dx] = '*'
    return data2.tostring()

def is_solved(data):
    for i in xrange(len(data)):
        if (sdata[i] == '.') != (data[i] == '*'):
            return False
    return True

def solve():
    openn = deque([(ddata, "", px, py)])
    visited = set([ddata])
    dirs = ((0, -1, 'u', 'U'), ( 1, 0, 'r', 'R'),
            (0,  1, 'd', 'D'), (-1, 0, 'l', 'L'))

    lnrows = nrows
    while openn:
        cur, csol, x, y = openn.popleft()
        print(cur)

        for di in dirs:
            temp = cur
            dx, dy = di[0], di[1]
            legit=((y+dy) * lnrows )+ x+dx
            if (temp[legit] == '*'):
                temp = push(x, y, dx, dy, temp)
                if temp and temp not in visited:
                    if is_solved(temp):
                        return csol + di[3]
                    openn.append((temp, csol + di[3], x+dx, y+dy))
                    visited.add(temp)
            else:
                if sdata[(y+dy) * lnrows + x+dx] == '#' or \
                   temp[(y+dy) * lnrows + x+dx] != ' ':
                    continue

                data2 = array("c", temp)
                data2[y * lnrows + x] = ' '
                data2[(y+dy) * lnrows + x+dx] = '@'
                temp = data2.tostring()

                if temp not in visited:
                    if is_solved(temp):
                        return csol + di[2]
                    openn.append((temp, csol + di[2], x+dx, y+dy))
                    visited.add(temp)

    return "No solution"


level = """\
#######
#     #
#     #
#. #  #
#. $$ #
#.$$  #
#.#  @#
#######"""

#psyco.full()
init(level)
print(solve())
