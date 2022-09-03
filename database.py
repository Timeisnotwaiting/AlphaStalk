from mongo import db

stalkdb = db.stalk

async def stalk(_: int):
    stalking = stalkdb.find_one({"_": _})
    if stalking:
        return 
    return await stalkdb.insert_one({"_": _})

async def unstalk(_: int):
    stalking = stalkdb.find_one({"_": _})
    if not stalking:
        return 
    return await stalkdb.delete_one({"_": _})

async def list_stalk():
    get = stalkdb.find({"_": {"$gt": 0}})
    if not get:
        return []
    lel = await get.to_list(length=10000000000)
    l = []
    for l in lel:
        l.append(lel["_"])
    return l

async def stalking(_: int):
    stalking = stalkdb.find_one({"_": _})
    if stalking:
        return True
    return False

stalkdb = db.stalk

async def add_sudo(_: int):
    stalking = stalksudo.find_one({"_": _})
    if stalking:
        return 
    return await stalksudo.insert_one({"_": _})

async def del_sudo(_: int):
    stalking = stalksudo.find_one({"_": _})
    if not stalking:
        return 
    return await stalksudo.delete_one({"_": _})

async def list_sudo():
    get = stalksudo.find({"_": {"$gt": 0}})
    if not get:
        return []
    lel = await get.to_list(length=10000000000)
    l = []
    for l in lel:
        l.append(lel["_"])
    return l

async def is_sudo(_: int):
    stalking = stalksudo.find_one({"_": _})
    if stalking:
        return True
    return False
