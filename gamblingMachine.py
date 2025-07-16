# Gambling machine simulation

LEMON = int(1)
CHERRY = int(2)
SEVEN = int(3)
SKULL = int(4)
mapSpin = {LEMON: "🍋", CHERRY: "🍒", SEVEN: "7️⃣", SKULL: "💀"}

SCORE_TWO = int(5)
SCORE_THREE = int(10)
# spin returns three values, each vlaue is a random number between 1 and 4
def spin():
    import random
    return random.randint(1, 4), random.randint(1, 4), random.randint(1, 4)

def score(vals):
    # if all values are identical...
    if vals[0] == vals[1] == vals[2]:
        if numVals(vals, SKULL) != 0:
            return -SCORE_THREE
        return SCORE_THREE
    
    # if two values are identical...
    if vals[0] == vals[1] or vals[1] == vals[2] or vals[0] == vals[2]:
        if numVals(vals, SKULL) > 1:
            return -SCORE_TWO
        return SCORE_TWO  # Example score for two identical values

    return int(0)

def numVals(vals, val):
    # count how many skulls are in the spin
    return vals.count(val)  # Assuming 4 represents a skull

print("Welcome to the gambling machine!")
cashmoney = int(input("How much money do you want to play with? "))

while cashmoney >= 2:
    print("You have", cashmoney, "dollars.")
    doSpin = input("Do you want to spin? (yes/no) ").strip().lower()
    if doSpin != "yes":
        break
    cashmoney -= 2  # Deduct the cost of a spin
    mySpin = spin()
    # print the spin values as strings
    print(f"Your spin: {mapSpin[mySpin[0]]} {mapSpin[mySpin[1]]} {mapSpin[mySpin[2]]}")
    cashmoney = cashmoney + score(mySpin)

print("Thanks for playing!")
print(f"Your final score: {cashmoney}")