#value = [200, 240, 150, 140]
#weight = [1,3, 5, 2]

def func (max_g, weights, values):
    density = []
    heist = 0
    runner = 0
    weigher = 0
    length = len (values)
    for x in range (length):
        if weight == 0:
            density.append (0)
        else:
            density.append (values[x] / weights[x])

    while (runner < length):
        maxi = density[0]
        counter = 0
        for x in range (length):
            if (density[x] > maxi):
                maxi = density[x]
                counter = x
        if (max_g - weigher >= weights[counter]):
            heist += values[counter]
            weigher += weights[counter]
            weights[counter] = 0
            runner += 1
        else:
            print weigher
            heist += (max_g - weigher) * density[counter]
            return heist
        density[counter] = 0
    return heist

print func (5, weight, value)
