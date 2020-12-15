"""for"""
for i in range(5):
    print(i*i)

"""while"""
a = 0
while a < 1001:
    print(a)
    a += 250

"""break & continou"""
a = 0
while True:
    print(a)
    a += 1
    if a >= 5:
        break


"""using else as additional print"""
a=0
while(a<5):
    print(a)
    a +=1
else:
    print("count value reached %d" %(a))