name = input("Hi there! What is your name? ")
country = input(f"Hello {name}, nice to meet you! And where are you from? ").strip().title()

if country == "Singapore":
    print("Oh! I see, Singapore is a fine, beautiful island nation!")
else:
    print(f"Oh! I see, {country} is a beautiful country!")

#Non-destructive: It returns a new string and does not
#  modify the original variable unless you reassign it (e.g., country = country.upper()).

#Non-alphabetic characters: Numbers, punctuation, 
# and symbols remain unchanged (e.g., 'hello 123!'.upper() returns 'HELLO 123!').
   
#In your original code, "Singapore" in line 3 was doing two things at once: checking the specific country name AND checking the exact casing.

#Here is what was happening step-by-step:

#String Transformation (.capitalize()): This changes how the letters look.
#  It forces the first letter to be uppercase and every other letter to be lowercase (e.g., "sInGaPoRe" becomes "Singapore").

#Comparison (== "Singapore"): The == operator doesn't care how you transformed the string; it asks:
#  "Is the resulting string literally the country Singapore?"

#So if a user entered "singapore", .capitalize() made it "Singapore", and line 3 evaluated to True.
#  But if the user entered "ghana", .capitalize() made it "Ghana", which did not equal "Singapore", so it evaluated to False.

#If your goal is just to format the letters nicely regardless of what country they type, you don't need if country == "Singapore".
#  You simply format the input variable and print it directly
#country = input("Where are you from? ").strip().title()

# 'country' now has proper capitalization (e.g., "Ghana", "South Africa")
#print(f"Oh! I see, {country} is a beautiful country!")