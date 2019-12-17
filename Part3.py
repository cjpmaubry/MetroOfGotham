import csv
from pathlib import Path

def GiveDataSet():
    #finding the folder and file
    data_folder = Path("MetroOfGotham/")
    file_to_open = data_folder / "DatasetPart3.csv"
    with open(file_to_open, "r") as csvfile:
        lines = csv.reader(csvfile)
        dataset=list(lines)
    return dataset

    # QUESTION 1
    #We use an algorithm that scans the entire dataset to find the ID (it stops as soon as it finds it)

def FindID(dataset,ID):
    index=0
    while(index<len(dataset)): #We scans all the dataset
        if(int(dataset[index][0])==ID ):# If we find the ID :
            value=index
            index+=len(dataset)+1 # We modifie the index to go out the loop
        index+=1 # Next line

    if(index==len(dataset)): # If we don't find the ID
        print("The ID: ",ID," isn't in the Dataset")
    else: # If we find the ID
        print("The ID: ",ID," is in the Dataset and it corresponds to :",dataset[value][1], " and he was certified by ",dataset[int(dataset[value][2])-1][1])






def main():
    dataset=GiveDataSet()
    FindID(dataset,100)


if __name__ == "__main__":
    main()