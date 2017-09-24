#import s1
import requests
import s1

level = """\
xxx*xxxx
xxxoxxxx
xxxb o*x
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx"""

level = """\
xxxxxxxx
xxx*xxxx
xxx xxxx
xxxo o*x
x*ob  xx
xxxxo xx
xxxx*xxx
xxxxxxxx"""



'''
["xx---xxx",
 "xx-*-xxx",
 "xx- ----",
 "---o o*-",
 "-*ob  --",
 "----o --",
 "xxx-*-xx",
 "xxx---xx"]
 '''

@csrf_exempt
def wde(request):
	if request.method == 'POST':
		print(str(request.body))
		a=json.loads((request.body))
		map_1=a['map']
        level=a["level"]
        id_1=a["id"]
        map_1=format(map_1)
        s1.init(map_1)
        commands=[s1.solve()]

        requests.post("cis2017-warehouse-keeper.herokuapp.com/reset?run_id=%s")%(id_1)

        for i,com in enumerate(commands):
            requests.post("cis2017-warehouse-keeper.herokuapp.com/move/%s?run_id=%s")%(com,id_1)
            if(i=len(commands)-1):


        return HttpResponse((sen))





def format(map_1):
    string=""
    length=0
    padding=""
    for i,row in enumerate(map_1):
        #print(row)
        length=len(row)
        row=row.replace("-","x")
        string=string+'\n'+row

    for x in range(length):
        padding+='x'

    pad=8
    while(pad-len(map_1)>0):
        string=string+'\n'+padding
        pad-=1

    return(string)


s1.init(level)
print (s1.solve())
