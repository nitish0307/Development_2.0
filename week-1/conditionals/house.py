name = input("Who are you talking about? ")

match name:
    case "Nitish" | "Ritesh" | "Nibha":
        print("Yea, I know him!")
    case "Prakash":
        print("Not enough close")
    case _:
        print("I don't know!")
