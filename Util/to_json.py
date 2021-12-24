import json


def commodity(com):
    return {
        'id':com.id,
        'name':com.name,
        'price':com.price,
        'number':com.number,
        'img':com.img,
        'introduce':com.introduce
    }

def commodity_json(obj):
    return json.dumps(obj,default=commodity,ensure_ascii=False)

def user(usr):
    return {
        'id':usr.id,
        'username':usr.username,
        'password':usr.password,
        'name':usr.name
    }

def user_json(obj):
    return json.dumps(obj,default=user,ensure_ascii=False)


def order(ord):
    return {
        'username':ord.username,
        'commodityname':ord.commodityname,
        'price':ord.price
    }

def order_josn(obj):
    return json.dumps(obj,default=order,ensure_ascii=False)