def hst (a):

    weights=[]
    items=[]
    #print(str(request.body))

    #a=''.join(c for c in str(request.body) if c.isdigit())
    max_val=a['maxWeight']
    val=a['vault']
    for e in val:
        items.append((e['weight'],e['value']))

    MAXWT = max_val
    if(MAXWT>1000 or MAXWT<=0):
	       return 0

    z=range(101)
    sorted_items = sorted(((float(value)/float(amount), amount) for amount, value in items if (amount not in z or value not in z)),reverse = True)
    wt = val = 0
    for unit_value, amount in sorted_items:
        portion = min(MAXWT - wt, amount)
        wt     += portion
        addval  = portion * unit_value
        val    += addval
        if wt > MAXWT:
            break
    print(val)

data={
"maxWeight": 4,
"vault": [
{"weight": 1, "value": 200},
{"weight": 3, "value": 240},
{"weight": 5, "value": 150},
{"weight": 2, "value": 140}
]
}
hst (data)
''':

    items=[]


    #a=''.join(c for c in str(request.body) if c.isdigit())
    max_val=data['maxWeight']
    print(max_val)
    val=data['vault']

    for e in val:
        if(e['weight'] > 100 or e['value'] > 100):
            return 0
        items.append((e['weight'],e['value']))

    MAXWT = max_val
    if(MAXWT>1000 or MAXWT<=0):
        return 0

    z=range(101)
    sorted_items = sorted( ((value/amount, amount) for amount, value in items), reverse = True)
    wt = val = 0
    for unit_value, amount in sorted_items:
        portion = min(MAXWT - wt, amount)
        wt     += portion
        addval  = portion * unit_value
        val    += addval
        if wt >= MAXWT:
            break
    print(val)


data = {
  "maxWeight": 4,
  "vault": [
  {"weight": 1, "value": 200},
  {"weight": 3, "value": 240},
  {"weight": 5, "value": 150},
  {"weight": 2, "value": 140}
  ]
}
hst(data)
'''
