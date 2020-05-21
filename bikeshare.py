import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data from chicago, new york city or washington?\n').lower()
    while city not in ('chicago', 'new york city', 'washington'):
        print('Please key in a correct city name')
        city = input('Would you like to see data from chicago, new york city or washington?\n').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month would you like to see data from?\nPlease choose from january, february, march, april, may, june or all.\n').lower()
    while month not in('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print('Please key in a valid month name')
        month = input('Which month would you like to see data from?\nPlease choose from january, february, march, april, may, june or all.\n').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    day = input('Select the day of the week you want to filter the bikeshare data by. \nPlease choose from sunday, monday, tuesday, wednesday, thursday, friday, saturday or all:\n').lower()
    while day not in days:
        print('\nPlease enter a valid day of the week')
        day = input('Which day of the week would you like to check?\nPlease choose from sunday, monday, tuesday, wednesday, thursday, friday, saturday or all)\n').lower()

    print('\nWe are working with {} data\n'.format(day.upper()))
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    while True:
        raw_data = input('Would you like to see 5 lines of raw data?\nPlease enter yes or no.\n').lower()
        if raw_data == 'yes':
            print(df.head())
            break
        elif raw_data == 'no':
            break
        else:
            print('your entry is invalid')
            continue


    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    #print(df.head())

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        #print(df.head())

    # filter by day of week if applicable
    if day != 'all':
        #use the index of the weekdays list to get the corresp int
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        day = days.index(day)

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
        #print(df.head())

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('the most common month is: ', popular_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('the most common day is: ', popular_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('the most common start hour is: ', popular_hour)
    #TO DO: display the least common start hour
    hour_counts = df['hour'].value_counts()
    least_common_hour = hour_counts.index[-1]
    print('the least common start hour is: ', least_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('the most popular start station is: ', popular_start_station)
    #display least commonly used start station
    start_station_counts = df['Start Station'].value_counts()
    least_used_start_station = start_station_counts.index[-1]
    print('the least commonly used start station is: ', least_used_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('the most popular end station is: ', popular_end_station)
    #display least commonly used end station
    end_station_counts = df['End Station'].value_counts()
    least_used_end_station = end_station_counts.index[-1]
    print('the least commonly used end station is: ', least_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    #create a column for the combination of start station and end station
    df['combination'] = df['Start Station'].str.cat(df['End Station'], sep='-')
    most_frequent_combination = df['combination'].mode()[0]
    print('the most frequent combination of start station and end station trip is: ', most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('the total travel time is: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('the mean travel time is: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].nunique()
    print('the counts of user types are: ', user_type)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        count_of_gender = df['Gender'].nunique()
        print('the count of gender is: ', count_of_gender)
        count_user_by_gender = df['Gender'].value_counts()
        print('the count of users by gender is: \n', count_user_by_gender.to_string())
    else:
        print('gender column does not exists')


    # TO DO: Display earliest, most recent, and most common year of birth
    #convert column Birth Year to datetime format
    if 'Birth Year' in df.columns:
        df['Birth Year'] = pd.to_datetime(df['Birth Year'])
    #to get the earliest year of Birth
        least_recent_year = df['Birth Year'].min()
        print('the earliest year of birth is: ', least_recent_year)
    #to get the most recent year of birth
        most_recent_year = df['Birth Year'].max()
        print('the most recent year of birth is: ', most_recent_year)
    #to get the most common year of birth
        most_common_year = df['Birth Year'].mode()[0]
        print('the most common year of birth is: ', most_common_year)

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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
