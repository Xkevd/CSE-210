from operator import truediv
import random


def main ():

        
    current_card = Cards.display_card()
    answer = "y"
    while Choices.points>0 and answer=="y":
        print(f"The card is {current_card}")
        previous_card = current_card
        current_card = Cards.display_card()
        Choices.options(previous_card, current_card)
        print(f"Your next card was: {current_card}")
        print(f"Your score is: {Choices.points}")
        answer = Points.game_over()
    print("End")
    pass


class Cards:
     
    def display_card():
        picked_card = random.randint(1,13)
        return picked_card

class Choices:
    points = 300

    def options(previous, current):
        option = input("Higher or lower? [h/l] ")
        if (option == "h") and current>previous:
            Choices.points += 100
        elif (option == "h") and current<previous:
            Choices.points -=75
        elif (option == "l") and current<previous:
            Choices.points +=100
        elif (option == "l") and current>previous:
            Choices.points -=75
        
        return 0<Choices.points

class Points:


    def game_over():
        if Choices.points > 0:
            answer_yes = input("Would you like to keep playing? [y/n]")
        else:
            print("Game Over")
            answer_yes = "n"
        return answer_yes


if __name__ == "__main__":
    main()

    

















