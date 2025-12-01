"""
Prac 07 - Do From Scratch Exercise
Project Management Program
Estimated: 2hrs
Actual: Few days (Approx 3hrs 30mins total)
"""

from prac_07.project import Project
from datetime import datetime

MENU = ("Welcome to Pythonic Project Management\n"
        "Loaded {len(projects)} projects from {filename}\n"
        "- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate projects")

def main():
    """Program to keep track of complete and incomplete projects"""
    filename = "projects.txt"
    projects = load_projects(filename=filename)

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = get_valid_filename()
            projects = load_projects(filename=filename)
            print(f"Projects loaded from {filename}")
        elif choice == "S":
            filename = input("Enter filename to save projects to: ")
            save_projects(projects, filename=filename)
            print(f"Projects saved to {filename}")
        elif choice == "D":
            display_projects(projects)
        elif choice == "U":
            update_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_project(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_prompt = input(f"Would you like to save to {filename}? ").lower()
    if save_prompt != "yes":
        print("Thank you for using custom-built project management software.")
    else:
        save_projects(projects, filename=filename)
        print(f"Projects saved to {filename}")
        print("Thank you for using custom-built project management software.")


def get_valid_filename():
    """Prompt the user for a valid filename until it is either not black, or exists in the file directory"""
    try:
        filename = input("Enter filename: ")
    except FileNotFoundError:
        print("File not found")
    return filename


# TODO: create exception based error checking to ask for a valid filename until it is either not blank, or it exists.


def get_valid_int(prompt):
    """Prompt the user to enter a number until it is valid"""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(prompt))
            if number <= 0:
                print("Number must be > 0")
            else:
                is_valid_input = True
                return number
        except ValueError:
            print("Invalid input - please enter a valid number")
    return None


def load_projects(filename):
    """Read projects.txt and store each record as a Project object in a list """
    with open(filename, "r") as in_file:
        projects = []
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            name = parts[0]
            start_date = parts[1]
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
        return projects


def display_projects(projects):
    """Display two groups: incomplete projects; completed projects, both sorted by priority"""
    print("Incomplete projects: ")
    for project in projects:
        if int(project.completion_percentage) < 100:
            print(f"\t{project}")

    print("Complete projects: ")
    for project in projects:
        if int(project.completion_percentage) == 100:
            print(f"\t{project}")


# TODO: Sort projects by priority

def update_projects(projects):
    """Choose a project, then modify the completion % and/or priority - the user can leave either input blank to retain existing values"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    while True:
        try:
            project_choice = int(input("Project choice: "))
            selected_project = projects[project_choice]
            print(selected_project)
            break
        except (ValueError, IndexError):
            print("Invalid project number")

    while True:
        try:
            new_percentage = input("New percentage: ")
            if new_percentage != "":
                selected_project.completion_percentage = new_percentage
                break
            else:
                break
        except ValueError:
            print("Invalid input")

    while True:
        try:
            new_priority = input("New priority: ")
            if new_priority != "":
                selected_project.new_priority = new_priority
                break
            else:
                break
        except ValueError:
            print("Invalid input")


def add_project(projects):
    """Ask the user for the inputs and add a new project to memory"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start datee (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percentage_complete = int(input("Percentage complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, percentage_complete)
    projects.append(new_project)


def filter_projects_by_date(projects):
    """Ask the user for a date and display only projects that start after that date, sorted by date"""
    date = input("Show projects that start after datee (dd/mm/yyyy): ")

    filter_date = datetime.strptime(date, "%d/%m/%Y").date()

    filtered_projects = []
    for project in projects:
        project_date = datetime.strptime(project.start_date, "%d/%m/%Y").date()
        if project_date > filter_date:
            filtered_projects.append(project)

    for project in filtered_projects:
        print(project)

    # TODO: Sort filtered projects by date


def save_projects(projects, filename="projects.txt"):
    """Prompt the user for a filename to save projects to and save them"""
    with open(filename, "w") as out_file:
        for project in projects:
            out_file.write(
                f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


main()
