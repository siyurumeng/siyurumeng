import datetime as dt

class person:
    # YOUR CODE HERE
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
    
    def get_age(self):
        today = datetime.timedelta(year=2017, month = 12, day = 26)
        form = '%Y-%m-%d'
        birthday_dt= datetime.datetime.strptime(self.birthday, form)
        diff = today - birthday_dt
        self.years = diff.year
        self.days = diff.day
        return (self.years, self.days)

person('LiLei', '1999-08-23').get_age()
