import random
import time
import sys


def stratGame(option):
    PrintSequentially("You find yourself standing in an open field,"
                      " filled with grass and yellow wildflowers.")
    PrintSequentially("Rumor has it that a " + option +
                      " is somewhere around here, and has been "
                      " terrifying the nearby village")
    PrintSequentially("In front of you is a house.")
    PrintSequentially("To your right is a dark cave.")
    PrintSequentially("In your hand you hold your trusty"
                      " (but not very effective) dagger.\n")


def fieldPosition(option, items):
    PrintSequentially("Enter 1 to knock on the door of the house.")
    PrintSequentially("Enter 2 to peer into the cave.")
    PrintSequentially("What would you like to do?")
    choice = input("(Please enter 1 or 2.)")
    if choice == "1":
        house(option, items)
    elif choice == "2":
        cave(option, items)
    else:
        fieldPosition(option, items)


def house(option, items):
    PrintSequentially("You approach the door of the house.")
    PrintSequentially("You are about to knock when the door"
                      " opens and out steps a " + option + ".")
    PrintSequentially("Eep! This is the wicked " + option + "'s house!")
    PrintSequentially("The " + option + " attacks you!")
    if "sward" not in items:
        PrintSequentially("You feel a bit under-prepared for this, "
                          "what with only having a tiny dagger.")
    while True:
        choice = input("Would you like to (1) fight or (2) run away?")
        if choice == "1":
            fight(option, items)
        elif choice == "2":
            RunAway(option, items)
        else:
            fieldPosition(option, items)


def fight(option, items):
    if "sward" in items:
        PrintSequentially("As the " + option +
                          " moves to attack, you unsheath your new sword.")
        PrintSequentially("The Sword of Ogoroth shines brightly in your "
                          "hand as you brace yourself for the "
                          "attack.")
        PrintSequentially("But the " + option +
                          " takes one look at your shiny new toy and "
                          "runs away!")
        PrintSequentially("You have rid the town of the " +
                          option + ". You are victorious!")
    else:
        PrintSequentially("You do your best...")
        PrintSequentially("but your dagger is no match for the "
                          + option + ".")
        PrintSequentially("You have been defeated!")
    returnGame = input("Would you like to play again? (y/n)")
    GameAgain(returnGame)


def RunAway(option, items):
    PrintSequentially("You run back into the field. "
                      "Luckily, you don't seem to have been followed.")
    fieldPosition(option, items)


def cave(option, items):
    if "sward" in items:
        PrintSequentially("You peer cautiously into the cave.")
        PrintSequentially("You've been here before, and gotten "
                          "all the good stuff. It's just an empty cave now.")
        PrintSequentially("You walk back to the field.")
    else:
        PrintSequentially("You peer cautiously into the cave.")
        PrintSequentially("It turns out to be only a very small cave.")
        PrintSequentially("Your eye catches a glint of metal behind a rock.")
        PrintSequentially("You have found the magical Sword of Ogoroth!")
        PrintSequentially("You discard your silly old dagger and "
                          "take the sword with you.")
        PrintSequentially("You walk back out to the field.")
        items.append("sward")
    fieldPosition(option, items)


def GameAgain(returnGame):
    if returnGame == 'y':
        PrintSequentially("Excellent! Restarting the game ...")
        PlayGame()
    elif returnGame == 'n':
        PrintSequentially("Thanks for playing! See you next time.")
        sys.exit(0)


def PrintSequentially(message):
    print(message)
    time.sleep(2)


def PlayGame():
    items = []
    option = random.choice([
        "wicked fairie", "pirate", "dragon", "troll", "gorgon"])
    stratGame(option)
    fieldPosition(option, items)


PlayGame()
