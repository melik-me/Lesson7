class Person:
    def __init__(self, full_name="", year_of_birth=1901):
        self.full_name = full_name
        self.year_of_birth = year_of_birth
        id = self.full_name.split()
        try:
            second = id[1]
        except IndexError:
            self.full_name = full_name + " Doe"

        if not 1900 < self.year_of_birth < 2018:
            raise ValueError("Year of birth you've entered is unreal. You broke everything.")

    def name(self):
        id = self.full_name.split()
        return id[0]

    def surname(self):
        id = self.full_name.split()
        return id[1]

    def age(self, years=2018):
        return years - self.year_of_birth


class Employee(Person):
    def __init__(self, full_name="", year_of_birth=1901, position="", experience=0, salary=0):
        Person.__init__(self, full_name, year_of_birth)
        self.position = position
        self.experience = experience
        self.salary = salary

    def rank(self):
        if self.experience < 3:
            return "Junior " + self.position
        elif 3 <= self.experience < 6:
            return "Middle " + self.position
        else:
            return "Senior " + self.position

    def cash_rain(self, increment):
        self.salary += increment

class ITEmployee(Employee):
    def __init__(self, *args, **kwargs):
        Employee.__init__(self, *args, **kwargs)
        self.skills = []

    def add_skills(self, *args):
        for skill in args:
            self.skills.append(skill)


if __name__ == "__main__":
    p = Person("John", 1936)
    print("His name is {} {}, he will be {} years old in the year 2020.".format(p.name(), p.surname(), p.age(2020)))

    e = Employee("\nJudy Doe", 1936, "old stager", 100500, 100500)
    print("{} is a {}!".format(e.full_name, e.rank()))

    print("Her salary was {} ".format(e.salary), end='')
    e.cash_rain(899499)
    print("and now it is {}.".format(e.salary))

    i = ITEmployee("Jane Doe", 1984, "HR", 10, 9999)
    i.add_skills("communication", "head recruiting", "word", "excel", "instagram")
    print("\n{} is a {} with {} skills.".format(i.full_name, i.rank(), i.skills))