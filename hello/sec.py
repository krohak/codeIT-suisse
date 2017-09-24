l={"destination":"DhobyGhaut","stations":[{"name":"Punggol","passengers":80,"connections":[{"station":"Sengkang","line":"purple"}]},{"name":"Sengkang","passengers":40,"connections":[{"station":"Punggol","line":"purple"},{"station":"Serangoon","line":"purple"}]},{"name":"Serangoon","passengers":40,"connections":[{"station":"LittleIndia","line":"purple"},{"station":"Sengkang","line":"purple"},{"station":"PayaLebar","line":"orange"},{"station":"Bishan","line":"orange"}]},{"name":"LittleIndia","passengers":40,"connections":[{"station":"Serangoon","line":"purple"},{"station":"DhobyGhaut","line":"purple"}]},{"name":"DhobyGhaut","passengers":20,"connections":[{"station":"LittleIndia","line":"purple"},{"station":"HarbourFront","line":"purple"},{"station":"Somerset","line":"red"},{"station":"MarinaBay","line":"red"},{"station":"Esplanade","line":"orange"}]},{"name":"HarbourFront","passengers":90,"connections":[{"station":"DhobyGhaut","line":"purple"}]},{"name":"Somerset","passengers":0,"connections":[{"station":"DhobyGhaut","line":"red"},{"station":"Orchard","line":"red"}]},{"name":"Orchard","passengers":30,"connections":[{"station":"Somerset","line":"red"},{"station":"Novena","line":"red"}]},{"name":"Novena","passengers":10,"connections":[{"station":"Orchard","line":"red"},{"station":"Bishan","line":"red"}]},{"name":"Bishan","passengers":20,"connections":[{"station":"Novena","line":"red"},{"station":"Woodlands","line":"red"},{"station":"Serangoon","line":"orange"}]},{"name":"Woodlands","passengers":40,"connections":[{"station":"Bishan","line":"red"}]},{"name":"MarinaBay","passengers":100,"connections":[{"station":"DhobyGhaut","line":"red"}]},{"name":"Esplanade","passengers":0,"connections":[{"station":"DhobyGhaut","line":"orange"},{"station":"PayaLebar","line":"orange"}]},{"name":"PayaLebar","passengers":75,"connections":[{"station":"Esplanade","line":"orange"},{"station":"Serangoon","line":"orange"}]}]}

from collections import OrderedDict


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
    arr = []
    destin = 0
    for x in range (len (dic)):
        arr.append ([])
    for x in dic.items():
        arr[x[1][0]].append (x[0])
        arr[x[1][0]].append (x[1][0])
        arr[x[1][0]].append (x[1][1])
    degree = []
    for x in range (len (arr)):
        degree.append (-1)
    for x in arr:
        if x[0] == dest:
            destin = x[1]
    degree [destin] = 0
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

def func_2 (dic, conn, dest, degree):
    arr = []
    destin = 0
    for x in range (len (dic)):
        arr.append ([])
    for x in dic.items():
        arr[x[1][0]].append (x[0])
        arr[x[1][0]].append (x[1][0])
        arr[x[1][0]].append (x[1][1])
    for x in arr:
        if x[0] == dest:
            destin = x[1]
    pop = []
    for x in range (len (dic)):
        pop.append (arr[x][2])
    while (list_max (degree) > 1):
        maxi = list_max (degree)
        for x in conn:
            if degree[dic[x[0]][0]] == maxi and degree[dic[x[1]][0]] == maxi - 1:
                pop[dic[x[1]][0]] += pop[dic[x[0]][0]]
                pop[dic[x[0]][0]] = 0
                degree[dic[x[0]][0]] = -1
            if degree[dic[x[1]][0]] == maxi and degree[dic[x[0]][0]] == maxi - 1:
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
        if (x[0] == dest and x[1] == arr[counter][0]) or (x[1] == dest and x[0] == arr[counter][0]):
            colour = x[2]
    return [colour, maxi, arr[counter][0]]


nodes=[]
destination=l["destination"]
node_dict={}
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

print(func_2(node_dict,edge_list,destination,func_1(node_dict,edge_list,destination)))
# Create a graph given in the above diagram
'''
g = Graph ();
g.addEdge("ramu", "sagar")
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)

target = 6; maxDepth = 3; src = 0

if g.IDDFS(src, target, maxDepth) == True:
    print ("Target is reachable from source " +
        "within max depth")
else :
    print ("Target is NOT reachable from source " +
        "within max depth")


'''



'''


max_weight
weights=[]
values=[]
densities=[]
densities=sort(densities)
val

weights=sort(weights,key=densities)
values=sort(values,key=densities)

for i,den_i in enumerate(densities):
    while(max_weight>0 or weight[i]!=0):
        max_weight-=values[i]
        weight[i]-=1

    while(max_weight!=0):
        if(weight[i]==0):
            max_weight-=values[i]

'''
