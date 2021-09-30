"""A simple game to demonstrate coding skills."""
__author__: str = "730401999"


def main() -> None:
    """Starts program."""
    greet()
    global player
    global points
    i: int = 0
    while i < 5:
        print(f"Your current score out of 10 points possible is: {points}.")
        print("Please choose one of the following:")
        print("1: Assess GPA")
        print("2: Assess extra curriculars")
        print("3: Assess Shadowing and Clinical Experience")
        print("4: Randomness factor")
        print("5: End Game")
        choice_one: int = int(input())
        if choice_one == 1:
            print("You selected gpa")
            b: str = input("Are you applying to MD or DO schools? ")    
            if b == "MD":
                print("You have selected the MD program!")
                a: float = float(input(player + ", what is your GPA '('0-4.0')' "))    
                points = points + md_gpa(a)
            else:
                print("You have selected the DO program!")
                a: float = float(input(player + ", what is your GPA '('0-4.0')' "))
                points = points + do_gpa(a)
            i += 1 
        if choice_one == 2:
            print("You have selected extracurriculars!")
            extras: int = int(input("How many extracurricular activites were you a part of? "))
            points = points + ec(extras)
            i += 1
        if choice_one == 3:
            print("You have selected shadowing/clinical experience!")
            points = points + shadowing()
            i += 1

        if choice_one == 4:
            print("You have selected the randomness factor!")
            print("Medical school admissions can be weirdly decided, therfore a part of your likely of getting in will be evauluated as such!")
            points = points + randomness()
            i += i
        if choice_one == 5:
            print(f"You have chosen to end the game, {player}!") 
            print(final_score(points))
            print(10 * HAPPY_FACE)
            i = 5
    print(f"You have reached the end of the game, {player}!") 
    print(final_score(points))
    print(10 * HAPPY_FACE)


def greet() -> None:
    """Welcomes player and records name."""
    global player
    player = input("What is your name? ")    
    print("Hello, " + player + ", welcome to Medical School Admissions Adventure!!")
    print("This simulation will take you through your undergraduate achievements to determine your possibilies of getting into Medical School.")
    print("As you go through each aspect of the application we will update you on your total points out of 10!")


def md_gpa(a: float) -> int:
    """Evaluates MD programs GPA."""
    if a > 3.75:
        return 4
    elif a > 3.5:
        return 3
    elif a > 3.25:
        return 2
    elif a > 3.0:
        return 1
    else:
        return 0 


def do_gpa(a: float) -> int:
    """Evaluates DO school GPA."""
    if a > 3.25:
        return 4
    elif a > 3.0:
        return 3
    elif a > 2.5:
        return 2
    elif a > 2.25:
        return 1
    else:
        return 0 


def ec(extras: int) -> int:
    """Evaluates extracurriculars."""
    points: int = 0
    if extras > 1:
        points += 1
    elif extras > 0:
        points += 1
    elif extras <= 0:
        points == 0
    return points


def randomness() -> int:
    """Evavalutes random aspect of admissions."""
    from random import randint 
    t: int = 0
    points: int = 0 
    while t < 2:
        answer: int = randint(1, 3)
        guess: int = int(input("Pick a number 1-3: "))
        if answer == guess:
            print("Correct!")
            points += 1
        else:
            print("Incorrect!")
        t += 1
    return points


def shadowing() -> int:
    """Evaluates the shawdowing and clinical experience."""
    points: int = 0
    u: str = input("Do you have shadowing experience? ")
    v: str = input("Do you have clinical experience? ")
    if u == "yes":
        points += 1
    if v == "yes":
        points += 1
    return points   


def final_score(x: int) -> str:
    """Determines probability from score."""
    x = (points) 
    xy = "You have a " + str(x) + "/10 chance of getting into medical school!"
    return xy
    

player: str = ""
points: int = 0
HAPPY_FACE = "\U0001F604"

if __name__ == "__main__":
    main()