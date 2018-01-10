from dateutil import parser
import pandas as pd
import matplotlib.pyplot as plt


class CsvController:

    def __init__(self, csvFile, weekNumFrom, weekNumTo, yearNum):
        self.csvFile = csvFile
        self.weekNumFrom = weekNumFrom
        self.weekNumTo = weekNumTo
        self.yearNum = yearNum

    def excuteCsv(self):
        # reading csv file
        data = pd.read_csv(self.csvFile)
        # create dataframe from specified columns
        df = pd.DataFrame(data, columns = ['fake_user_id', 'country', 'language', 'created_time'])

        # create empty lists for parsing datetime object to date only, extract week number, month and year
        dateOnlyList, weekNumList, monthList, yearList = [], [], [], []

        # iterate through data to update lists
        for row_index, row in df.iterrows():
            # parse 'created_time' column
            d = parser.parse(row['created_time'])
            d = d.date()

            # append to lists
            dateOnlyList.append(d)
            weekNumList.append(d.isocalendar()[1])
            monthList.append(d.month)
            yearList.append(d.year)

        # create new dataframe from the generated date only list
        new_df = pd.DataFrame({'created_time': dateOnlyList})
        # update 'created_time' column within main dataframe
        df.update(new_df)
        # add 'week_num', 'month' and 'year' columns to main dataframe
        df['week_num'] = weekNumList
        df['month'] = monthList
        df['year'] = yearList

        # sort dataframe by year and week_num
        df = df.sort_values(by=['year', 'month', 'week_num'], ascending=True)	
        
        # add filters to data
        dft = df[(df.year == int(self.yearNum)) & (df.week_num >= int(self.weekNumFrom)) & (df.week_num <= int(self.weekNumTo))]

        # grouping data by week_num
        df_group = dft.groupby(['week_num'])
        # get number of users
        newDF = df_group.size().reset_index(name='counts')
        newDF = newDF.set_index('week_num')

        # draw chat
        self.drawPlt(newDF)
        

    def drawPlt(self, df):

        fig = plt.plot(df, alpha=0.5, label='Users', color='k', linestyle="dashed", marker="o")

        plt.grid(True)
        plt.xlabel('Weeks')
        plt.ylabel('New Users')
        plt.title('Number of new users per week for ' + self.yearNum)
        plt.legend(loc='upper right', borderpad=1)   
        plt.savefig('stats/static/images/graph.png')
        plt.close()
