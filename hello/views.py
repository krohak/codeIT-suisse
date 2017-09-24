from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import requests
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

import json
import math
import datetime
import pytz
import numpy as np
from collections import OrderedDict
import re
#import two

'''
from snippets.serializers import SnippetSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
'''

# Create your views here.
def index(request):
	test = 5
	r = requests.get('http://httpbin.org/status/418')
	print(r.text)
	print("hi")
	return HttpResponse('<pre>' + r.text + '</pre>')

@csrf_exempt
def db(request):
	if request.method == 'POST':
		greeting = Greeting()
		greeting.save()
		greetings = Greeting.objects.all()




@csrf_exempt
def sort(request):
	if request.method == 'POST':
		#tickets={"sagar":"rohak"}
		#return HttpResponse(str("Content-Type: application/json")+str(request.body))
		#a=str(request.body).replace('"'," ").replace(","," ").replace("'"," ").replace("["," ").replace("]"," ").replace("b"," ").split(" ")
		a=json.loads((request.body))
		#a=''.join(c for c in str(request.body) if c.isdigit())
		#quickSort(a)
		a=np.array(a)
		a=np.sort(a,kind='heapsort')
		print(a)
		return HttpResponse(str(a.tolist()))

@csrf_exempt
def horse(request):
	if request.method == 'POST':

		return HttpResponse(json.dumps(horse1(request.body)))


@csrf_exempt
def heist(request):
	if request.method == 'POST':
		weights=[]
		values=[]
		print(str(request.body))
		a=json.loads((request.body))
		#a=''.join(c for c in str(request.body) if c.isdigit())
		max_val=a['maxWeight']
		val=a['vault']
		for e in val:
			values.append((e['weight'],e['value']))

			#weights.append(e['weight'])
			#values.append(e['value'])

		#quickSort(a)
		#print(val)
		#print("weights"+str(weights))
		#print("value"+str(values))
		data = {}
		data["heist"] =  (hst(max_val,values))
		#print(str(data))
		return HttpResponse(json.dumps(data))



@csrf_exempt
def rle(request):
	if request.method == 'POST':
		print(str(request.body))
		a=json.loads((request.body))
		sen=a['data']
		return HttpResponse(func_four(sen))

@csrf_exempt
def lzw(request):
	if request.method == 'POST':
		print(str(request.body))
		a=json.loads((request.body))
		sen=a['data']
		return HttpResponse(compress(sen))

@csrf_exempt
def wde(request):
	if request.method == 'POST':
		print(str(request.body))
		a=json.loads((request.body))
		sen=a['data']
		return HttpResponse(string_third(sen))

@csrf_exempt
def plan(request):
	if request.method == 'POST':
		print(str(request.body))
		l=json.loads((request.body))

		destination=l["destination"]
		node_dict=OrderedDict()
		edge_list=[]


		for i,node in enumerate(l["stations"]):
		    name=""
		    node_dict[node["name"]]=(i,node["passengers"])


		for i,node in enumerate(l["stations"]):
		    name=node["name"]
		    for connections in node["connections"]:
		        edge_list.append((name,connections["station"],connections["line"]))


		print(node_dict)
		print(edge_list)
		print(destination)

		arr=func_2(node_dict,edge_list,destination,func_1(node_dict,edge_list,destination))
		out={ "line": str(arr[0]), "totalNumOfPassengers": arr[1], "reachingVia": str(arr[2]) }
		return HttpResponse(json.dumps(out))

