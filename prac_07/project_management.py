"""
Prac 07 - Do From Scratch Exercise
Project Management Program
Estimated: 2hrs
Actual:
"""
from prac_03.capitalist_conrad import out_file
from prac_07.project import Project
from datetime import datetime


def main():
    """"""
    filename = "projects.txt"
    projects = load_projects()

    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {filename}")
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate projects")
    print("- (Q)uit")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename: ")
            projects = load_projects(filename=filename)
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
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate projects")
        print("- (Q)uit")
        choice = input(">>> ").upper()
    save_prompt = input(f"Would you like to save to {filename}? ").lower()
    if save_prompt != "yes":
        print("Thank you for using custom-built project management software.")
    else:
        save_projects(projects, filename=filename)
        print(f"Projects saved to {filename}")
        print("Thank you for using custom-built project management software.")


def load_projects(filename="projects.txt"):
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
    """"""
    print("Incomplete projects: ")
    for project in projects:
        if project.completion_percentage < 100:
            print(f"\t{project}")

    print("Complete projects: ")
    for project in projects:
        if project.completion_percentage == 100:
            print(f"\t{project}")


def update_projects(projects):
    """"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_choice = int(input("Project choice: "))
    selected_project = projects[project_choice]

    new_percentage = int(input("New percentage: "))
    selected_project.completion_percentage = new_percentage

    new_priority = int(input("New priority: "))
    selected_project.priority = new_priority


def add_project(projects):
    """"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start datee (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percentage_complete = int(input("Percentage complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, percentage_complete)
    projects.append(new_project)


def filter_projects_by_date(projects):
    """"""
    date = input("Show projects that start after datee (dd/mm/yyyy): ")

    filter_date = datetime.strptime(date, "%d/%m/%Y").date()

    filtered_projects = []
    for project in projects:
        project_date = datetime.strptime(project.start_date, "%d/%m/%Y").date()
        if project_date > filter_date:
            filtered_projects.append(project)

    for project in filtered_projects:
        print(project)


def save_projects(projects, filename="projects.txt"):
    with open(filename, "w") as out_file:
        for project in projects:
            out_file.write(
                f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


main()
