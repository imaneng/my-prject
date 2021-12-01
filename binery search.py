
a =[2,5,7,15,18,25,39]

def bs (lis,adad):
    n = len(lis)
    lo = 0
    hi = n-1
    
    while lo <= hi :
        mid = (lo + hi) // 2
        if adad == lis[mid] :
            return mid
        elif adad < lis[mid]:
            hi = mid -1
        elif adad > lis[mid] :
            lo = mid+1
        
    return -1
    
print(bs(a,39))


def ser(lis: list, lo, hi, adad):
    mid = (lo+hi) // 2
    if lo <= hi:
        
        if adad == lis[mid]:
            return mid
        elif adad < lis[mid]:
            return ser(lis,lo,mid -1,adad)
        else:
            return ser(lis,mid +1,hi ,adad)
        
    return -1

b = [8,9,14,39,78,98,120,133]
s=(len(b))-1
m=ser(b,0,s,39)
print(m)
print("byyyyyyyy")
