#Title: Acupuncture - Heart Helper 

# Greeting message
print("Welcome to the Heart Helper - Five Element Acupuncture Program!")

# Initialize a loop to let the user learn about multiple points
while True:
    # Asking the user for input
    user_input = input(
        "Which Heart acupuncture point would you like to learn about? (Enter HT-9, HT-8, HT-7, HT-4, HT-3, or 'exit' to quit): "
    ).lower()

    # Decision logic for valid inputs
    if user_input == "ht-9":
        print("HT-9 (Shaochong) - Wood Element Point")
        print("Location: On the radial side of the pinky finger, at the corner of the nail.")
        print("Benefits: Clears heat, revives consciousness, and benefits the tongue and eyes.")
    elif user_input == "ht-8":
        print("HT-8 (Shaofu) - Fire Element Point")
        print("Location: On the palm, between the 4th and 5th metacarpal bones.")
        print("Benefits: Clears heat from the Heart, calms the mind, and alleviates palpitations.")
    elif user_input == "ht-7":
        print("HT-7 (Shenmen) - Earth Element Point")
        print("Location: On the wrist crease, in line with the little finger.")
        print("Benefits: Calms the mind, relieves anxiety, and promotes sleep.")
    elif user_input == "ht-4":
        print("HT-4 (Lingdao) - Metal Element Point")
        print("Location: On the radial side of the wrist, 1.5 cun above the wrist crease.")
        print("Benefits: Calms the mind, alleviates sadness, and clears heat.")
    elif user_input == "ht-3":
        print("HT-3 (Shaohai) - Water Element Point")
        print("Location: At the elbow, in the depression between the medial end of the elbow crease and the medial epicondyle.")
        print("Benefits: Clears heat, calms the mind, and soothes pain.")
    elif user_input == "exit":
        print("Thank you for using the Heart Helper - Acupuncture Program! Goodbye!")
        break
    else:
        # Inform the user about invalid input and loop again
        print("Invalid input. Please try again.")
