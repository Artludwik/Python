print("""  
░█▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀█ █▀▀█ 　 ░█▀▀█ ─▀─ █▀▀█ █──█ █▀▀ █▀▀█
░█─── █▄▄█ █▀▀ ▀▀█ █▄▄█ █▄▄▀ 　 ░█─── ▀█▀ █──█ █▀▀█ █▀▀ █▄▄▀
░█▄▄█ ▀──▀ ▀▀▀ ▀▀▀ ▀──▀ ▀─▀▀ 　 ░█▄▄█ ▀▀▀ █▀▀▀ ▀──▀ ▀▀▀ ▀─▀▀  """)
activity = True
while activity:
    def equation(text, key, direction):
        end_text = ""
        if choice == 'decode':
                key *= -1
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = (position + key) % len(alphabet)
                new_char = alphabet[new_position]
                end_text += new_char
            else:
                end_text += char
        print(f"\nHere's {choice}d result:{end_text}\n")
        
    # Extended alphabet
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2',
                '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$',
                '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[',
                ']', '{', '}', ';', ':', "'", '"', '<', '>', ',', '.',
                '/', '|', '?', '\\', ' ']
    
    # Added user error handling for 'encode' or 'decode' words.
    choice_value = True
    while choice_value:
        choice = input("\nType 'encode' to encrypt or 'decode' to decrypt:\n")
        if choice == 'encode' or choice == 'decode':
            choice_value = False
        else:
            print("\nPlease use only 'encode' or 'decode' words\n")
            choice_value = True

    message = input("\nType your message:\n")
    
    # Added user error handling for non-integer characters.
    while True:
        try:
            shift = (int(input("Type your shift:\n")))
            break
        except ValueError:
            print("Sorry, please chose only numbers\n")
            
    equation(text=message, key=shift, direction=choice)
    
    end_message = input("Type 'yes' if you want to go again, otherwise type 'no'.\n")
    
    if end_message == 'yes':
        activity = True
    elif end_message == 'no':
        activity = False
        print("See you next time!")
