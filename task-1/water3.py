def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0]==4 and s[1]==4
    # return (4,4,0)

def successors(s):
    x, y, z = s
   #8l-->5l
    t = 5-y
    if x>0 and t>0:
        if x>t:
            yield ((x-t, y+t, z), t)
        else:
            yield ((0, y+x, z), x)
    #8L-->3L
    t = 3-z
    if x>0 and t>0:
        if x>t:
            yield ((x-t, y, z+t), t)
        else:
            yield ((0, y, z+x), x)
    #5l-->8l
    t = 8-x
    if y>0 and t>0:
        if y>t:
            yield ((x+t, y-t, z), t)
        else:
            yield ((x+y, 0, z), y)
    #5l-->3l
    t = 3-z
    if y>0 and t>0:
        if y>t:
            yield ((x, y-t, z+t), t)
        else:
            yield ((x, 0, z+y), y)
    #3l-->8l
    t = 8-x
    if z>0 and t>0:
        if z>t:
            yield ((x+t, y, z-t), t)
        else:
            yield ((x+z, y, 0), z)
    #3l-->5l
    t = 5-y
    if z>0 and t>0:
        if z>t:
            yield ((x, y+t, z-t), t)
        else:
            yield ((x, y+z, 0), z)
    return []
