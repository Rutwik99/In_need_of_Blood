from datetime import datetime
from dateutil.relativedelta import relativedelta

def get18_back():
    seventeen_yrs_ago = str(datetime.now() - relativedelta(years=17))
    sis_yrs_ago = str(datetime.now() - relativedelta(years=66))
    max_year_back = seventeen_yrs_ago.split(' ')
    min_year_back = sis_yrs_ago.split(' ')

    return min_year_back[0], max_year_back[0]


print(get18_back())


def findAge(current_date, current_month, current_year,
            birth_date, birth_month, birth_year):
    # if birth date is greater then current birth_month
    # then donot count this month and add 30 to the date so
    # as to subtract the date and get the remaining days

    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (birth_date > current_date):
        current_month = current_month - 1
        current_date = current_date + month[birth_month - 1]

    # if birth month exceeds current month, then
    # donot count this year and add 12 to the
    # month so that we can subtract and find out
    # the difference
    if (birth_month > current_month):
        current_year = current_year - 1
        current_month = current_month + 12

    # calculate date, month, year
    calculated_date = current_date - birth_date
    calculated_month = current_month - birth_month
    calculated_year = current_year - birth_year
    return str(calculated_year)


def send_to_find_age(birth_day):
    cur_date = str(datetime.now()).split(' ')
    cur_date_array = cur_date[0].split('-')
    birth_day_array = birth_day.split('-')
    return findAge(int(cur_date_array[2]), int(cur_date_array[1]), int(cur_date_array[0]), int(birth_day_array[2]), int(birth_day_array[1]), int(birth_day_array[0]))

print(send_to_find_age('1999-10-27'))