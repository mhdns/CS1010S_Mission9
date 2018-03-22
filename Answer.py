import json
import time


def read_json(filename):
    datafile = open(filename, 'r', encoding="utf-8")
    return json.loads(datafile.read())


#############
# Accessors #
#############


def module_code(module):
    return module[0]


def module_name(module):
    return module[1]


def module_prof(module):
    return module[2]


#Question 1 part a
#Get the position where k belongs
def search(k, lst):
    mid = len(lst) // 2
    if lst == []:
        return 0
    elif k > lst[mid]:
        return len(lst[:mid+1]) + search(k, lst[mid+1::])
    else:
        return search(k, lst[0:mid])


def insert_list(k, lst):
    lst.insert(search(k, lst), k)
    return lst


def accumulate(fn, initial, seq):
    if not seq:
        return initial
    else:
        return fn(seq[0], accumulate(fn, initial, seq[1:]))


def sort_list(lst):
    return accumulate(insert_list, [], lst)


def merge_lists(lists):
    return sort_list(accumulate(lambda x, y: x+y, [], lists))

#Oestion 1 part b
def search_choice(module, lst, field): #field is getter function, k is the attribute
    mid = len(lst) // 2
    if lst == []:
        return 0
    elif field(module) < field(lst[mid]):
        return search_choice(field(module), lst[0:mid],field)
    else:
        return len(lst[:mid + 1]) + search_choice(field(module), lst[mid+1::], field)

def insert_choice(module, lst, field):
    lst.insert(search_choice(module, lst, field), module)
    return lst

def sort_choice(lst, field):
    res = []
    for i in lst:
        print(res)
        res = insert_choice(i,res, field)
    return res
    return accumulate(lambda x, y: insert_choice(x, y, field), [], lst)


def merge(lists, field):
    return sort_choice(accumulate(lambda x, y: x + y, [], lists), field)