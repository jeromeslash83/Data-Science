import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv(r'C:\Users\jy\Documents\coding\Coding\adult.data.csv')
    

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    males_age = df[['sex']][df['sex']=='Male']
    males_age['age'] = df[['age']][df['sex']=='Male']
    average_age_men = round(males_age['age'].mean(), 1)
    

    # What is the percentage of people who have a Bachelor's degree?
    educ= df['education']
    BS = df['education'][df['education']=='Bachelors']
    percentage_bachelors = round((BS.count()/educ.count()) * 100, 1)


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    advanced_education = df[['education', 'salary']][df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    rich_advanced_education = advanced_education['salary'][advanced_education['salary']== '>50K']


    # What percentage of people without advanced education make more than 50K?
    lower_education = df[['education', 'salary']][~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    rich_lower_education = lower_education['salary'][lower_education['salary']== '>50K']


    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = (advanced_education['education'].count())
    lower_education = (lower_education['education'].count())


    # percentage with salary >50K
    higher_education_rich = round((int(rich_advanced_education.count()) / higher_education)*100, 1)
    lower_education_rich = round((int(rich_lower_education.count()) / lower_education)*100, 1)


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_work_hours = df['hours-per-week'].min()
    salary_min_hrs = df[['salary']][df['hours-per-week']== min_work_hours]
    num_min_hr_workers = df['salary'][df['hours-per-week']== min_work_hours].count()
    rich_lazy_count = salary_min_hrs['salary'][salary_min_hrs['salary']== '>50K'].count()

    rich_percentage = (rich_lazy_count/num_min_hr_workers) * 100

    # What country has the highest percentage of people that earn >50K?
    Number_of_50k = ((df['native-country'][(df['salary'] == '>50K')].value_counts()))
    total_country = df['native-country'].value_counts()
    percentages = Number_of_50k/total_country 
    highest_earning_country = percentages.idxmax()


    highest_earning_country_percentage = round(percentages[highest_earning_country] * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    #This gets the jobs in India with the >50k salary then gets the id of the max value_count.
    top_IN_occupation = (df['occupation'][(df['native-country']== 'India') & (df['salary'] == '>50K')].value_counts()).idxmax()

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