@csrf_exempt
def cal(request):
	if request.method == 'POST':
		print(str(request.body))
		a=json.loads((request.body))
		container=a['container']
		typ=0

		try:
			ele=a['rectangle']
			typ=1

		except Exception as e:
			print(e)
			try:
				ele=a['square']
				typ=2

			except Exception as e:
				print(e)
				try:
					ele=a['circle']
					typ=3

				except Exception as e:
					print(e)

		cont=[]
		data=[]

		cont.append(container["coordinate"]["X"])
		cont.append(container["coordinate"]["Y"])
		cont.append(container["width"])
		cont.append(container["height"])

		if (typ==1):
			data.append(ele["coordinate"]["X"])
			data.append(ele["coordinate"]["Y"])
			data.append(ele["width"])
			data.append(ele["height"])
		elif (typ==2):
			data.append(ele["coordinate"]["X"])
			data.append(ele["coordinate"]["Y"])
			data.append(ele["width"])
		elif (typ==3):
			data.append(ele["center"]["X"])
			data.append(ele["center"]["Y"])
			data.append(ele["radius"])


		#return HttpResponse(str(cont)+str(data))
		pi = math.pi
		return HttpResponse(str(func_r(cont,typ, data, pi)))

@csrf_exempt
def schedx(request):
	if request.method == 'POST':
		print(str(request.body))
		a=json.loads(request.body)

		ele=a[0].split(";")
		ran=ele[0]
		t1=ele[1]
		t2=ele[2]
		try:
		    next_time=datetime.datetime.strptime(t1,'%d-%m-%Y %H:%M:%S.%f%z')
		    next_time2=datetime.datetime.strptime(t2,'%d-%m-%Y %H:%M:%S.%f%z')
		except Exception as e:
			next_time=datetime.datetime.strptime(t1,'%d-%m-%Y %H:%M:%S.%fZ')
			next_time2=datetime.datetime.strptime(t2,'%d-%m-%Y %H:%M:%S.%fZ')
			next_time=pytz.utc.localize(next_time)
			next_time2=pytz.utc.localize(next_time2)

		a1=next_time2-next_time
		a1=a1.total_seconds()

		time_durations=[]
		for i in range(int(ran)):
		    #print(i+1)
		    #print(a[i+1])
		    details=a[i+1].split(";")
		    try:
		        time_now1=datetime.datetime.strptime(details[1],'%d-%m-%Y %H:%M:%S.%f%z')
		        time_now2=datetime.datetime.strptime(details[2],'%d-%m-%Y %H:%M:%S.%f%z')
		    except Exception as e:
		        #print(e)
		        time_now1=datetime.datetime.strptime(details[1],'%d-%m-%Y %H:%M:%S.%fZ')
		        time_now2=datetime.datetime.strptime(details[2],'%d-%m-%Y %H:%M:%S.%fZ')
		        time_now1=pytz.utc.localize(time_now1)
		        time_now2=pytz.utc.localize(time_now2)
		        #print(time_now1)
		    time_tup=(((time_now1-next_time).total_seconds()),((time_now2-next_time).total_seconds()))
		    time_durations.append(time_tup)

		flag=0
		for (times1,times2) in time_durations:
			if(times1<0 and times2<0):
				flag=0
			else:
				flag=1
		if flag==1:
			result=func_r_2(a1,time_durations)
		else:
			result=a1
		return HttpResponse('"'+str(int(result))+'"')


@csrf_exempt
def ware(request):
	if request.method == 'POST':
		print(str(request.body))
		a=json.loads(request.body)
		map_1=a["map"]
		level=a["level"]
		id_1=a["run_id"]
		print(map_1,level,id_1)
		requests.post("cis2017-warehouse-keeper.herokuapp.com/reset?run_id=%s")%(id_1)

		for i,com in enumerate(commands):
			requests.post("cis2017-warehouse-keeper.herokuapp.com/move/%s?run_id=%s")%(com,id_1)
		return HttpResponse("hi")






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

def list_max (a_list):
    maxi = a_list[0]
    for x in a_list:
        if maxi < x:
            maxi = x
    return maxi

