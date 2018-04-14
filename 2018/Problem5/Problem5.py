name = raw_input()
age = int(raw_input())
gender = raw_input().lower()
city = raw_input()
sport = raw_input()
team = raw_input()
job = raw_input()
if gender == "girl":
	print "%s is a %i year-old %s. %s is living with %s parents in an apartment in the centre of %s, where %s hangs out with %s friends. Moreover, in %s free time %s plays %s in a team called %s. %s would like to pursue a career in %s when %s is older, that's why %s is studying hard." %(name, age, gender, "She", "her", city, "she", "her", "her", "she", sport, team, name, job, "she", "she")
else:
	print "%s is a %i year-old %s. %s is living with %s parents in an apartment in the centre of %s, where %s hangs out with %s friends. Moreover, in %s free time %s plays %s in a team called %s. %s would like to pursue a career in %s when %s is older, that's why %s is studying hard." %(name, age, gender, "He", "his", city, "he", "his", "his", "he", sport, team, name, job, "he", "he")