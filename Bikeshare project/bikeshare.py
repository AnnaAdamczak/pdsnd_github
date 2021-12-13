import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    User is supposed to pick city, month and day

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please enter the name of the city, that you want to explore. You can peak from:\n Chicago, New York City, Washington.\n>>>')
    city = city.casefold()

    # checking if the city typed by user is in the dictionary
    while city not in CITY_DATA:
        city = input("We don't have that city in our base. Please try again or check for misspelling.\n>>>")
        city = city.casefold()


    # TO DO: get user input for month (all, january, february, ... , june)

    # definifn list of months
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input('Please enter the month from Januray to June or "all" to filter months:\n>>>')

    #changing whatever user added to casefold and checking if the input is in the list
    month = month.casefold()
    while month not in months:
        month = input('Month incorrect please try again or check for misspelling.\n>>>')
        month = month.casefold()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # defining list of days
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = input('Please enter the day of week from Monday to Satruday or "all" to filter days:\n>>>')

    #changing whatever user added to casefold and checking if the input is in the list
    day = day.casefold()
    while day not in days:
        day = input('Week day incorrect please try again or check for misspelling.\n>>>')
        month = month.casefold()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
# preparing and loading the dataframe to calculate
    df = pd.read_csv(CITY_DATA[city])
    print('The data is loaded!')


 # Extracting month and day of week from Start Time to create new columns
 # But first converting string column to date time datatype
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # month filter
    if month != 'all':
        # to get an intiger from the month list using index
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filtering the data by month name
        df = df[df['month'] == month]

    # day filter
    if day != 'all':
        # to get an intiger from the day of week list using index
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    # new month column
    df['month'] = df['Start Time'].dt.month
    # calculation of the popularity of the month using .mode()
    popular_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('The most popular month was:', months[popular_month-1])


    # TO DO: display the most common day of week

    # new day of week column
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    # calculation of the popularity of the day using .mode()
    popular_day = df['day_of_week'].mode()[0]
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print('The most popular day of rental was:', days[popular_day])


    # TO DO: display the most common start hour
    # new hour column
    df['hour'] = df['Start Time'].dt.hour

    popular_hour = df['hour'].mode()[0]
    print('The nost popular hour of starting a trip was:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.

    Returns:
    1) Most popular start station
    2) Most popular end of trip station
    3) The most popular trip from start to end station

    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most popular start station is: '+ str(start_station))


    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most popular end station is: '+ str(end_station))


    # TO DO: display most frequent combination of start station and end station trip
    print('\n Most Frequent Combination of Start and End Station Trips: \n\n',df.groupby(['Start Station', 'End Station']).size().nlargest(1))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total trip duration:', df['Trip Duration'].sum())


    # TO DO: display mean travel time
    print('Mean of trip duration:', round(df['Trip Duration'].mean(),2))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.

    Returns:
    user type - as a type of user from database
    gender - gender of user declared by customers
    birth years - as max, min and mos t common year of birth

    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types,'\n')


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(gender,'\n')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest year of birth is:', df['Birth Year'].min())
        print('Most recent year of birth is:', df['Birth Year'].max())
        print('Most common year of birth is:', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        #While loop for displaying raw data
        enter = ['yes','no']
        user_input = input('Would you like to see raw data? Type Yes or No.\n>>>')

        while user_input.lower() not in enter:
            user_input = input('Only yes or no arguments are applicable. Please Enter Yes or No:\n>>>')
            user_input = user_input.lower()

        # n as a number of rows at the beggining
        n = 0
        while True:
            if user_input.lower() == 'yes':

                print(df.iloc[n : n + 5])
                n += 5
                user_input = input('\nWould you like to see more rows? Type Yes or No.\n>>>')
                while user_input.lower() not in enter:
                    user_input = input('Only yes or no arguments are applicable. Please type Yes or No:\n>>>')
                    user_input = user_input.lower()
            else:
                break


        restart = input('\nWould you like to restart? (Enter:Yes/No).\n>>>')
        while restart.lower() not in enter:
            restart = input('Only yes or no arguments are applicable. Please Enter Yes or No:\n>>>')
            restart = restart.lower()
        if restart.lower() != 'yes':
            print('Thank you and see you later!')
            break


if __name__ == "__main__":
	main()