def func_hst (max_g, weights, values):
    heist2 = 0
    used = 0
    choice = 0
    length = len (weights)
    if length == 0:
        return 0
    density = []
    for x in range (length):
        if weights[x] == 0:
            density.append (0)
        else:
            density.append (values[x] / weights[x])
    while (used < max_g and list_max (density) > 0):
        choice = 0
        for x in range (len (density)):
            if density[x] == list_max (density):
                choice = x
        if (max_g - used) > weights[choice]:
            heist2 = heist2 + values[choice]
            used = used + weights[choice]
            density[choice] = 0
        else:
            heist2 = heist2 + (density[choice] * (max_g - used))
            return heist2
    return heist2


def hst (max_g, items):

	MAXWT = max_g

	sorted_items = sorted(((value/amount, amount)
	                       for amount, value in items),
	                      reverse = True)
	wt = val = 0
	for unit_value, amount in sorted_items:
	    portion = min(MAXWT - wt, amount)
	    wt     += portion
	    addval  = portion * unit_value
	    val    += addval
	    if wt >MAXWT:
	        break

	return val
'''

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)


def sort(request):
	if request.method == 'POST':
		serializer = SnippetSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


				#return HttpResponse('<pre>' + str(request.path) + '</pre>')
				#return Response(str(request.path))
				#data= request.POST.get('data','')
				#return data
			    #return render(request, 'db.html', {'greetings': greetings})
				return render(request,"register.html", {"form": form,})

'''

def quad_parity (x, y):
    if x >= 0 and y >= 0:
        return 1
    elif x < 0 and y < 0:
        return 1
    return -1

def modu (x):
    if x < 0:
        return -x
    return x

def circle (x, y, pi):
    if math.pow (x, 2) + math.pow (y, 2) <= 1:
        return x * y
    elif (x < 1 and y < 1):
        return 0.5 * ((pi / 2) + math.sqrt (math.pow (x, 2) - math.pow (x, 4)) - math.acos (x) + math.sqrt (math.pow (y, 2) - math.pow (y, 4)) - math.acos (y))
    elif (x < 1):
        return 0.5 * ((pi / 2) + math.sqrt (math.pow (x, 2) - math.pow (x, 4)) - math.acos (x))
    elif (y < 1):
        return 0.5 * ((pi / 2) + math.sqrt (math.pow (y, 2) - math.pow (y, 4)) - math.acos (y))
    else:
        return pi / 4

