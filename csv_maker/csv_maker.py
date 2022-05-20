import pandas as pd
#name	answers	As	Bs	Cs	Ds	Es	proportion	url
initial_data = pd.read_csv("./csv_maker/initial_data.csv")


def process_string(letter):
    #Returns [As, Bs, Cs, Ds, Es]
    global initial_data
    initial_data.loc[:, letter] = initial_data.loc[:, "answers"].str.count(letter)



process_string("A")
process_string("B")
process_string("C")
process_string("D")
process_string("E")

initial_data.to_csv("./csv_maker/counted_data.csv")
print(True)