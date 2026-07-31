dic = {"tom" : 123456789,
       "john": 123567890,
       "bon" : 1234567890,
       }
print(dic)

print(dic["tom"])

dic["sam"] = 9876544521

print(dic)

del dic["sam"]

print(dic)

for key in dic:
    print(f"Key : {key}, Value : {dic[key]}")

for key, value in dic.items():
    print(key,value)

print("tom" in dic)
print("samir" in dic)

dic.clear()
print(dic)

tuple_point = (5,6)

print(tuple_point)
print(tuple_point[0])
print(tuple_point[1])

# tuple_point[0] = 1 We can not change values in tuples.
