import numpy as np
from tqdm import tqdm
import json
import re
# with open("winner.weights" ,"r") as f:
# 	winner_weigths = f.read().split('\n')
# 	print(len(winner_weigths))
# 	print(winner_weigths)
# 	#winner_weigths = [eval(i) for i in tqdm(winner_weigths[:-1])]
# 	print("Import Complete")

filename = "winner.weights"
winner_combined_weights = []
with open(filename,"r") as f:
    input_lines = f.readlines() #Contains all the winner weights
    input_lines = list(map(lambda s: s.strip(), input_lines)) #Remove \n present in the list
    input_lines = ' '.join(input_lines)
    input_lines = re.split("\$\$",input_lines)
    winner_combined_weights = input_lines[0]
    # print(input_lines)

winner_combined_weights_list = re.split("\!\!",winner_combined_weights) #Each win's weights seperated as list.

# print(winner_combined_weights_list)
numpyarray = np.array(winner_combined_weights)
print(numpyarray.size)
# data = [x for x in data if x] #Removes empty lists

# data2 = data[0]

# data2 = re.findall(".*?[\]]",data2) #Splitting into a list

# print(data2)