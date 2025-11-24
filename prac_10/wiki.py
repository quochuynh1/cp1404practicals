"""
Prac 10 - Wiki
"""
import wikipedia


def main():
    """Program that prompts the user for a page title or search phrase, then prints some details of that page. Use a loop that continues doing this until the user enters blank input."""

    user_input = input("Enter page title or search phrase: ")
    while user_input != "":
        try:
            page_details = wikipedia.page(user_input)
            print(page_details.title)
            print(page_details.summary)
            print(page_details.url)
            print()
        except wikipedia.exceptions.PageError:
            print(f"Page id '{user_input}' does not match any pages. Try another id!")
        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search: ")
            print(e.options)
        user_input = input("Enter page title or search phrase: ")
    print("Thank you")


main()
