"""
Prac 07 - Do From Scratch Exercise
Project Management Program
Estimated: 2hrs
Actual:
"""
from prac_07.project import Project


def main():
    """"""

    projects = load_projects()

    print("Welcome to Pythonic Project Management")
    print(f"Loaded len(projects) projects from projects.txt")
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (U)pdate projects")
    print("- (Q)uit")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "D":
            display_projects(projects)
        else:
            print("Invalid menu choice")
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (U)pdate projects")
        print("- (Q)uit")
        choice = input(">>> ").upper()

def load_projects():
    """Read projects.txt and store each record as a Project object in a list """
    with open("projects.txt", "r") as in_file:
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
    for project in projects:
        print(project)



main()