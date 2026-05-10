import random # random module

score = 0 # initial score
def check(multiply,usr_input):
    global score
    # for incorrect answers
    if multiply != usr_input:
        # score decrease (-2)
        score -= 2
        print("Wrong Answer ❌❌💀💀")
        print(f"Score = {score}")
        print(f"The Correct✅ Answer is {a} x {b} = {multiply}✅")
    else:
        # score increase +1
        score += 1
        print("Correct Answer ✅✅😎🥇")
        print(f"Score = {score}")

# Main loop
def main():
    # Main loop
    while True:
        # enter tables (from,to) 
        a = random.randint(6,11) # tables form 6 to 11
        # tables second number by default 1 to 10
        b = random.randint(1,10)
        # error and exception handling
        while True:
            try:
                # input of answers
                usr_input = int(input(f"{a} x {b} = "))
                break
            except TypeError:
                print("Enter Correctly")
                continue
            except ValueError:
                print("Enter Correctly")
                continue
        # multiply for correct answer by system
        multiply = a*b
        # checks for the answer
        check(multiply, usr_input)

# for import safety
if __name__ == "__main__":
    main()
