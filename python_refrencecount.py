import sys
a = "shankar"
print("refrence count:",sys.getrefcount(a))
print("addres of : ",id(a))

b = a
print("refrence count :",sys.getrefcount(a))
print("addres of : ",id(b))

b="suzaki"
print("refrence count :",sys.getrefcount(a))
print("addres of : ",id(b))