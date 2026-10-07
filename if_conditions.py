name = input("Hi there! Welcome to wigglebuy and what is your name? ")
print(f"Hello {name}, nice to meet you!")
country = input("And which country are you from? ").strip().title()

print(f"Oh! I see, {country} is a beautiful country!")
input_state = input("And which state are you buying from? ").strip().title()

if country == "Ghana":
    if input_state in ('Volta', 'Ashanti', 'Central'):
        tax = 0.07
    elif input_state in ('Greater Accra', 'Eastern', 'Western'):
        tax = 0.05
    else:   
        tax = 0.03
else:
    tax = 0.0

print(f"The tax rate for {input_state} in {country} is {tax * 100:.2f}%.")
