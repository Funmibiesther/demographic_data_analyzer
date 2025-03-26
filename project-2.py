import pandas as pd
adult_data = pd.read_csv('adult.csv')

#Q1
race_count = adult_data['race'].value_counts()

#Q2
average_age_of_men = round(adult_data[adult_data['sex'] == 'Male']['age'].mean(),2)

#Q3
bachelors_per = round(adult_data['education'].value_counts(normalize =True)['Bachelors'],2)

#Q4
advanced_edu_per = round(adult_data[adult_data['education'].isin(['Doctorates','Bachelors','Masters'])]['income'].value_counts(normalize = True) ['>50K'],2)

#Q5
less_adv_edu_per = round(adult_data[adult_data['education'].isin(['HS-grad','Some-college','7th-8th','10th','Prof-school','11th','Assoc-acdm','Assoc-voc','1st-4th','5th-6th','12th','9th','Preschool'])]['income'].value_counts(normalize = True) ['>50K'],2)

#Q6
min_hour = adult_data['hours.per.week'].min()

#Q7
earning_>50K_per = adult_data[adult_data['hours.per.week']==adult_data['hours.per.week'].min()]['income'].value_counts(normalize= True)['>50K']

#Q8 country highest per
highest_per = round(adult_data[adult_data['native.country'] =='Yugoslavia']['income'].value_counts(normalize = True)['>50K'],2

#Q9 most popular occupation in india
popular_occup = adult_data[(adult_data['native.country'] == 'India') & (adult_data ['income'] =='>50K')]['occupation'].value_counts().keys()                  