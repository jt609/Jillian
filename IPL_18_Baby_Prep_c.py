# Import random to choose a different activity for the introduction.
import random
from datetime import date, datetime

# There are 16 ounces in one pound.
OUNCES_PER_POUND = 16

def ask_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("That's not a valid whole number. Please try again.")

def ask_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("That's not a valid number. Please try again.")

def ask_date(prompt):
    while True:
        birth_date_text = input(prompt)
        # Check the date format, calendar date, and that it is not in the future.
        if len(birth_date_text) != 8 or not birth_date_text.isdigit():
            print("Please enter a valid date as 8 numbers, like 08262019.")
            continue
        try:
            parsed_birth_date = datetime.strptime(birth_date_text, "%m%d%Y").date()
        except ValueError:
            print("Please enter a valid date as 8 numbers, like 08262019.")
            continue
        if parsed_birth_date > date.today():
            print("Birth date cannot be in the future.")
            continue
        return birth_date_text

def introduce_baby(baby_name, birth_date, current_weight_oz):
    # Pick one activity at random to include in the introduction.
    activities = [
        "eating pizza",
        "dancing",
        "sleeping all day",
        "taking over the world",
    ]
    activity = random.choice(activities)

    # Convert the birth date text into a date so the baby's age can be calculated.
    birth_date = datetime.strptime(birth_date, "%m%d%Y").date()
    today = date.today()
    age_months = (today.year - birth_date.year) * 12 + today.month - birth_date.month
    if today.day < birth_date.day:
        age_months -= 1

    print(f"Meet {baby_name}!")
    print(f"{baby_name} is {activity}.")
    # Show age in days, months, or years and remaining months, as appropriate.
    if age_months == 0:
        age_days = (today - birth_date).days
        day_word = "day" if age_days == 1 else "days"
        print(f"{baby_name} is {age_days} {day_word} old.")
    elif age_months < 12:
        month_word = "month" if age_months == 1 else "months"
        print(f"{baby_name} is {age_months} {month_word} old.")
    else:
        age_years = age_months // 12
        remaining_months = age_months % 12
        year_word = "year" if age_years == 1 else "years"
        month_word = "month" if remaining_months == 1 else "months"
        print(f"{baby_name} is {age_years} {year_word} and {remaining_months} {month_word} old.")

    # Convert ounces to pounds for the introduction.
    weight_pounds = current_weight_oz / OUNCES_PER_POUND
    print(f"{baby_name} currently weighs {weight_pounds:.2f} pounds.")

print("Hello, and welcome to baby prep!")
print("First, let's gather some information about your baby. Please answer the following questions:")
baby_name = input("What is your baby's name? ")
birth_date = ask_date("What is your baby's birth date (8 numbers, MMDDYYYY)? ")
current_weight_oz = ask_int("What is your baby's weight in ounces? ")
baby_height = ask_float("What is your baby's height in inches? ")
introduce_baby(baby_name, birth_date, current_weight_oz)

DEFAULT_MOOD = "content"
mood = DEFAULT_MOOD
eat_count = 0
drink_count = 0
action= "choose"


def eat(current_weight_oz, eat_count):
    current_weight_oz += 11
    eat_count += 1
    return current_weight_oz, eat_count

def poop(current_weight_oz):
    current_weight_oz-= 5
    return current_weight_oz

def drink(current_weight_oz, drink_count):
    current_weight_oz += 8
    drink_count +=1
    return current_weight_oz, drink_count
           
def pee(current_weight_oz):
    current_weight_oz-= 4
    return current_weight_oz

def cry():
    print (baby_name + " is crying")

def ask_to_change_diaper():
    # Keep asking until the user agrees to change the diaper.
    while True:
        answer = input("Would you like to change the diaper? (yes/no) ").lower()
        if answer == "yes":
            print(baby_name + "'s diaper was changed. " + baby_name + " is happy.")
            return
        elif answer == "no":
            cry()
        else:
            print("Please answer yes or no.")

def sleep():
    print (baby_name + " is sleeping")

def display_status(baby_name, current_weight_oz, mood, eat_count, drink_count):
        current_pounds = current_weight_oz / OUNCES_PER_POUND
        print("Here is a summary of your baby's information.")
        print("baby's name: " +baby_name)
        print(f"{baby_name}'s birth date is: {birth_date}")
        print(f"{baby_name} ate {eat_count} times")
        print(f"{baby_name} drank {drink_count} times")
        print(f"{baby_name}'s weight in pounds is: {current_pounds}")
        print(f"{baby_name}'s height in inches is: {baby_height} ")
        print(f"{baby_name}'s mood is {mood}")



while action !="home":
    action = input ("What would you like the baby to do? Choose from: eat, drink, sleep, cry, status, or home. ").lower()

    if action == "eat":
        current_weight_oz, eat_count = eat(current_weight_oz, eat_count)
        mood= "happy"
        print (baby_name + " ate 11ozs")
        if eat_count % 3 == 0:
            current_weight_oz= poop(current_weight_oz)
            print (baby_name+ " pooped")
            mood= "uncomfortable"
            # Ask to change the diaper after the baby poops.
            ask_to_change_diaper()
            mood = "happy"

    elif action == "drink":
        current_weight_oz, drink_count = drink(current_weight_oz, drink_count)
        mood= "content"
        print (baby_name+ " drank 8ozs")
        if drink_count % 3 == 0:
            current_weight_oz= pee(current_weight_oz)
            print (baby_name + " peed")
            mood= "uncomfortable"
            # Ask to change the diaper after the baby pees.
            ask_to_change_diaper()
            mood = "happy"

    elif action == "sleep":
        mood= "content"
        sleep()

    elif action == "cry":
        mood = "sad"
        cry()

    elif action =="status":
        display_status(baby_name, current_weight_oz, mood, eat_count, drink_count)

    elif action == "home":
        break

    else:
        print ("Unknown action, please try again.")
