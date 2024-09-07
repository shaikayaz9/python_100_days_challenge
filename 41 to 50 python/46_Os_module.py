#operetor system

import os
#make a folder
os.mkdir("data")


# if(not os.path.exists("data")):
#     os.mkdir("data")

# 50 folder at oncs

# for i in range(0,100):
    # os.mkdir(f"data/day{i+1}") #give error bececuse we have data file already we will check not condition (stop os.mkdir on top)
    # os.rename(f"data/python_day{i+1}", f"data/python day{i+1}")

#WAP to find a file

folder = os.listdir("data")

for i in folder:
  print(i)  #folders
  print(os.listdir(f"data/{i}")) #folder/file



print(os.getcwd()) #current working directory