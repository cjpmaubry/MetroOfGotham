import csv
import sys, os

def GiveDataSet():
    #finding the folder and file
    file_to_open = os.path.join(sys.path[0], "DatasetPart3.csv")

    with open(file_to_open, "r") as csvfile:
        lines = csv.reader(csvfile)
        dataset=list(lines)
    return dataset

def GiveDataSet2():
    #finding the folder and file
    file_to_open = os.path.join(sys.path[0], "DatasetPart3NotSort.csv")
    
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
#We decide to use the sort algorithm merge sort, which complexity is nlogn (where n is the number of line in the dataset)

# Implementation of the sort method Merge Sort for the Dataset define in the Project
def mergeSort(dataset):
    if len(dataset) > 1:
        middle = len(dataset) // 2 #Finding the middle of the array
        left = dataset[:middle] # Dividing the array : fisrt halves
        right = dataset[middle:] # Dividing the array : second halves

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)


        #Define usefull index :
        
        i = 0 # iterator for traversing the first halves
        j = 0 # iterator for traversing the second halves
        k = 0 # Iterator for the main list
        
        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if int(left[i][0]) < int(right[j][0]):
              # The value from the left half has been used
              dataset[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                dataset[k] = right[j]
                j += 1
            k += 1

        # For all the remaining values
        while i < len(left):
            dataset[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            dataset[k]=right[j]
            j += 1
            k += 1
            



#QUESTION 4
#The three are launched in the main
# A Special database (same as DatasetPart3 but where this ID are not already sorted) is used for this question


def main():
    dataset=GiveDataSet2() #Database not sorted
    print("Using method of question 1")
    FindID(dataset,10)
    print("\nUsing method of question 2 and 3 (sort with 3 and find ID with 2)")
    mergeSort(dataset)
    FindIDWithDichotomic(dataset,12)

if __name__ == "__main__":
    main()


