def express_love():
    recipient = input("To whom would you like to express your love? ")
    love_message = input(f"What message do you want to send to {recipient}? ")

    print(f"Dear {recipient},\n")
    print(f"{love_message}\n")
    print("With all my love,")
    print("Your Name")


express_love()
