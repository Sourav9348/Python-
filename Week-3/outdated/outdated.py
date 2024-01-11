months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    while True:
        date = input('Date: ')
        try:
            month,day,year = date.split('/')
            month = int(month)
            day = int(day)
            year = int(year)
            if (int (month) > 0 and int(month) < 13) and (int(day) > 0 and int(day) < 32):
                if year >= 1000 and year <= 9999:
                    print (year, f'{month:02}',f'{day:02}', sep='-')
                    break
        except:
            try:
                if "," in date:
                    month,day,year = date.split(' ')
                    day = day.replace(',','')
                    day = int(day)
                    year = int(year)
                    if month in months and (int(day) > 0 and int(day) < 32):
                        if year >= 1000 and year <= 9999:
                            month= (months.index (month)+1)
                            print (year, f'{month:02}',f'{day:02}', sep = '-')
                            break
            except:
                pass

main()
