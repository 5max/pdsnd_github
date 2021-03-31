import time
import pandas as pd

CITY_DATA = { 'chicago': 'D:/Studium Arbeit/IT/Udacity Programming for Data Science with Python/4 Udacity Introduction to Programming/Project/chicago.csv',
              'new york city': 'D:/Studium Arbeit/IT/Udacity Programming for Data Science with Python/4 Udacity Introduction to Programming/Project/new_york_city.csv',
              'washington': 'D:/Studium Arbeit/IT/Udacity Programming for Data Science with Python/4 Udacity Introduction to Programming/Project/washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    citydict = {"chicago":"chicago","the windy city":"chicago","chi-city":"chicago","chi-town":"chicago","chi":"chicago","chic":"chicago",
                "washington":"washington","wa":"washington","capitol":"washington",
                "new york city":"new york city","ny":"new york city","nyc":"new york city","n y":"new york city","newyorkcity":"new york city",
                "big apple":"new york city","new york":"new york city","newyork":"new york city"}
    city = input("Tell me the name of the city you want to see data for, chicago or new york city or washington?\n").lower().strip()

    # get city input
    while city not in citydict:
        city = input("You misspelled the city, try another synonym for the city chicago or new york city or washington.\n").lower().strip()

    if city in citydict:
        city = citydict[city]


    # Determine if the user wants to filter at all
    filter = input("Would you like to filter the data by month or day or both or not at all? Type month or day or both or all or m or d or b or a.\n").lower().strip()

    while filter not in ["month","day","both","all","m","d","b","a"]:
        filter = input("Just type month or day or both or all.\n").lower().strip()


    # get user input for month (all, january, february, ... , june)
    def monthly():
        monthdict = {"january":1, "jan":1, "1":1, "february":2, "feb":2, "2":2, "march":3, "mar":3, "3":3, "april":4, "apr":4, "4":4, "may":5,
                     "5":5, "june":6, "jun":6, "6":6}
        month = input("Which month? January, February, March, April, May, or June?\n").lower().strip()

        while month not in monthdict:
            month = input("Just type the name or the short name or the number of the month\n").lower().strip()

        if month in monthdict:
            month = monthdict[month]
        return month


    # get user input for day of week (all, monday, tuesday, ... sunday)
    def daily():
        daydict = {"monday":0,"mon":0,"0":0,"tuesday":1,"tue":1,"1":1,"wednesday":2,"wed":2,"2":2,"thursday":3,"thu":3,"3":3,"friday":4,"fri":4,"4":4,"saturday":5,"sat":5,"5":5,"sunday":6,"sun":6,"6":6}
        day = input("Which day of the week? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday?\n").lower().strip()

        while day not in daydict:
            day = input("Just type the name or the short name or the number of the day of the week, Monday is 0, Tuesday is 1, Sunday is 6...\n").lower().strip()

        if day in daydict:
            day = daydict[day]
        return day


    # set the month and day variables depending on what was entered in filter
    if filter == "day" or filter == "d":
        day = daily()
    else:
        day = "all"

    if filter == "month" or filter == "m":
        month = monthly()
    else:
        month = "all"

    if filter == "both" or filter == "b":
        month = monthly()
        day = daily()

    if filter == "all" or filter == "a":
        month = "all"
        day = "all"


    # just printing out the filters which the user chose
    to_month_name = {1 : "January", 2 : "February", 3 : "March", 4 : "April", 5 : "May", 6 : "June", "all" : "all"}
    to_day_name = {0 : "Monday", 1 : "Tuesday", 2 : "Wednesday", 3 : "Thursday", 4 : "Friday", 5 : "Saturday", 6 : "Sunday", "all" : "all"}

    print("\nYour settings are: ", "\nCity: ", city.title(), "\nMonth: ", to_month_name[month], "\nDay: ", to_day_name[day])
    print('-'*80)
    # month from 1 - 6   and   day from 0 - 6

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        (str) both - name of the month and day of week to filter by, or "all" to apply no both filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df["Start Time"])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df["month"] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert monthnumber and daynumber to monthname and dayname
    monthlydict = {1 : "January", 2 : "February", 3 : "March", 4 : "April", 5 : "May", 6 : "June"}
    dailydict = {0 : "Monday", 1 : "Tuesday", 2 : "Wednesday", 3 : "Thursday", 4 : "Friday", 5 : "Saturday", 6 : "Sunday"}

    # display the most common month
    print(monthlydict[df["month"].mode()[0]], " is the most common month")

    # display the most common day of week
    print(dailydict[df["day_of_week"].mode()[0]], " is the most common day of the week")

    # display the most common start hour
    print(df['Start Time'].dt.hour.mode()[0], "-", df['Start Time'].dt.hour.mode()[0] + 1, "o'clock  is the most common hour of day")

#    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(df["Start Station"].mode()[0], " is the most common start station")

    # display most commonly used end station
    print(df["End Station"].mode()[0], " is the most common end station")

    # display most frequent combination of start station and end station trip
    print((df["Start Station"] + " --> " + df["End Station"]).mode()[0], " is the most common trip (from start station to end station)")

#    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("{:.2f}".format(df["Trip Duration"].sum()/60/60/24), "DAYS of total traval time")

    # display mean travel time
    print("{:.2f}".format(df["Trip Duration"].mean()/60), "MINUTES of average traval time")

#    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of each user type:")
    print(df["User Type"].value_counts())

    # Display counts of gender, but only if the filtered city is new york city or chicago
    if city == "new york city" or city == "chicago":
        print("\nCounts of each gender:")
        print(df["Gender"].value_counts(), "\n")
    # Display earliest, most recent, and most common year of birth
        print(int(df["Birth Year"].min()), "is the earliest year of birth")
        print(int(df["Birth Year"].max()), "is the most recent year of birth")
        print(int(df["Birth Year"].mode()), "is the most common year of birth")

#    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def display_raw_data(df):
    # Asking the user if he wants to see 5 rows of raw data at a time
    row = 0
    while True:
        raw = input("Do you want to see 5 rows of raw data at a time? Y or N\n").lower().strip()
        if row + 5 < df.shape[0] and (raw == "y" or raw == "yes"):
            print(df.iloc[row : row + 5])
            row += 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(df)

        # asking for a restart to filter again
        restart = input('\nWould you like to restart? Y or N\n').lower().strip()
        if restart.lower() not in ["yes","yep","yeah","y","yessir"]:
            break


if __name__ == "__main__":
	main()