# possibilitiesofsink

>  本项目是为了帮助老师完成节点验证的模拟实验

## 代码需求

* sink与node随机分布，求sink与node匹配率
* sink与node按区域投放，求sink与node匹配率
* sink存放的crp存在重叠情况，求sink与node匹配率
* 求sink中存在重叠crp的情况下node不在区域内的概率

## 数据结构设计

```json
//sinkstruct
{
    "sinknum":{
        "nodegroup":{
            "node1":{
                "nodestruct":{
                    "x":x,
                    "y",y,
                },
                "crp":"123456",
                "clusternum":"sinknum",
            }
            ....
        },
        "sinkstruct":{
            "x":x,
            "y":y,
            "R":r
        },
        "crp":['123456',......],
 		"nodeinthisarea":123,
        "nodeofthissink":456,
        "p":0.123
     	},
}
//nodestruct
{
    "nodenum":"node1",
    "nodestruct":{
        "x":x,
        "y":y
    },
    "crpresponse":"123456",
    "distancegroup":{
        "sink1":1,
        "sink2":2,
        ......
    },
    "shortdistance":"sink1"
}
```

## 模拟算法实现

​	本次算法主要还是使用python库中自带的random随机数生成器去生成对应的sink和node对应的投放点，按照代码需求限制投放情况去投放sink和node，从而可以模拟实际场景的投放以及计算连通率。

