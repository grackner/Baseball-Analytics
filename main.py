import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
import data_cleaning
sns.set()

"""
Gabrielle Rackner and Owen Schaff
CSE 163
This program implements functions that analyze MLB player data to
look at relationships between salary, WAR, age, etc.
It also creates a Machine Learning model to predict
performance (WAR) from the salary and age of a player.
"""


def salary_over_time(salary):
    """
    Pt 1 Salary Vs. Time-
    This function returns a plot of MLB players salaries over time.
    It uses the salary dataset and filters the data
    to only look at the years from 2003 to 2015.
    """
    salary1 = salary[(salary['yearID'] >= 2003) & (salary['yearID'] <= 2015)]
    salary1 = salary1.groupby('yearID')['salary'].mean()
    sns.relplot(data=salary1, kind='line')
    plt.title('MLB Salaries Over Time')
    plt.xlabel('Year')
    plt.ylabel('Salary')
    plt.savefig('salary_vs_time.png')


def salary_war(merged2):
    """
    Pt 2a Relationship Between Salary & WAR -
    This function creates a plot of the relationship between salary and WAR.
    It uses the merged dataset created in the main method of this program.
    """
    sns.relplot(data=merged2, x='salary', y='WAR')
    plt.title('Salary Vs. WAR')
    plt.xlabel('Salary (Tens of millions)')
    plt.xticks([0, 5000000, 10000000, 20000000])
    plt.savefig('salary_vs_war.png')


def salary_by_team(merged2):
    """
    Pt 2b Relationship between Salary & Team
    This function creates a plot of the average salary by team in the MLB.
    It uses the merged dataset to group teams and find the mean salary.
    """
    season = merged2.groupby('teamID', as_index=False)['salary'].mean()
    season = pd.DataFrame(season)
    sns.catplot(data=season, x='teamID', y='salary', kind='bar', color='b')
    plt.xticks(rotation=-80)
    plt.title('Average Salary by MLB Team')
    plt.xlabel('Team')
    plt.ylabel('Average Salary per Player (Millions)')
    plt.savefig('salary_by_team.png')


def salary_by_age(merged2):
    """
    Pt 3 Relationship between Salary & Age-
    This function creates a scatter plot of the
    relationsihp between Salary and Age. It uses the merged
    dataset.
    """
    sns.relplot(data=merged2, x='Age', y='salary')
    plt.yticks([0, 5000000, 10000000, 15000000, 20000000])
    plt.title('Salary Vs. Age of an MLB Player')
    plt.savefig('salary_by_age.png')


def age_war(merged2):
    """
    Pt 4 Age Vs WAR-
    This function creates a scatter plot of the relationship
    between the age of an MLB player and their salary. Uses
    the merged dataset.
    """
    sns.relplot(data=merged2, x='Age', y='WAR')
    plt.title('Age of a Player Vs. WAR')
    plt.savefig('age_vs_war.png')


def predict_war(merged2):
    """
    Pt 5 Machine Learning Model -
    This function creates a Machine Learning model that
    predicts WAR (performance) of a player from their age
    and salary. We use a regression model since we are
    predicting a numeric variable.
    """
    subset = merged2[['WAR', 'Age', 'salary']]
    features = subset.loc[:, subset.columns != 'WAR']
    labels = subset['WAR']
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)

    model = DecisionTreeRegressor()
    model.fit(features_train, labels_train)
    test_predictions = model.predict(features_test)

    test_acc = mean_squared_error(labels_test, test_predictions)
    return test_acc


def main():
    merged2 = data_cleaning.merged()
    salary = data_cleaning.salary()
    salary_over_time(salary)
    salary_war(merged2)
    salary_by_team(merged2)
    salary_by_age(merged2)
    age_war(merged2)
    print(predict_war(merged2))


if __name__ == '__main__':
    main()
