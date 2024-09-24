import random
import time


class Hand():
    def __init__(self, count):
        self.count = count
        self.dead = False
        self.display = ""

    def state_update(self):
        if self.count == 0:
            self.dead = True
        else:
            self.dead = False

    def hit(self, target):
        target.count = self.count + target.count
        if target.count >= 5:
            target.count -= 5
        self.state_update()
        target.state_update()


Ai_left = Hand(1)
Ai_right = Hand(1)
U_left = Hand(1)
U_right = Hand(1)


def print_screen():
    # A is Ai_left, B is Ai_right C is U_left and D is U_right
    list = [Ai_left, Ai_right, U_right, U_left]
    for i in list:
        if i.count == 0:
            i.display = "[*_*]"
        else:
            i.display = "|"*i.count

    print(f'Ai:    {Ai_left.display}   {Ai_right.display}')
    print(f'You:   {U_left.display}   {U_right.display}')


def tutorial():
    print("Initialising tutorial", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    print("kidding", end="")
    time.sleep(0.5)
    print(", this is a prewritten script...")



# Opening screen
print("Do you want to see the tutorial? [Recommended]")
start = False
while not start:
    answer = input().lower()
    if answer == "no":
        start = True
    elif answer == "yes":
        tutorial()
        start = True
    else:
        print("What?")

# game start
print_screen()


def play():

    while not (Ai_left.dead and Ai_right.dead) and not (U_left.dead and U_right.dead):
        print("")
        print("[Your turn]")
        hit = ""
        using = ""
        while not (hit == "left" or hit == "right") or (hit == "left" and Ai_left.dead) or (hit == "right" and Ai_right.dead):
            hit = input("Hit (Op's) ").lower()
            if not hit == "left" and not hit == "right":
                print("What?")
            if (hit == "left" and Ai_left.dead) or (hit == "right" and Ai_right.dead):
                print("Target is dead")

        while not (using == "left" or using == "right") or (using == "left" and U_left.dead) or (using == "right" and U_right.dead):
            using = input("Using (Your) ").lower()
            if not using == "left" and not using == "right":
                print("What?")
            if (using == "left" and U_left.dead) or (using == "right" and U_right.dead):
                print("That hand is dead")
        if hit == "left":
            if using == "left":
                U_left.hit(Ai_left)
            else:
                U_right.hit(Ai_left)
        else:
            if using == "left":
                U_left.hit(Ai_right)
            else:
                U_right.hit(Ai_right)

        if Ai_left.dead and Ai_right.dead:
            break

        print("")
        print_screen()
        time.sleep(1.5)

        print("")
        print("[Opponent's turn]")
        time.sleep(2)

        options_list = [0, 1, 2, 3]
        if Ai_left.dead:
            if 0 in options_list:
                options_list.remove(0)
            if 1 in options_list:
                options_list.remove(1)
        if Ai_right.dead:
            if 2 in options_list:
                options_list.remove(2)
            if 3 in options_list:
                options_list.remove(3)
        if U_left.dead:
            if 0 in options_list:
                options_list.remove(0)
            if 2 in options_list:
                options_list.remove(2)
        if U_right.dead:
            if 1 in options_list:
                options_list.remove(1)
            if 3 in options_list:
                options_list.remove(3)

        option = random.choice(options_list)
        if option == 0:
            Ai_left.hit(U_left)
        elif option == 1:
            Ai_left.hit(U_right)
        elif option == 2:
            Ai_right.hit(U_left)
        elif option == 3:
            Ai_right.hit(U_right)

        print("")
        print_screen()

    if Ai_left.dead and Ai_right.dead:
        print("You win!")
    else:
        print("Opponent wins")


playing = True
while playing:
    play()
    if input("Do you want to play again? ").lower() == "yes":
        Ai_left = Hand(1)
        Ai_right = Hand(1)
        U_left = Hand(1)
        U_right = Hand(1)
        Ai_left.state_update()
        Ai_right.state_update()
        U_right.state_update()
        U_left.state_update()
        print_screen()
    else:
        playing = False

