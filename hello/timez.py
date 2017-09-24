
import json
import datetime
import pytz

#j=str()

a=["3;28-05-2017 13:00:00.000+0800;28-05-2017 16:00:00.000+0800","London morning trading check;28-05-2017 05:15:00.000Z;28-05-2017 06:15:00.000Z","Tokyo risk testing;28-05-2017 16:15:00.000+0900;28-05-2017 16:45:00.000+0900","New York midnight database check;28-05-2017 03:50:00.000-0400;28-05-2017 03:59:00.000-0400"]
ele=a[0].split(";")
ran=ele[0]
t1=ele[1]
t2=ele[2]
try:
    next_time=datetime.datetime.strptime(t1,'%d-%m-%Y %H:%M:%S.%f%z')
    next_time2=datetime.datetime.strptime(t2,'%d-%m-%Y %H:%M:%S.%f%z')
except Exception as e:
    #print(e)
    next_time=datetime.datetime.strptime(t1,'%d-%m-%Y %H:%M:%S.%fZ')
    next_time2=datetime.datetime.strptime(t2,'%d-%m-%Y %H:%M:%S.%fZ')

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

print(time_durations)
print(a1)





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


print(timesched(a1,time_durations))
