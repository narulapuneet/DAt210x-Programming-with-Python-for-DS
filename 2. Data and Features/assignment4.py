import pandas as pd

nhl = pd.read_html("http://espn.go.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2")[0]

# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
nhl = pd.read_html("http://espn.go.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2")[0]

# TODO: Rename the columns so that they match the
# column definitions provided to you on the website
#
# .. your code here ..
nhl.columns = ['RK', 'Player', 'Team', 'GP', 'G','A','PTS', '+/-', 'PIM', 'PTS/G', 'SOG', 'PCT', 'GWG', 'PP_G','PP_A', 'SH_G','SH_A']

# TODO: Get rid of any row that has at least 4 NANs in it
#
# .. your code here ..
nhl=nhl.dropna(axis=0, thresh=4)

# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..
nhl = nhl.drop([1,13,25,37])

# TODO: Get rid of the 'RK' column
#
# .. your code here ..
nhl = nhl.drop(labels=['RK'], axis=1)

# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..
nhl.reset_index(drop=True)


# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
nhl.dtypes


# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
print (nhl.shape[0])
print (nhl.PCT.nunique())
print (int(nhl.GP.iloc[15]) + int(nhl.GP.iloc[16]))