def func_r (cont, type, data, pi):
    temp = 0
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    a1 = 0
    a2 = 0
    b1 = 0
    b2 = 0
    if type == 2:
        data.append (data[2])
        type = 1
    if type == 1:
        x1 = cont[0]
        x2 = cont[0] + cont[2]
        y1 = cont[1]
        y2 = cont[1] + cont[3]
        a1 = data[0]
        a2 = data[0] + data[2]
        b1 = data[1]
        b2 = data[1] + data[3]
        area = (x2 - x1) * (y2 - y1)
        if (cont[0] <= data[0] and cont[0] + cont[2] >= data[0] + data[2] and cont[1] <= data[1] and cont[1] + cont[3] >= data[1] + data[3]):
            return (cont[2] * cont[3]) - (data[2] * data[3])
        if (cont[0] >= data[0] + data[2] or cont[1] >= data[1] + data[3] or cont[0] + cont[2] <= data[0] or cont[1] + cont[3] <= data[1]):
            return cont[2] * cont[3]
        if (x1 >= a1 and x1 <= a2 and y1 >= b1 and y2 <= b2):
            return (x2 - a2) * (y2 - y1)
        if (x2 >= a1 and x2 <= a2 and y1 >= b1 and y2 <= b2):
            return (a1 - x1) * (y2 - y1)
        if (y1 >= b1 and y1 <= b2 and x1 >= a1 and x2 <= a2):
            return (y2 - b2) * (x2 - x1)
        if (y2 >= b1 and y2 <= b2 and x1 >= a1 and x2 <= a2):
            return (b1 - y1) * (x2 - x1)
        if (x1 >= a1 and x1 <= a2 and y1 >= b1 and y2 <= b2):
            return area - ((a2 - x1) * (b2 - y1))
        if (x1 >= a1 and x1 <= a2 and y2 >= b1 and y2 <= b2):
            return area - ((a2 - x1) * (y2 - b1))
        if (x2 >= a1 and x2 <= a2 and y1 >= b1 and y1 <= b2):
            return area - ((x2 - a1) * (b2 - y1))
        if (x2 >= a1 and x2 <= a2 and y2 >= b1 and y2 <= b2):
            return area - ((x2 - a1) * (y2 - b1))
        if (x1 >= a1 and x2 <= a2):
            return (y2 - y1 - (b2 - b1)) * (x2 - x1)
        if (y1 >= b1 and y2 <= b2):
            return (x2 - x1 - (a2 - a1)) * (y2 - y1)
        if (a1 <= x1):
            return area - ((b2 - b1) * (a2 - x1))
        if (a2 >= x2):
            return area - ((b2 - b1) * (x2 - a1))
        if (b1 <= y1):
            return area - ((a2 - a1) * (b2 - y1))
        if (b2 >= y2):
            return area - ((a2 - a1) * (y2 - b1))
        return 0
    if type == 3:
        area = cont[2] * cont [3]
        summer = 0
        ref_array = [[1, -1, -1, 1], [-1, 1, -1, 1], [1, 1, 1, 1], [-1, -1, 1, 1]]
        cont[0] -= data[0]
        cont[1] -= data[1]
        data[0] = 0
        data[1] = 0
        cont[2] /= data[2]
        cont[3] /= data[2]
        cont[0] /= data[2]
        cont[1] /= data[2]
        x1 = cont[0]
        x2 = cont[0] + cont[2]
        y1 = cont[1]
        y2 = cont[1] + cont[3]
        if quad_parity (x1, y1) * quad_parity (x2, y1) == -1:
            summer += 1
        if quad_parity (x2, y1) * quad_parity (x1, y2) == -1:
            summer += 1
        if quad_parity (x1, y2) * quad_parity (x2, y2) == -1:
            summer += 1
        inter = modu (circle (modu (x1), modu (y1), pi) * ref_array[summer][0] + circle (modu (x2), modu (y1), pi) * ref_array[summer][1] + circle (modu (x1), modu (y2), pi) * ref_array[summer][2] + circle (modu (x2), modu (y2), pi) * ref_array[summer][3])
        return area - (inter * data[2] * data[2])


def compress(uncompressed):

    # Build the dictionary.
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}
    # in Python 3: dictionary = {chr(i): i for i in range(dict_size)}

    p = uncompressed[0]
    result = []
    for i in range(1, len(uncompressed), 1):
        c = uncompressed[i]
        pc = p + c
        if pc in dictionary:
            p = pc
        else:
            dictionary[pc] = dict_size
            dict_size += 1
            result.append(dictionary[p])
            # Add wc to the dictionary.
            p = c

    # Output the code for w.
    #if w:
    #    result.append(dictionary[w])
    return( len(result)*12)


def timesched (t, time_list):
    schedule = [0, t]
    for x in time_list:
        t1 = x[0]
        t2 = x[1]
        if (t1 >= t):
            continue
        elif t1 < 0:
            for l in range (len (schedule)):
                if schedule[l] >= t2:
                    break
            if l % 2:
                schedule.insert (l, t2)
                schedule.insert (0, 0)
            else:
                schedule.insert (l, schedule[l])
                schedule.insert (0, 0)
        else:
            for k in range (len (schedule)):
                if schedule[k] > t1:
                    break
            if k % 2:
                if t2 <= schedule[k]:
                    schedule.insert (k, t2)
                    schedule.insert (k, t1)
                else:
                    for l in range (len (schedule)):
                        if schedule[l] > t2:
                            break;
                    if l % 2:
                        schedule.insert (l, t2)
                        schedule.insert (k, t1)
                    else:
                        schedule.insert (l, schedule[l])
                        schedule.insert (k, t1)
            else:
                if t2 <= schedule[k]:
                    schedule.insert (k, schedule [k])
                    schedule.insert (k, schedule [k])
                elif t2 <= schedule[k + 1]:
                    schedule.insert (k + 1, t2)
                    schedule.insert (k, schedule[k])
                else:
                    for l in range (len (schedule)):
                        if schedule[l] > t2:
                            break
                    if l % 2:
                        schedule.insert (l, t2)
                        schedule.insert (k, schedule[k])
                    else:
                        schedule.insert (l, schedule[l])
                        schedule.insert (k, schedule[k])
    maxi = schedule[1] - schedule[0]
    for x in range (int(len (schedule) / 2)):
        if maxi < schedule[(2 * x) + 1] - schedule[(2 * x)]:
            maxi = schedule[(2 * x) + 1] - schedule[(2 * x)]
    return maxi


