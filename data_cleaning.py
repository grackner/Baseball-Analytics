import pandas as pd

'''
Gabrielle Rackner and Owen Schaff
CSE 163
This program implements cleans the datasets and returns a salary dataset,
and a merged dataset of players salary and performance statistics.
'''


def merged():
    '''
    This function returns the dataset merged2,
    a merge of two datasets.
    '''
    salary = pd.read_csv('salary.csv')
    player = pd.read_csv('players.csv')
    master = pd.read_csv('Master.csv')
    master['Name'] = master['nameFirst'] + ' ' + master['nameLast']
    subset = master[['playerID', 'Name']]
    merged = salary.merge(subset, left_on='playerID', right_on='playerID')
    merged = merged[merged['yearID'] == 2015]
    merged2 = merged.merge(player, left_on='Name', right_on='Name')
    return merged2


def salary():
    '''
    This function returns the dataset, salary.
    '''
    salary = pd.read_csv('salary.csv')
    return salary


def main():
    merged()
    salary()


if __name__ == '__main__':
    main()
