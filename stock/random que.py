import random
cities=['agra','delhi','chennai','bhopal']
NUM=random.randint(1,2)+1
for city in cities:
    for I in range(1,NUM):
        print(city,end='')
    print()
