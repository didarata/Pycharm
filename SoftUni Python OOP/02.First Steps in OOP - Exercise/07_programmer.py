class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, course_language, skills_earned):
        if self.language == course_language:
            self.skills += skills_earned

            return f"{self.name} watched {course_name}"

        return f"{self.name} does not know {course_language}"

    def change_language(self, new_language, skills_needed):
        if self.skills >= skills_needed and new_language != self.language:
            previous_language = self.language
            self.language = new_language

            return f"{self.name} switched from {previous_language} to {new_language}"

        elif self.skills >= skills_needed and new_language == self.language:

            return f"{self.name} already knows {new_language}"

        else:

            return f"{self.name} needs {skills_needed - self.skills} more skills"



# https://judge.softuni.org/Contests/Compete/Index/1935#6

programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