def func_r_2 (t, time_list):
    schedule = [0, t]
    summer = 0
    k = 0
    l = 0
    for x in time_list:
        flag = 0
        t1 = x[0]
        t2 = x[1]
        if (t1 == t2) or (t2 <= schedule[0]) or (t1 >= schedule[len (schedule) - 1]):
            flag = 1
        else:
            if t1 <= schedule[0] and schedule[0] < t2:
                summer = 0
                for y in range (len (schedule)):
                    if schedule[y] < t2:
                        summer += 1
                k = summer - 1
                if schedule[k] == schedule[len (schedule) - 1]:
                    return 0
                elif k % 2:
                    for y in range (k + 1):
                        schedule.pop (0)
                else:
                    for y in range (k + 1):
                        schedule.pop (0)
                    schedule.append (t2)
                    schedule.sort ()
            elif t1 < schedule[len (schedule) - 1] and t2 >= schedule[len (schedule) - 1]:
                summer = 0
                for y in range (len (schedule)):
                    if schedule[y] > t1:
                        summer += 1
                k = len (schedule) - summer
                if schedule[k] == schedule[0]:
                    return 0
                elif (k % 2) == 0:
                    for y in range (summer):
                        schedule.pop (len (schedule) - 1)
                else:
                    for y in range (summer):
                        schedule.pop (len (schedule) - 1)
                    schedule.append (t1)
                    schedule.sort ()
            elif schedule[0] < t1 and t2 < schedule[len (schedule) - 1]:
                summer = 0
                for y in range (len (schedule)):
                    if schedule[y] < t1:
                        summer += 1
                k = summer - 1
                summer = 0
                for y in range (len (schedule)):
                    if schedule[y] > t2:
                        summer += 1
                l = len (schedule) - summer
                for y in range (k + 1, l):
                    schedule.pop (k + 1)
                if k % 2 == 0:
                    schedule.append (t1)
                if l % 2:
                    schedule.append (t2)
                schedule.sort ()
    maxi = schedule[1] - schedule[0]
    for x in range (int(len (schedule) / 2)):
        if maxi < schedule[(2 * x) + 1] - schedule[(2 * x)]:
            maxi = schedule[(2 * x) + 1] - schedule[(2 * x)]
    return maxi


