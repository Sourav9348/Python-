import re



def main():
    print(convert(input("Hours: ")))


def convert(s):
    correct_format = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if correct_format:
        group = correct_format.groups()
        if int(group[1]) > 12 or int(group[5]) > 12:
            raise ValueError
        first_time = new_format(group[1], group[2], group[3])
        second_time = new_format(group[5], group[6], group[7])
        return first_time + " to " + second_time
    else:
        raise ValueError

def new_format(hour, minute, am_pm):
    if am_pm == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12

    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)

    if minute == None:
        new_minute = ":00"
        new_time = f"{new_hour:02}" + new_minute
    elif int(minute) >= 60:
        raise ValueError

    else:
        new_time = f"{new_hour:02}" + ":" + minute
    return new_time



if __name__ == "__main__":
    main()


