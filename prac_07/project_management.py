"""
Prac 07 - Do From Scratch Exercise
Project Management Program
Estimated: 2hrs
Actual:
"""
from prac_07.project import Project


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
        elif choice == "D":
            display_projects(projects)
        elif choice == "U":
            update_projects(projects)
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
    if new_percentage:
        selected_project.completion_percentage = new_percentage

    new_priority = int(input("New priority: "))
    if new_priority:
        selected_project.priority = new_priority


def add_project(projects):
    """"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start datee (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percentage_complete = int(input("Percentage complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, percentage_complete)
    projects.append(new_project)


main()
