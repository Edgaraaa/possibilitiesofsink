from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import random
import math
import json
import hashlib
# Create your views here.

nodeGroup={}
nodeNum=0
def create_sink(sinkname,R,begin,end):
    sink={}
    x=random.randint(begin,end)
    y=random.randint(begin,end)
    point={
        'R':R,
        'x':x,
        'y':y,
    }
    sink.update({sinkname:point})
    return sink

def random_create_node(num,begin,end,clustername,sinkx,sinky,sinkR):
    nodegroup={}
    for i in range(num):
        flag=0
        node={}
        x=random.randint(begin,end)
        y=random.randint(begin,end)
        distance=math.sqrt((sinkx-x)**2+(sinky-y)**2)
        if(sinkR>=distance):
            flag=1
        point={
            'clustername':clustername,
            'x':x,
            'y':y,
            'distance':distance,
            'flag':flag
        }
        nodegroup.update({'node'+str(i):point})
    return nodegroup

def random_create_sinks(sinknum,R,sinkbegin,sinkend,nodenum,nodebegin,nodeend):
    sinkgroup={}
    for i in range(sinknum):
        sink=create_sink('sink'+str(i),R,sinkbegin,sinkend)
        nodegroup=random_create_node(nodenum,nodebegin,nodeend,'sink'+str(i),sink['sink'+str(i)]['x'],sink['sink'+str(i)]['y'],R)
        sink.update({'nodegroup':nodegroup})
        sinkgroup.update({'cluster'+str(i):sink})
    return sinkgroup

def create_form(request):
    return render_to_response('test1.html')

def create_sink_node_group_random(request):
    request.encoding='utf-8'
    if 'sinknum' in request.GET and 'R' in request.GET and 'sinkbegin' in request.GET and 'sinkend' in request.GET and 'nodenum' in request.GET:
        message = random_create_sinks(int(request.GET['sinknum']),int(request.GET['R']),int(request.GET['sinkbegin']),int(request.GET['sinkend']),int(request.GET['nodenum']),int(request.GET['sinkbegin']),int(request.GET['sinkend']))
    else:
        message = '你提交了空表单'
    print(type(message))
    for i in message:
        print(message[i])
        innum=0
        for j in message[i]:
            if "nodegroup" in j:
                print(message[i][j])
                for k in message[i][j]:
                    if message[i][j][k]["flag"] == 1:
                        innum+=1
        message[i].update({"in":innum})
        p=float(innum/float(request.GET['nodenum'])*1.0)
        message[i].update({"p":p})
    f=open("/home/edgar/Desktop/project/static/json/arg.json",'w')
    json.dump(message,f)
    return HttpResponse("hh")

def create_form2(request):
    return render_to_response('test2.html')

def create_sink_by_people(sinkname,R,beginx,beginy,width):
    sink={}
    x=random.randint(beginx,beginx+width)
    y=random.randint(beginy,beginy+width)
    point={
        'R':R,
        'x':x,
        'y':y,
    }
    sink.update({sinkname:point})
    return sink

def create_node_by_people(num,beginx,beginy,width,clustername,sinkx,sinky,sinkR):
    nodegroup={}
    for i in range(num):
        flag=0
        node={}
        x=random.randint(beginx,beginx+width)
        y=random.randint(beginy,beginy+width)
        distance=math.sqrt((sinkx-x)**2+(sinky-y)**2)
        if(sinkR>=distance):
            flag=1
        point={
            'clustername':clustername,
            'x':x,
            'y':y,
            'distance':distance,
            'flag':flag
        }
        nodegroup.update({'node'+str(i):point})
    return nodegroup   


def random_create_sinks_by_people(sinknum,R,nodenum,n):
    sinkseach=int(sinknum/(n*n))
    sinkleft=sinknum%(n*n)
    sinkgroup={}
    numofsink=0
    width=int(1000/n)
    for i in range(n):
        for j in range(n):
            for k in range(sinkseach):
                sink=create_sink_by_people('sink'+str(numofsink),R,i*width,j*width,width)
                nodegroup=create_node_by_people(nodenum,i*width,j*width,width,'sink'+str(numofsink),sink['sink'+str(numofsink)]['x'],sink['sink'+str(numofsink)]['y'],R)
                sink.update({'nodegroup':nodegroup})
                sinkgroup.update({'cluster'+str(numofsink):sink})
                numofsink+=1
    for i in range(sinkleft):
        m=random.randint(0,n)
        n=random.randint(0,n)
        sink=create_sink_by_people('sink'+str(numofsink),R,m*width,n*width,width)
        nodegroup=create_node_by_people(nodenum,m*width,n*width,width,'sink'+str(numofsink),sink['sink'+str(numofsink)]['x'],sink['sink'+str(numofsink)]['y'],R)
        sink.update({'nodegroup':nodegroup})
        sinkgroup.update({'cluster'+str(numofsink):sink})
        numofsink+=1
    return sinkgroup

def create_sink_node_by_people(request):
    request.encoding='utf-8'
    if 'sinknum' in request.GET and 'R' in request.GET and 'nodenum' in request.GET and 'n' in request.GET:
        message=random_create_sinks_by_people(int(request.GET['sinknum']),int(request.GET['R']),int(request.GET['nodenum']),int(request.GET['n']))
    else:
        message='no things!'
    for i in message:
        print(message[i])
        innum=0
        for j in message[i]:
            if "nodegroup" in j:
                print(message[i][j])
                for k in message[i][j]:
                    if message[i][j][k]["flag"] == 1:
                        innum+=1
        message[i].update({"in":innum})
        p=float(innum/float(request.GET['nodenum'])*1.0)
        message[i].update({"p":p})
    f=open("/home/edgar/Desktop/project/static/json/arg2.json",'w')
    json.dump(message,f)
    return HttpResponse("hh")

def create_node(nodename,beginx,beginy,width,sinkname):
    node={}
    x=random.randint(beginx,beginx+width)
    y=random.randint(beginy,beginy+width)
    node.update({"nodename":nodename})
    nodestruct={
        "x":x,
        "y":y,
    }
    node.update({"nodestruct":nodestruct})
    hash=hashlib.md5()
    hash.update(bytes(nodename,encoding='utf-8'))
    crp=hash.hexdigest()
    node.update({"crp":crp})
    node.update({"nodename":nodename})
    nodeGroup.update({"node"+str(nodeNum):node})
    return node

def create_sinks(sinkname,beginx,beginy,R,width,nodenum):
    sink={}
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
    return sink


