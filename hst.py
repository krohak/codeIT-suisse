max_g=3
weights=[1,3,5,2]
values=[200,220,150,140]

def func_two (max_g, weights, values):

    density = []

    heist2 = 0

    runner = 0

    weigher = 0

    length = len (values)

    for x in range (length):

        if weights[x] == 0:

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

            heist2 += values[counter]

            weigher += weights[counter]

            weights[counter] = 0

            runner += 1

        else:

            heist2 += (max_g - weigher) * density[counter]

            return heist2

        density[counter] = 0

    return heist2





print(func_two(max_g,weights,values))
