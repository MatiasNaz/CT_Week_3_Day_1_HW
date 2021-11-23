# Exercise 1:
import re
words = ['this', 'is', 'a', 'sentence', '.']


def my_funct(alist):
    alist[0], alist[1], alist[2], alist[3], alist[4] = alist[4], alist[3], alist[2], alist[1], alist[0]
    return alist


print(my_funct(words))

# Exercise 2:

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'


def word_funct(string):
    dict = {}
#     count = 0
    pattern = re.compile('[A-Za-z]+')
    text = pattern.findall(string)
    print(text)
    for word in text:
        if word in dict.keys():
            dict[word] += 1

        else:
            dict[word] = 1
    return dict


word_funct(a_text)


# Exercise 3:

def list_1(nums_list):
    for n in nums_list:
        if n == 70:
            return n


nums_list = [10, 23, 45, 70, 11, 15]
target = 70
print(list_1(nums_list))







