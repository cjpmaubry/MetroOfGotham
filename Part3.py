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




#QUESTION 2
#Because the ID in the Database are in order we can use a dichotomic search algorithm

#Dichotomic Search which return the index of the line where are the ID researched
def  DichotomicSearchID( ID, SortedDatabase ):
    a = 0
    b = len(SortedDatabase)-1
    m = (a+b)//2
    while a < b :
        if (int(SortedDatabase[m][0]) == ID ):
            return m
        elif (int(SortedDatabase[m][0]) > ID ):
            b = m-1
        else :
            a = m+1
        m = (a+b)//2 
    if(int(SortedDatabase[m][0]) == ID ): # Final test for the last value
        return a
    else: # If last test is egal to ID return -1 
        return -1

#This method launch Dichotomic Search and interpret the result by displaying message to the user
def FindIDWithDichotomic(SortedDatabase,ID):
    index=DichotomicSearchID( ID, SortedDatabase )
    if(index==-1): # If we don't find the ID
        print("The ID: ",ID," isn't in the Dataset")
    else: # If we find the ID
        print("The ID: ",ID," is in the Dataset and it corresponds to :",SortedDatabase[index][1], " and he was certified by ",SortedDatabase[int(SortedDatabase[index][2])-1][1])



#QUESTION 3








def main():
    dataset=GiveDataSet()
    #FindID(dataset,100)
    FindIDWithDichotomic(dataset,100)

if __name__ == "__main__":
    main()


