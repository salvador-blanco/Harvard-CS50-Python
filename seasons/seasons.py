from datetime import date
import inflect
import re
import sys

class DateInMinutes():
    def __init__(self, birthday_year, birthday_month, birthday_day):
        try:
            self.birthday = date(birthday_year, birthday_month, birthday_day)
        except TypeError:
            raise ValueError

        self.today_date = date.today()


        self.delta_time = self.today_date - self.birthday
        self.age_in_minutes = int(self.delta_time.total_seconds()/60)
        self.p = inflect.engine()

    @classmethod
    def get(cls):
        birdthay = input("Date of Birth: ").strip()
        birdthay = re.search(r"^(\d{4})-(\d{2})-(\d{2})$", birdthay)
        if birdthay:
            year = int(birdthay[1])
            month = int(birdthay[2])
            day = int(birdthay[3])
        else:
            sys.exit("Invalid date")

        return cls(year, month, day)

    def get_str(self):
        return self.p.number_to_words(self.age_in_minutes, andword = "").capitalize() + " minutes"

    def __str__(self):
        return self.get_str()

def main():
    user_age = DateInMinutes.get()
    print(user_age)

if __name__ == "__main__":
    main()
