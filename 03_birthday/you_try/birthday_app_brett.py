import datetime


def print_header():
    print()
    print('--------------------------------')
    print('         Birthday App')
    print('--------------------------------')


def get_birthday():
    print('When were you born?')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(year=target_date.year, month=original_date.month, day=original_date.day)
    dt = this_year - target_date
    return dt.days


def print_birthday_information(days):
    # your birthday passed
    if days < 0:
        print("You already had your birthday, it was {0} days ago".format(-days))
    # your birthday is upcoming
    elif days > 0:
        print("Your birthday is in {0} days".format(days))
    # today is your birthday
    else:
        print("It is your birthday!")


def main():
    print_header()
    bday = get_birthday()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_information(number_of_days)


main()
