# def greeting():
#     print("hello, chala")
#
# greeting()
#
# list1=[78,43,343,32,23]
# list2=[44,32,44,32,32]
#
# def average(par1):
#     ave=sum(par1)/len(par1)
#     return ave
#
# print(average(list1))
# print(average(list2))
#
# #parity checking
#
# def parity(num):
#     if num%2==0:
#         print("Even number")
#     else:
#         print("Odd number")
#
# parity(6)
# parity(7)


# def add(*args):
#     print(sum(args))
#
# add(3,4,5)
# add(4,5,6,7)

def argss(*args,**kwargs):
    print(args)
    for key,value in kwargs.items():
        print(key,value)

argss(12,2,3,4,name="CHala",age=23)
