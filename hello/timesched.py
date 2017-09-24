#Let's suppose I do this
#I create a list of times
#The first entry would be start_time
#and last entry would be end_time
#Then every interval is either 1 or 0
#1 is available (can use), 0 is occupied (cant use)
#Then one by one events come.
#Event_start = t1
#So, I put t1 into the array. Like, I see where it lies
#If t1 already lies, then check the position of the last such t1.
#If it has index 0, 2, 4, ..., etc. then t1 is actually an available time.
#Then, insert t1 after this last copy of t1 and check t2 vs next in array after t1
#If t2 is big, then insert the number in array again
#Otherwise, put t2 in the array after t1
#If t1 has index 1, 3, 5, ..., etc. then put t1 = next time after t1 and goto line 14
#If t1 isnt already there, figure out which index it should replace
#If the

#So, kets put t1 as 0 and t2 - t1 as t.
#Then, for anytime time subtract t1 from it.

#i = 3
#t = 10800
#time_list = [(900, 4500), (8100, 9900), (10200, 10740)]

def timesched (i, t, time_list):
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
    for x in range (len (schedule) / 2):
        if maxi < schedule[(2 * x) + 1] - schedule[(2 * x)]:
            maxi = schedule[(2 * x) + 1] - schedule[(2 * x)]
    return maxi

#print timesched (i, t, time_list)
