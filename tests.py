from scipy.stats import chisquare
import pandas as pd
import math
from scipy import stats


counted_data = pd.read_csv("./csv_maker/counted_data.csv", index_col=[0])


def make_chisquare(name):
    "Get the test result, print it out, add it to the df"
    row = counted_data.loc[name]
    list_of_data = [row.loc["A"], row.loc["B"], row.loc["C"], row.loc["D"], row.loc["E"]]
    chisquared_result = chisquare(list_of_data)
    print("Name: {0}, Chi-Squared Statistic: {1}, p-value: {2}".format(name, chisquared_result[0], chisquared_result[0]))
    
    counted_data.loc[name, "chisquared_statistic"] = chisquared_result[0]
    counted_data.loc[name, "chi_p-value"] = chisquared_result[1]




    
#Do a test on the sums

counted_data.loc["TOTAL", "A":"E"] =     [counted_data.loc[:, "A"].sum(),
    counted_data.loc[:, "B"].sum(),
    counted_data.loc[:, "C"].sum(),
    counted_data.loc[:, "D"].sum(),
    counted_data.loc[:, "E"].sum() ]

make_chisquare("TOTAL")



#One sample z tests

def one_sample_z_test(row_name, letter):

    #First get the amount of letters, then do a 1 sample z test, then store it
    letter_count = counted_data.loc[row_name, letter]

    #Set the total # of letters
    if row_name == "TOTAL":
        total_letters = 360
    else:
        total_letters = 40

    #get statistics
    phat = letter_count/total_letters
    null_pi = 0.2
    z_score = (phat-null_pi)/math.sqrt((phat*(1-phat))/total_letters)
    p_value = stats.norm.sf(z_score)

    #Write the data
    counted_data.loc[row_name, "{0}_statistic".format(letter)] = z_score
    counted_data.loc[row_name, "{0}_p-value".format(letter)] = p_value

letters_list = ["A", "B", "C", "D", "E"]
#Loop through and do the test
for index, row in counted_data.iterrows():
    make_chisquare(index)

    #Do 1 sample tests
    for letter in letters_list:
        one_sample_z_test(index, letter)
    

    

counted_data.to_csv("./csv_maker/counted_data.csv", index=True)
