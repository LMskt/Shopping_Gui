import json

from Dao.commodity_dao import commodity_get_all, commodity, commodity_get_byname
from Util.to_json import commodity_json


def com_get_all():
    a=commodity_get_all()
    return commodity_json(a)

def com_get_byname(name):
    a=commodity_get_byname(name)
    return commodity_json(a)


if __name__ =="__main__":
    a = com_get_all()
    print(a)
