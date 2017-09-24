import json
import math
from array import array

def horse1(fullobject):

    data = fullobject['data']
    horse_dic = {}
    trainer_dic = {}
    jockey_dic = {}
    placings ={}

    points = [7, 3 ,1]

    for jsonob in data:
        place_val = int(jsonob['Placing'])


        if( place_val == 1 or place_val == 2 or place_val == 3):
            add_points('Horse', jsonob, horse_dic, points[place_val-1])
            add_points('Trainer', jsonob, trainer_dic, points[place_val-1] )
            add_points('jockey_code', jsonob, jockey_dic, points[place_val-1])

        #print(horse_dic)
        #print(trainer_dic)
        #print(jockey_dic)

    result = { "q1": {},
    "q2": {"horse": max(horse_dic, key=horse_dic.get),
    "jockey": max(jockey_dic, key=jockey_dic.get),
    "trainer": max(trainer_dic, key=trainer_dic.get)
    },
    'q3':{}}

    print(result)

def horse3(fullobject):

    data = fullobject['data']
    result = array('i')
    for jsonob in data:
        result.append(1)
    print(result)

'''
    data = { 'a' : [1,2], 'b': [3,4]}

    for (key, values) in data.items():
        print(values)

    races = [5]
    races[0] = 1
    print(races)

    data = fullobject['data']
    for jsonob in data:
        races[0] = 1
    print(races)
'''


def add_points(str, jsonob, dic, place_value):

    if( jsonob[str] in dic):
        dic[jsonob[str]]+=place_value
    else:
        dic[jsonob[str]]=place_value


data1 = {"info":"xyz",
"data": [{
"RaceIndex": "RACE 4 (411)",
"Placing": "3","Track": "ALL WEATHER TRACK",
"Course": "ALL WEATHER TRACK",
"Dist": "Class 3 - 1650M - (80-60)",
"RaceClass": "Class 3 - 1650M - (80-60)",
"Going": "GOOD","Horse": "SILLY BUDDIES(S054)",
"Draw": "14",
"Rtg": "5",
"Trainer": "C W Chang",
"jockey_code": "Me",
"raceno": "1"
},
{
"RaceIndex": "RACE 4 (411)",
"Placing": "1","Track": "ALL WEATHER TRACK",
"Course": "ALL WEATHER TRACK",
"Dist": "Class 3 - 1650M - (80-60)",
"RaceClass": "Class 3 - 1650M - (80-60)",
"Going": "GOOD","Horse": "Sagar BUDDIES(S054)",
"Draw": "14",
"Rtg": "5",
"Trainer": "Wang",
"jockey_code": "You",
"raceno": "2"
},
{
"RaceIndex": "RACE 4 (411)",
"Placing": "3","Track": "ALL WEATHER TRACK",
"Course": "ALL WEATHER TRACK",
"Dist": "Class 3 - 1650M - (80-60)",
"RaceClass": "Class 3 - 1650M - (80-60)",
"Going": "GOOD","Horse": "Sagar BUDDIES(S054)",
"Draw": "14",
"Rtg": "5",
"Trainer": "Wang",
"jockey_code": "Me",
"raceno":"1"
}
]
}

horse3(data1)
