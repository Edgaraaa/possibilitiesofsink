from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators import csrf
import random
import math
import json
import string
import hashlib
# Create your views here.

nodeGroup={}
sinkGroup={}
nodeNum=0
sinkNum=0
def create_node(nodename,beginx,beginy,width,sinkname):
    node={}
    global nodeNum
    x=random.randint(beginx,beginx+width)
    y=random.randint(beginy,beginy+width)
    node.update({"nodename":nodename})
    node.update({"cluster":sinkname})
    nodestruct={
        "x":x,
        "y":y,
    }
    node.update({"nodestruct":nodestruct})
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    hash=hashlib.md5()
    hash.update(bytes(ran_str,encoding='utf-8'))
    crp=hash.hexdigest()
    node.update({"crp":crp})
    node.update({"nodename":nodename})
    nodeGroup.update({"node"+str(nodeNum):node})
    nodeNum=nodeNum+1
    return node

def create_sinks(sinkname,beginx,beginy,R,width,nodenum):
    sink={}
    global sinkNum
    x=random.randint(beginx,beginx+width)
    y=random.randint(beginy,beginy+width)
    sinkstruct={
        "x":x,
        "y":y,
        "R":R,
    }
    crp=[]
    sink.update({"sinkstruct":sinkstruct})
    nodegroup={}
    for i in range(nodenum):
        node=create_node("node"+str(i),beginx,beginy,width,sinkname)
        crp.append(node["crp"])
        nodegroup.update({"node"+str(i):node})
    sink.update({"nodegroup":nodegroup})
    sink.update({"crp":crp})
    sinkGroup.update({"sink"+str(sinkNum):sink})
    sinkNum=sinkNum+1

def reset():
    global nodeGroup
    global sinkGroup
    global nodeNum
    global sinkNum
    global sinkNum
    nodeGroup={}
    sinkGroup={}
    nodeNum=0
    sinkNum=0
    sinkNum=0

def findTheShortdistance():
    global nodeGroup
    global sinkGroup
    mindistance=0xffffff
    minsink=""
    for i in nodeGroup:
        #print(nodeGroup[i])
        for j in sinkGroup:
            #print(j)
            a=getdistance(nodeGroup[i]['nodestruct']['x'],nodeGroup[i]['nodestruct']['y'],sinkGroup[j]['sinkstruct']['x'],sinkGroup[j]['sinkstruct']['y'])
            #print(a)
            if a<mindistance :
                mindistance=a
                minsink=j
        nodeGroup[i].update({"mindistance":mindistance})
        nodeGroup[i].update({"minsink":minsink})
        mindistance=0xffffff
        minsink=""

def nodecreate(nodenum):
    nodegroup={}
    for i in range(nodenum):
        x=random.randint(0,1000)
        y=random.randint(0,1000)
        nodestruct={
            "x":x,
            "y":y,
        }
        nodegroup.update({"node"+str(i):nodestruct})
    return nodegroup

def sinkcreate(R,sinknum):
    sinkgroup={}
    for i in range(sinknum):
        x=random.randint(0,1000)
        y=random.randint(0,1000)
        sinkstruct={
            "x":x,
            "y":y,
            "R":R,
        }
        sinkgroup.update({"sink"+str(i):sinkstruct})
    return sinkgroup

            
def getdistance(ax,ay,bx,by):
    return math.sqrt((ax-bx)*(ax-bx)+(ay-by)*(ay-by))

def getshortdistance():
    shortdistance=0xffffff
    nearbysink=""
    for i in nodeGroup:
        for j in sinkGroup:
            a=getdistance(nodeGroup[i]['x'],nodeGroup[i]['y'],sinkGroup[j]['x'],sinkGroup[j]['y'])
            if a<=shortdistance :
                shortdistance=a
                nearbysink=j
        nodeGroup[i].update({"nearbysink":nearbysink})
        nodeGroup[i].update({"shortdistance":shortdistance})
        shortdistance=0xffffff
        nearbysink=""

