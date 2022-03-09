from functions import play_game, get_top_scores 

while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")
    level  = input("Chose level: easy/hard ")

    if selection.lower() == "a":
        play_game(level)
    elif selection.lower() == "b":
        for score_dict in get_top_scores():
            print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
    else:
        break