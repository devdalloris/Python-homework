class Date:
    def __init__(self, month, day, year):
        self.month=month
        self.day=day
        self.year=year
        self.month_list=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        if day<0 and day>31:
            raise ValueError
        if month<0 and month>12:
            raise ValueError
    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'
    def second_format(self):
       print(f'{self.month_list[self.month-1]} {self.day}, {self.year}')
    def third_format(self):
        print(f'{self.day} {self.month_list[self.month-1]}, {self.year}')       

p=Date(12, 25, 2018)
print(p)
p.second_format()
p.third_format()