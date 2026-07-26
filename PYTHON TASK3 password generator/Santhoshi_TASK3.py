#PYTHON TASK3 PASSWORD GENERATOR
#random and string module tiskovali
import random
import string
#user nunchi y or n answer 
def get_choice(message):
    while True:
        choice = input(message).strip().lower()
        # y or n 
        if choice == "yes" or choice == "no":
        #y true,n false
         return choice == "yes"
        print("please enter only yes or no.")
#password generate funtion 
def generate_password(length,use_upper,use_lower,use_numbers,use_symbols):
    # Selected character types anni ee variable lo store avuthayi
    characters = ""

    # Password characters ee list lo store avuthayi
    password = []

    # Uppercase option select chesthe A-Z add avuthayi
    if use_upper:
        characters = characters + string.ascii_uppercase

        # Minimum oka uppercase letter password lo compulsory ga add chesthundi
        password.append(random.choice(string.ascii_uppercase))

    # Lowercase option select chesthe a-z add avuthayi
    if use_lower:
        characters = characters + string.ascii_lowercase

        # Minimum oka lowercase letter add chesthundi
        password.append(random.choice(string.ascii_lowercase))

    # Numbers option select chesthe 0-9 add avuthayi
    if use_numbers:
        characters = characters + string.digits

        # Minimum oka number add chesthundi
        password.append(random.choice(string.digits))

    # Symbols option select chesthe !, @, # laanti symbols add avuthayi
    if use_symbols:
        characters = characters + string.punctuation

        # Minimum oka symbol add chesthundi
        password.append(random.choice(string.punctuation))

    # User ichina password length reach ayye varaku random characters add chesthundi
    while len(password) < length:
        password.append(random.choice(characters))
    
    # shuffle= letters same order lo lekunda mix cheysthundhi
    random.shuffle(password)
    # list ni single string laga convert chysthundhi
    return"".join(password)

#program heading niprint cheysthundhi
print("-------Random Password Generator-------")

#user password generate cheyadaniki loop
while True:
    try:
        #user ki password lenth adagali
        length=int(input("enter password length(minimum 8):"))
        #  8 kante thakuva
        if length<8:
            print("password length must be atleast 8")
            continue
        # Prathi character type kavala vadha ani user ni adugutundi
        use_upper = get_choice("Include uppercase letters? (yes/no): ")
        use_lower = get_choice("Include lowercase letters? (yes/no): ")
        use_numbers = get_choice("Include numbers? (yes/no): ")
        use_symbols = get_choice("Include symbols? (yes/no): ")

        #enni options select chesro count cheyali
        # true=1 false=0
        selected_types = sum([use_upper,use_lower,use_numbers,use_symbols])
        # Strong password kosam minimum 2 types select avvali
        if selected_types < 2:
            print("Please select at least 2 character types.")
            continue

        # Function call chesi password generate chesthundi
        password = generate_password(
            length,
            use_upper,
            use_lower,
            use_numbers,
            use_symbols)
        # Generated password print chesthundi
        print("\nGenerated Password:", password)

        # Inko password create cheyyala ani adugutundi
        again = input("\nGenerate another password? (yes/no): ").strip().lower()

        # y kakapothe program stop avuthundi
        if again != "yes":
            print("Thank you for using Password Generator!")
            break

    # User number badulu letters enter chesthe error handle chesthundi
    except ValueError:
        print("Please enter a valid number.")


        






