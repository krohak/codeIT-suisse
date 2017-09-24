def hst (max_g, items):

    MAXWT = max_g
    if(MAXWT>1000 or MAXWT<=0):
        print("fuck off")
        return 0

    z=range(101)

    sorted_items = sorted(((value/amount, amount)
	                       for amount, value in items if (amount not in z or value not in z)),
	                      reverse = True)
    wt = val = 0

    for unit_value, amount in sorted_items:
        portion = min(MAXWT - wt, amount)
        wt     += portion
        addval  = portion * unit_value
        val    += addval
        if wt >= MAXWT:
            break

    return val


a={
  "maxWeight": 4,
  "vault": [
  {"weight": 1, "value": 200},
  {"weight": 3, "value": 240},
  {"weight": 5, "value": 150},
  {"weight": 2, "value": 140}
  ]
}



values=[]
max_val=a['maxWeight']
val=a['vault']
for e in val:
    values.append((e['weight'],e['value']))

data = {}
data["heist"] = int(hst(max_val,values))
print(str(data))
#return HttpResponse(json.dumps(data))
