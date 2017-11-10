import random
print("hello and welcome to the list exercises")
a=['ana','ben','catlin','help me']
for i in range(len(a)):
    print(a[i][random.randint(0,len(a[i])-1)])
print('')