def getfathersink(fathernum,sinknum):
    for i in nodeGroup:
        father=[]
        for k in range(fathernum):
            a=random.randint(0,sinknum)
            if a in father:
                k-=1
                continue
            else:
                father.append(a)
        for j in father:
            nodeGroup[i].update({"sink"+str(j):sinkGroup["sink"+str(j)]})

def getconnect(R):
    global nodeGroup
    global sinkGroup
    a=0
    for i in nodeGroup:
        for j in nodeGroup[i]:
            if j == nodeGroup[i]["nearbysink"]:
                if R>=nodeGroup[i]["shortdistance"]:
                    a+=1
    print("this is a "+str(a))
    return a

def getinareas(R):
    a=0
    for i in nodeGroup:
        if R>=nodeGroup[i]["shortdistance"]:
            a+=1
    return a



def random_create_sinks(sinknum,beginx,beginy,width,R,nodenum):
    reset()
    for i in range(sinknum):
        create_sinks("sink"+str(i),beginx,beginy,R,width,nodenum)
    



def crate_sinkandnode(sinknum,R,nodenum,x):
    global nodeGroup
    global sinkGroup
    reset()
    nodeGroup=nodecreate(nodenum)
    sinkGroup=sinkcreate(R,sinknum)
    getshortdistance()
    getfathersink(x,sinknum-1)




def index1(request):
    return render_to_response("func1.html")

def random_create_sinks_nodes(request):
    global exchangeNum
    ctx={}
    if request.POST['sinknum']!="" and request.POST['R']!="" and request.POST['nodenum']!="" and request.POST['x']!="":
        sinknum=int(request.POST['sinknum'])
        R=int(request.POST['R'])
        nodenum=int(request.POST['nodenum'])
        x=int(request.POST['x'])
        crate_sinkandnode(sinknum,R,nodenum,x)
        print(nodeGroup)
        p=getconnect(R)/getinareas(R)
        #print(p)
    ctx['rlt']=p
    return render(request,"func1.html",ctx)

def index2(request):
    return render_to_response("func2.html")
def people_create_sinks(sinknum,n,R,nodenum):
    reset()
    sinknn=0
    areas=n*n
    sink1=int(sinknum/areas)
    sink2=sinknum%areas
    width=int(1000/n)
    for i in range(n):
        for j in range(n):
            for k in range(sink1):
                create_sinks("sink"+str(sinknn),i*width,j*width,R,width,nodenum)
                sinknn+=1
    for i in range(sink2):
        x=random.randint(0,n)
        y=random.randint(0,n)
        create_sinks("sink"+str(sinknn),x*width,y*width,R,width,nodenum)
        sinknn+=1
def getconnects(R):
    global nodeGroup
    global sinkGroup
    a=0
    for i in sinkGroup:
        for j in nodeGroup:
            if nodeGroup[j]['minsink']==i:
                if nodeGroup[j]['mindistance']<=R:
                    if nodeGroup[j]['crp'] in sinkGroup[i]['crp']:
                        print("NB")
                        print(j+'->'+i)
                        a+=1
    return a

def getareas(R):
    global nodeGroup
    global sinkGroup
    a=0
    for i in nodeGroup:
        print(nodeGroup[i])
        if int(nodeGroup[i]['mindistance'])<=R:
            print(nodeGroup[i]["mindistance"])
            print(R)
            a+=1
    return a

def people_create_sinks_nodes(request):
    ctx={}
    if request.POST['sinknum']!="" and request.POST['n']!="" and request.POST['R']!="" and request.POST['nodenum']!="":
        n=int(request.POST['n'])
        print(n)
        people_create_sinks(int(request.POST['sinknum']),int(request.POST['n']),int(request.POST['R']),int(request.POST['nodenum']))
        f=open("static/json/arg2.json","w")
        print(sinkGroup)
        json.dump(sinkGroup,f)
    else:
        ctx['rlt']="no"
        return render(request,"func2.html",ctx)
    findTheShortdistance()
    print(sinkGroup)
    p=getconnects(int(request.POST['R']))/getareas(int(request.POST['R']))
    files=open("static/txt/record2.txt","a+")
    files.writelines(str(p)+'\n')
    ctx['rlt']="p="+str(p)
    return render(request,"func2.html",ctx)