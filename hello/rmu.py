def digits (num):
    digits = 0
    if(num == 1):
        return 0
    while (num > 0):
        num =  int(num /10)
        digits = digits+ 1
    return digits

def func_four(sentence):
    counter = 0
    size = 0
    current = sentence[0]
    for x in sentence:
        if(x == current):
            counter = counter + 1
        else:
            current = x
            size = size + 8
            size = size + (8 * (digits (counter)))
            counter = 1

    size = size+ 8
    size = size + (8 * (digits (counter)))
    return size



print(func_four("RRRRRRTTTTYYYULLL"))



next_time=datetime.datetime.strptime('29-05-2017 13:50:00.000+0800','%d-%m-%Y %H:%M:%S.%f%z')
next_time2=datetime.datetime.strptime('29-05-2017 13:00:00.000+0800','%d-%m-%Y %H:%M:%S.%f%z')

a=next_time-next_time2
a.total_seconds()
