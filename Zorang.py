import requests,math

def dis(a,b):
    x1,y1 = a[0],a[1]
    x2,y2 = b[0], b[1]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

#---------------------------------------  extract data from given url
p = requests.get("https://zorang-recrutment.s3.ap-south-1.amazonaws.com/addresses.json")
p = p.json() #----------------convert it into json


initx,inity = map(float,input().split())  #--------- initial coordinate of store taken as input.


arr = []
for i in p:
    arr.append([i["latitude"],i["longitude"],i["_id"]])
# arr.sort()
lo = 0
hi = 10**10
ans = []
while(lo<=hi):
    mid = (lo+hi)/2 #----------------------- mid can be a min dist travelled by all of the given agent.
    res = [[] for i in range(10)]
    def check(mid):
        tot = 0
        arr2 = []
        for i in arr:
            arr2.append(i)
        totdist = 0
        a, b = initx, inity
        while(tot<10 and len(arr2)>0):
            dist = []
            index = 0
            for i,j,k in arr2:
                dist.append([dis([i,j],[a,b]),i,j,k,index])
                index+=1
            dist.sort()
            totdist+=dist[0][0]
            finaldist = dis([initx,inity],[dist[0][1],dist[0][2]])
            if totdist+finaldist<=mid:
                a,b = dist[0][1],dist[0][2]
                res[tot].append(dist[0][3])
                arr2.pop(dist[0][4])
            else:
                tot+=1
                totdist = 0
                a,b = initx,inity
        if len(arr2)==0:
            return res
        else:
            return False
    if check(mid):
        ans = res.copy()
        hi = mid-1
    else:
        lo = mid+1
remaining = 0
for i in ans:
    if len(i)==0:
        remaining+=1
l = []
for i in range(len(ans)):
    if remaining==0:
        break
    while(len(ans[i])>1 and remaining>0):
        l.append(ans[i].pop())
        remaining-=1
for i in range(len(ans)):
    if ans[i]==[]:
        ans[i].append(l.pop()) #----------------ensuring every agents deliver at least one parcel.
print(ans)