

    #name = input("Hi there! What is your name? ")
#country = input(f"Hello {name}, nice to meet you! and where are you from? ")
#if country.capitalize() == "Singapore":
 #   print("Oh! I see, Singapore is a beautiful country!")
#else:
 #   print(f"Oh! I see, {country} is a beautiful country!")

name = input("Hi there! What is your name? ")
country = input(f"Hello {name}, nice to meet you! And where are you from? ").strip().title()

#.strip() is a method of the string object that removes any leading and trailing whitespace characters from the string.
#.title() is a method of the string object that capitalizes the first letter of each word in the string and converts the rest of the letters to lowercase.
print(f"Oh! I see, {country} is a beautiful country!")

