planets = {"mercury": 88, "venus": 225, "earth": 365, "mars": 687, "jupiter": 4333, "saturn": 10759, "uranus": 30689, "neptune": 60182}
var1 = int(raw_input())
var2 = raw_input().lower()
print planets[var2] * var1 / planets["earth"]