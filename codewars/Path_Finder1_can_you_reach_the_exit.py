# true name peremennih
# obishno ya ih tak ne nazivayu

import numpy
import sys

sys.setrecursionlimit(10000)

def estdoroga(fld):
    n, m, flag = len(fld[0]), len(fld), False
    v = [[False for x in range(n)] for y in range(m)]

    for i in range(n):
        for j in range(n):
            if fld[i][j] == 1 and not v[i][j]:
                if naitiput(fld, i, j, v):
                    flag = True
                    break
    return flag

def uperlis(i, j, fld):
    if i >= 0 and i < len(fld) and j >= 0 and j < len(fld[0]): return True
    return False

def naitiput(fld, i, j, v):
    if uperlis(i, j, fld) and fld[i][j] != 0 and not v[i][j]:
        v[i][j] = True
        if fld[i][j] == 2: return True
        up = naitiput(fld, i - 1, j, v)
        if up: return True
        left = naitiput(fld, i, j - 1, v)
        if left: return True
        down = naitiput(fld, i + 1, j, v)
        if down: return True
        right = naitiput(fld, i, j + 1, v)
        if right: return True
            
    return False

def mth(s):
    mat = s.splitlines()
    for subs in range(len(mat)):
        mat[subs] = list(mat[subs])
    return mat

def path_finder(maze):
    if len(maze) <= 2:
        return True
    fn = numpy.array(mth(maze))
    fn = numpy.where(fn == '.', 3, 0)
    fn[0][0] = 1
    n = len(fn[0])
    m = len(fn)
    fn[n - 1][m - 1] = 2
    return estdoroga(fn)