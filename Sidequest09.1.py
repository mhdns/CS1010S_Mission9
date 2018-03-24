import json
import time


def read_json(filename):
    datafile = open(filename, 'r', encoding="utf-8")
    return json.loads(datafile.read())

def write_json(filename, data):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)


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
def merge(list, field):
    final = []
    original = list.copy()
    while original:
        smallest = []
        if [] in original:
            while [] in original:
                original.remove([])
        if original:
            smallest = original[0][0]
        for i in original:
            for j in i:
                if field(j) < field(smallest):
                    smallest = j
        if smallest != []:
            final.append(smallest)
        for i in original:
            for j in i:
                if smallest == j:
                    i.remove(j)
                    break
    return final

#Part 2

def divide(lst, k):
    res = []
    original = lst.copy()
    remainder = len(lst)%k
    quotient = len(lst)//k
    if remainder > 0:
        tail = original[-remainder::]
        original[-remainder::] = []
    else:
        tail = []
    for i in range(0,len(original),quotient):
        res.append(original[i:i+quotient])
    res.append(tail)
    return res



def merge_sort(lst, k, field):
    original = divide(lst,k)
    return merge(original, field)

