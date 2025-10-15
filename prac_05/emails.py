"""
CP1404 Prac 5
Emails
Estimated: 1hr
Actual: 1hr 30 mins
"""


def main():
    """Store emails and names in dictionary"""
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        name_input = input(f"Is your name {name}? (Y/n) ")
        if name_input.upper() != "Y" and name_input != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract name from email address"""
    name_part = email.split("@")[0]  # ['lindsay.ward']
    name_parts = name_part.title().split(".")  # [Lindsay, Ward]

    name = " ".join(name_parts)  # "Lindsay Ward"
    return name


main()
