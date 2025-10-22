"""
Prac 06 - Programming Language
Estimated: 40 mins
Actual: 25 mins
"""
from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

print(python.is_dynamic())

languages = [python, ruby, visual_basic]

for language in languages:
    if language.is_dynamic():
        print(language.name)

