import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    data = pd.read_csv('sample_data/adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = data['race'].value_counts()

    # What is the average age of men?
    mask = data['sex'] == 'Male'
    average_age_men = data[mask].age.mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    num_bachelors = len(data[data['education'] =='Bachelors'])
    num_total = len(data)
    percentage_bachelors = round(num_bachelors / num_total * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    higher_ed = data[data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_ed = data[~data['education'].isin(['Bachelors','Masters','Doctorate'])]

    higher_ed_np = len(higher_ed[higher_ed.salary == '>50K'])
    lower_ed_np = len(lower_ed[lower_ed.salary == '>50K'])

    higher_education_rich = round(higher_ed_np / len(higher_ed) * 100, 1)
    lower_education_rich = round(lower_ed_np / len(lower_ed) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = data['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = data[data['hours-per-week'] == min_hours]

    rich_percentage = round(len(min_hours_p[min_hours_p.salary == '>50K']) / len(min_hours_p) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    country_counts = data['native-country'].value_counts()
    country_rich_counts = data[data['salary'] == '>50K']['native-country'].value_counts()

    highest_earning_country = (country_rich_counts / country_counts * 100).idxmax()
    highest_earning_country_percentage = round((country_rich_counts / country_counts * 100).max(), 1)
  
    # Identify the most popular occupation for those who earn >50K in India.
    filter = data.loc[(data['native-country'] == 'India') & (data['salary'] == '>50K')]
    top_IN_occupation = filter.occupation.value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
