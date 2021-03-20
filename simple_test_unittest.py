import datetime as dt 
import random
import calendar


def generate_date():
    year = random.randint(1900, dt.date.today().year)
    month = random.randint(1, 12)
    day = random.randint(1, calendar.monthrange(year, month)[1])
    return dt.date(year, month, day)


print(generate_date())



import unittest

class TestDateGenerator(unittest.TestCase):

    def test_check_year(self):
        self.assertTrue(1900 <= generate_date().year <= dt.date.today().year)

    def test_check_month(self):
        gen_date = generate_date()
        self.assertTrue(0 < gen_date.month < 13)

    def test_check_count_of_day(self):
        gen_date = generate_date()
        self.assertTrue(
            calendar.monthrange(gen_date.year, gen_date.month)[1] >= gen_date.day
            )


if __name__ == '__main__':
    unittest.main()