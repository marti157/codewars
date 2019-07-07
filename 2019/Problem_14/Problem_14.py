from math import ceil

days = 0
population = int(input())
zombies = 1
infected = 0
while 0 < population:
	days += 1
	infected = zombies * 2
	zombies -= ceil(0.25 * zombies)
	zombies += infected
	population -= infected

print(days, "days")