import pandas

# my_data = pandas.read_csv("marks.txt")

# write in terminal : explorer .     To Know the directory

# print(my_data)

# converting to CSV
# my_data.to_csv("marks.csv")

# To Convert and Dont Want Indexing
# my_data.to_csv("marks.csv", index=None)

# To add Header after converting
# my_data.columns = ["Name", "Marks"]

# Give a new sign exchanging "," sign
# my_data = pandas.read_csv("marks.txt", delimiter="=")



my_data = pandas.read_csv("marks.txt", sep="\t")

my_data.to_csv("marks.csv", index=None)

