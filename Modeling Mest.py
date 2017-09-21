class Person:
    def __init__(self, first_name, last_name, country):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.full_name = first_name + ' ' + last_name

    def __repr__(self):
        return "{} is from {}".format(self.full_name, self.country)


class EITs(Person):
    def __init__(self, first_name, last_name, country, fun_fact):
        Person.__init__(self, first_name, last_name, country)
        self.fun_fact = fun_fact

    def __repr__(self):
        return "The fun fact of {} is: {}".format(self.full_name, self.fun_fact)


class Fellows(EITs):
    def __init__(self, happiness_level, food, subject, first_name, last_name, country, fun_fact):
        EITs.__init__(self, first_name, last_name, country, fun_fact)
        self.happiness_level = happiness_level
        self.food = food
        self.subject = subject

    def __repr__(self):
        return "{} teaches {}, happiness level is: {} and like {}".format(self.full_name,
            self.subject, self.happiness_level, self.food)


class Fellow_Pay(Fellows):
    tract_pay = 0

    def __init__(self, first_name, last_name, country, happiness_level=None, food=None, subject=None, fun_fact=None):
            Fellows.__init__(self, happiness_level, food, subject, first_name, last_name, country, fun_fact)
            Fellow_Pay.tract_pay += 1
            if Fellow_Pay.tract_pay > 4:
                raise Exception("We cannot afford to hire: {}".format(first_name))

    def __repr__(self):
            return "Fellow({} , {})".format(self.full_name, self.country)


eit_details = EITs(first_name="Dare", last_name="Adesina", country="Nigeria", fun_fact="Music")
fellow_details = Fellows(first_name="Andrew", last_name="Francis", country="Ghana", fun_fact="None", subject="Tech",
                         happiness_level=10, food="rice")
print(eit_details)
print(fellow_details)
print("--------Fellow Hire---------")
# try:
for pay in range(5):
    gift = Fellow_Pay(first_name=raw_input('First name:'), last_name=raw_input("Last name:"), country=raw_input("Country"))
    print(gift)
# except Exception as e:
#     if Fellow_Pay.tract_pay > 4:
#             print("We cannot afford to hire: {}".format(self.full_name))










