import random
import csv
import time

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self,arr):
        self.head=None
        prev=None
        for v in arr:
            node=Node(v)
            if not self.head:
                self.head=node
            else:
                prev.next=node
            prev=node

    def to_list(self):
        arr=[]
        cur=self.head
        while cur:
            arr.append(cur.val)
            cur=cur.next
        return arr

def bubble_sort(a):
    a=a.copy()
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

def selection_sort(a):
    a=a.copy()
    n=len(a)
    for i in range(n):
        m=i
        for j in range(i+1,n):
            if a[j]<a[m]:
                m=j
        a[i],a[m]=a[m],a[i]
    return a

def insertion_sort(a):
    a=a.copy()
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
    return a

def shell_sort(a):
    a=a.copy()
    n=len(a)
    gap=n//2
    while gap>0:
        for i in range(gap,n):
            temp=a[i]
            j=i
            while j>=gap and a[j-gap]>temp:
                a[j]=a[j-gap]
                j-=gap
            a[j]=temp
        gap//=2
    return a

def merge_sort(a):
    if len(a)<=1:
        return a
    mid=len(a)//2
    left=merge_sort(a[:mid])
    right=merge_sort(a[mid:])
    return merge(left,right)

def merge(l,r):
    res=[]
    i=j=0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            res.append(l[i])
            i+=1
        else:
            res.append(r[j])
            j+=1
    res+=l[i:]
    res+=r[j:]
    return res

def quick_sort(a):
    if len(a)<=1:
        return a
    p=a[len(a)//2]
    left=[x for x in a if x<p]
    mid=[x for x in a if x==p]
    right=[x for x in a if x>p]
    return quick_sort(left)+mid+quick_sort(right)

def heap_sort(a):
    import heapq
    h=a.copy()
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]

def counting_sort(a):
    if not a:
        return a
    m=max(a)
    c=[0]*(m+1)
    for x in a:
        c[x]+=1
    res=[]
    for i,v in enumerate(c):
        res+= [i]*v
    return res

def radix_sort(a):
    if not a:
        return a
    m=max(a)
    exp=1
    arr=a.copy()
    while m//exp>0:
        arr=counting_digit(arr,exp)
        exp*=10
    return arr

def counting_digit(a,exp):
    n=len(a)
    output=[0]*n
    count=[0]*10
    for i in a:
        index=i//exp
        count[index%10]+=1
    for i in range(1,10):
        count[i]+=count[i-1]
    i=n-1
    while i>=0:
        index=a[i]//exp
        output[count[index%10]-1]=a[i]
        count[index%10]-=1
        i-=1
    return output

def random_list(n):
    return [random.randint(0,100000) for _ in range(n)]

def sorted_list(n):
    return list(range(n))

def reverse_list(n):
    return list(range(n,0,-1))

def almost_sorted(n):
    arr=list(range(n))
    swaps=max(1,int(n*0.02))
    for _ in range(swaps):
        i=random.randint(0,n-1)
        j=random.randint(0,n-1)
        arr[i],arr[j]=arr[j],arr[i]
    return arr

def half_sorted(n):
    arr=list(range(n//2))+random_list(n-n//2)
    return arr

def flat_list(n):
    return [random.randint(0,5) for _ in range(n)]

def measure(func,data):
    start=time.perf_counter()
    func(data)
    end=time.perf_counter()
    return end-start

def load_sizes(file):
    sizes=[]
    with open(file) as f:
        for line in f:
            sizes.append(int(line.strip()))
    return sizes

algorithms={
"bubble":bubble_sort,
"selection":selection_sort,
"insertion":insertion_sort,
"shell":shell_sort,
"merge":merge_sort,
"quick":quick_sort,
"heap":heap_sort,
"counting":counting_sort,
"radix":radix_sort
}

datasets={
"random":random_list,
"sorted":sorted_list,
"reverse":reverse_list,
"almost_sorted":almost_sorted,
"half_sorted":half_sorted,
"flat":flat_list
}

sizes=load_sizes("sizes.txt")

with open("results.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["algorithm","structure","dataset","size","time"])

    for size in sizes:
        for dtype,gen in datasets.items():
            data=gen(size)

            ll=LinkedList(data)
            list_data=data.copy()
            ll_data=ll.to_list()

            for name,alg in algorithms.items():
                t=measure(alg,list_data)
                writer.writerow([name,"array",dtype,size,t])

                t=measure(alg,ll_data)
                writer.writerow([name,"linked_list",dtype,size,t])