"""Program to allow you to loop up hexadecimal colour codes like those at: """

COLOUR_TO_CODE = {"absolutezero": "#0048ba",  "acidgreen": "#b0bf1a", "aliceblue": "#f0f8ff",
                  "alizarincrimson": "#e32636", "amber": "#ffbf00", "amethyst": "#9966cc", "aqua": "#00ffff",
                  "asparagus": "#87a96b", "barnred": "#7c0a02", "beige": "#f5f5dc"}

print(COLOUR_TO_CODE)

colour = input("Enter colour: ").lower()
while colour != "":
    try:
        print(f"{colour} is {COLOUR_TO_CODE[colour]}")
    except KeyError:
        print(f"{colour} not found")
    colour = input("Enter colour: ").lower()


