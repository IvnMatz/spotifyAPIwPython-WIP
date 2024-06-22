from spApi import searchItem

def getID(AccessTk ,Query, type):
    response = searchItem(AccessTk, Query, type)

    return response['albums']['items'][0]['id']



# a = getID("Bearer BQCLkMW5Bf3rynSMXAHa7scsZiI5SMP5PonfDZ6uk1KwodhDtzo9SDjVQty6MBJCMuMMitDRe1Sat9FKVzGiqnghdGa1GSUkg7qKRdoy1H76aI6mBSw", "the queen is dead", "album")
# print(a)