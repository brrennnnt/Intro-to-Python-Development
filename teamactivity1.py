print("Please enter the following information:")
print("")
#variables
first = input("First name: ")
last = input("Last name: ")
email = input("Email address: ")
phone = input("Phone number: ")
job = input("Job title: ")
id = input("ID Number: ")
hair = input("Hair color: ")
eyes = input("Eye color: ")
month = input("Month started: ")
training = input("Traing completed yes/no: ")
#display
print("")
print("The ID Card is: ")
print("")
print(f"{last.upper()}, {first.capitalize()}")
print(job.title())
print(f"ID: {id} ")
print(" ")
print(email.lower())
print(phone)
print("")
print(f"Hair: {hair.capitalize():15} Eyes: {eyes.capitalize()}")
print(f"Month: {month.capitalize():14} Training: {training.capitalize()}")