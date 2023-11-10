

stu = {"Alice" : 85, "bob" : 90, "charlie" : 95 }
stu["David"] = 80
stu["Alice"] = 88
#del(stu["bob"])
stu.pop("bob")

for i in stu.keys() :
    print( i, stu[i] )