def func_r_1 (t, time_list):
    schedule = [0, t]
    for x in time_list:
        counter = 0
        t1 = x[0]
        t2 = x[1]
        if (t1 >= t) and counter == 0:
            counter = 1
        elif t1 < 0 and counter == 0:
            for l in range (len (schedule)):
                if schedule[l] >= t2 and counter == 0:
                    counter = 1
            counter = 0
            if l % 2:
                schedule.insert (l, t2)
                schedule.insert (0, 0)
            else:
                schedule.insert (l, schedule[l])
                schedule.insert (0, 0)
        elif counter == 0:
            for k in range (len (schedule)):
                if schedule[k] > t1 and counter == 0:
                    counter = 1
            counter = 0
            if k % 2:
                if t2 <= schedule[k]:
                    schedule.insert (k, t2)
                    schedule.insert (k, t1)
                else:
                    for l in range (len (schedule)):
                        if schedule[l] > t2 and counter == 0:
                            counter = 1
                    counter = 0
                    if l % 2:
                        schedule.insert (l, t2)
                        schedule.insert (k, t1)
                    else:
                        schedule.insert (l, schedule[l])
                        schedule.insert (k, t1)
            else:
                if t2 <= schedule[k]:
                    schedule.insert (k, schedule [k])
                    schedule.insert (k, schedule [k])
                elif t2 <= schedule[k + 1]:
                    schedule.insert (k + 1, t2)
                    schedule.insert (k, schedule[k])
                else:
                    for l in range (len (schedule)):
                        if schedule[l] > t2 and counter == 0:
                            counter = 1
                    counter = 0
                    if l % 2:
                        schedule.insert (l, t2)
                        schedule.insert (k, schedule[k])
                    else:
                        schedule.insert (l, schedule[l])
                        schedule.insert (k, schedule[k])
    maxi = schedule[1] - schedule[0]
    for x in range (int(len (schedule) / 2)):
        if maxi < schedule[(2 * x) + 1] - schedule[(2 * x)]:
            maxi = schedule[(2 * x) + 1] - schedule[(2 * x)]
    return str(int(maxi))


def list_max (a_list):
	maxi = a_list[0]
	for x in a_list:
		if maxi < x:
			maxi = x
	return maxi

def list_min (b_list):
	mini = b_list[0]
	for x in b_list:
		if mini > x:
			mini = x
	return mini

def func_1 (dic, conn, dest):
	degree = []
	for x in range (len (dic)):
		degree.append (-1)
	degree [dic[dest][0]] = 0
	flag = 1
	while (flag):
		curr = list_max (degree)
		for x in conn:
			if degree[dic[x[0]][0]] == curr and degree[dic[x[1]][0]] == -1:
				degree[dic[x[1]][0]] = curr + 1
			elif degree[dic[x[0]][0]] == -1 and degree[dic[x[1]][0]] == curr:
				degree[dic[x[0]][0]] = curr + 1
		if list_min (degree) == 0:
			flag = 0
	return degree

pop = []
def func_2 (dic, conn, dest, degree):

	for x in range(len(dic)):
		pop.append (dic[list(dic)[x]][1])

	while (list_max (degree) > 1):
		maxi = list_max (degree)
		for x in conn:
			if (degree[dic[x[0]][0]] == maxi and degree[dic[x[1]][0]] == maxi - 1):
				pop[dic[x[1]][0]] += pop[dic[x[0]][0]]
				pop[dic[x[0]][0]] = 0
				degree[dic[x[0]][0]] = -1
			if (degree[dic[x[1]][0]] == maxi and degree[dic[x[0]][0]] == maxi - 1):
				pop[dic[x[0]][0]] += pop[dic[x[1]][0]]
				pop[dic[x[1]][0]] = 0
				degree[dic[x[1]][0]] = -1

	maxi = pop[0]
	counter = 0
	for x in range (len (pop)):
		if maxi < pop[x]:
			maxi = pop[x]
			counter = x
	colour = " "
	for x in conn:
		if (x[0] == dest and x[1] == list(dic)[counter]) or (x[1] == dest and x[0] == list(dic)[counter]):
			colour = x[2]

	return [colour, maxi, list(dic)[counter]]


import json
import math

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

    return(result)

def horse3(fullobject):

    data = fullobject['data']

    for jsonob in data:
        print( jsonob['raceno'])
    #print(races)

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

def string_third(strng):

	print("algorithm=WDE, input="+strng)
	dict_size = 256
	dictionary = {}
	sum = 0
	s = re.split('[^a-zA-Z]', strng)
	delim = re.split("[a-zA-Z]", strng)
	delim = list(filter(None, delim))
	for word in s:
		if not word in dictionary:
			dictionary[word] = dict_size
			dict_size+=1
			sum += len(word)*8
		else:
			print("ya")
	result = len(s)*12 + sum + len(delim)*12
	return(result)
