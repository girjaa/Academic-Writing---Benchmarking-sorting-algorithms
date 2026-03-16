import random
import csv
import time
import multiprocessing

class Node:
    def __init__(self,v):
        self.v=v
        self.next=None

class LinkedList:
    def __init__(self,arr):
        self.head=None
        p=None
        for x in arr:
            n=Node(x)
            if not self.head:
                self.head=n
            else:
                p.next=n
            p=n

    def to_list(self):
        r=[]
        c=self.head
        while c:
            r.append(c.v)
            c=c.next
        return r

def bubble(a):
    a=a.copy()
    n=len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

def selection(a):
    a=a.copy()
    n=len(a)
    for i in range(n):
        m=i
        for j in range(i+1,n):
            if a[j]<a[m]:
                m=j
        a[i],a[m]=a[m],a[i]
    return a

def insertion(a):
    a=a.copy()
    for i in range(1,len(a)):
        k=a[i]
        j=i-1
        while j>=0 and a[j]>k:
            a[j+1]=a[j]
            j-=1
        a[j+1]=k
    return a

def shell(a):
    a=a.copy()
    n=len(a)
    g=n//2
    while g>0:
        for i in range(g,n):
            t=a[i]
            j=i
            while j>=g and a[j-g]>t:
                a[j]=a[j-g]
                j-=g
            a[j]=t
        g//=2
    return a

def merge(a):
    if len(a)<=1:
        return a
    m=len(a)//2
    l=merge(a[:m])
    r=merge(a[m:])
    return merge2(l,r)

def merge2(l,r):
    o=[]
    i=j=0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            o.append(l[i]);i+=1
        else:
            o.append(r[j]);j+=1
    o+=l[i:]
    o+=r[j:]
    return o

def quick(a):
    if len(a)<=1:
        return a
    p=a[len(a)//2]
    l=[x for x in a if x<p]
    m=[x for x in a if x==p]
    r=[x for x in a if x>p]
    return quick(l)+m+quick(r)

def heap(a):
    import heapq
    h=a.copy()
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]

def counting(a):
    if not a:
        return a
    m=max(a)
    c=[0]*(m+1)
    for x in a:
        c[x]+=1
    o=[]
    for i,v in enumerate(c):
        o+= [i]*v
    return o

def radix(a):
    if not a:
        return a
    m=max(a)
    e=1
    arr=a.copy()
    while m//e>0:
        arr=count_digit(arr,e)
        e*=10
    return arr

def count_digit(a,e):
    n=len(a)
    o=[0]*n
    c=[0]*10
    for i in a:
        idx=i//e
        c[idx%10]+=1
    for i in range(1,10):
        c[i]+=c[i-1]
    i=n-1
    while i>=0:
        idx=a[i]//e
        o[c[idx%10]-1]=a[i]
        c[idx%10]-=1
        i-=1
    return o

def rand(n):
    return [random.randint(0,100000) for _ in range(n)]

def sorted_data(n):
    return list(range(n))

def reverse(n):
    return list(range(n,0,-1))

def almost(n):
    a=list(range(n))
    swaps=max(1,int(n*0.02))
    for _ in range(swaps):
        i=random.randint(0,n-1)
        j=random.randint(0,n-1)
        a[i],a[j]=a[j],a[i]
    return a

def half(n):
    return list(range(n//2))+rand(n-n//2)

def flat(n):
    return [random.randint(0,10) for _ in range(n)]

datasets={
"random":rand,
"sorted":sorted_data,
"reverse":reverse,
"almost":almost,
"half":half,
"flat":flat
}

algs={
"bubble":bubble,
"selection":selection,
"insertion":insertion,
"shell":shell,
"merge":merge,
"quick":quick,
"heap":heap,
"counting":counting,
"radix":radix
}

limits={
"bubble":10000,
"selection":10000,
"insertion":20000,
"shell":1000000,
"merge":100000000,
"quick":100000000,
"heap":100000000,
"counting":100000000,
"radix":100000000
}

def measure(f,data):
    s=time.perf_counter()
    f(data)
    e=time.perf_counter()
    return e-s

def read_sizes():
    sizes=[]
    with open("sizes.txt") as f:
        for l in f:
            sizes.append(int(l.strip()))
    return sizes

def task(args):
    alg_name,dtype,size=args
    if size>limits[alg_name]:
        return None

    gen=datasets[dtype]
    base=gen(size)

    ll=LinkedList(base)
    arr=base.copy()
    ll_data=ll.to_list()

    f=algs[alg_name]

    t1=measure(f,arr)
    t2=measure(f,ll_data)

    return (alg_name,"array",dtype,size,t1),(alg_name,"linked",dtype,size,t2)

def main():
    sizes = read_sizes()

    jobs=[]
    for s in sizes:
        for d in datasets:
            for a in algs:
                jobs.append((a,d,s))

    pool = multiprocessing.Pool()

    results=[]

    for r in pool.imap_unordered(task,jobs):
        if r:
            results.extend(r)

    pool.close()
    pool.join()

    with open("results.csv","w",newline="") as f:
        w=csv.writer(f)
        w.writerow(["algorithm","structure","dataset","size","time"])
        for r in results:
            w.writerow(r)

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()