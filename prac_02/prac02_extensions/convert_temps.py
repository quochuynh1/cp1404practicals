"""Program to read temperatures from text file, convert from Fahrenheit to Celsius, and write to another file"""


def main():
    with open("temps_input", "r") as file:
        contents = file.read()
        print(f"temps_input contains: {contents}")

    # with open("temps_output", "w") as file:
    #     file.write = f"{contents} in Celsius is:", convert_to_celcius(contents)


def convert_to_celcius(contents):
    celsius = 5 / 9 * (contents - 32)
    return celsius


main()
