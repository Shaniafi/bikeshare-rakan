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

    while True:
        city = input("pleaes enter a city name from the following [chicago, new york city, washington]:").lower()
        if city not in CITY_DATA.keys():
            print("pleaes choose one of these citys: chicago, new york city, washington")
            continue
        else:
            break


    while True:
        month = input("pleaes enter a specific month from january to june or all: ").lower()
        if month not in ["all", "january", "february", "march" , "april" , "may", "june"]:
            print("pleaes choose all or a specific month from january to june")
            continue
        else:
             break


    while True:
        day = input("pleaes enter a specific day or all: ").lower()
        if day not in ["all", "monday", "tuesday" , "wednesday" ,"thursday" , "friday" , "saturday" , "sunday"]:
            print("pleaes choose all or a specific day of the week")
            continue
        else:
            break
            

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day of week - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day"] = df["Start Time"].dt.weekday_name
    df["hour"] = df["Start Time"].dt.hour
    if month != "all":
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df["month"] == month]

    if day != "all":
        # filter by day of week to create the new dataframe
        df = df[df["day"] == day.title()]    
    
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    common_month = df["month"].mode()[0]
    print("Most common month is:", common_month)

    

    common_day = df["day"].mode()[0]
    print("Most common day is:", common_day)

    

    common_hour = df["hour"].mode()[0]
    print("Most common hour is:", common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    common_start_station = df["Start Station"].value_counts().max
    print("Most common start station:", common_start_station)


    common_end_station = df["End Station"].value_counts().max
    print("Most common end station:", common_end_station)

    common_station = df.groupby(["Start Station", "End Station"]).count()
    print("Most common station:", common_station)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    total_travel_time = df["Trip Duration"].sum()
    print("Total travel time 'in seconds' is:",total_travel_time)
    
    
    mean_travel_time = df["Trip Duration"].mean()
    print("Mean of travel time 'in seconds' is:",mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df["User Type"].value_counts()
    print("Count of user by type is:", user_types)

    try:
        gender_count = df["Gender"].value_counts()
        print("Counts of user by gender is:", gender_count)
    except:  
        print("No available data for the selected city")

    try:
        earliset = df["Birth Year"].min()
        print("The earliset year of birth is:", earliset)
    except:  
        print("No available data for the selected city")
        
      
    try:
        recent = df["Birth Year"].max()
        print("The recent year of birth is:", recent)
    except:  
        print("No available data for the selected city")
        
        
    try:
        most_common_year = df["Birth Year"].value_counts().idxmax()
        print("The most common year of birth is:", most_common_year)
    except:  
        print("No available data for the selected city")        

        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    index=0
    user_input=input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower() 
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()  
   