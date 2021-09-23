"""Examples of using lists in a a simple 'game' . """


from random import randint


rolls: list[int] = list()
rolls.append(randint(1, 6))
 
print(rolls)