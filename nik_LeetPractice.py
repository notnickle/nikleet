#Leetcode Practice
import src.Library.datastructures as struct
import src.Library.linked_list_prob as llprob


def modeSelect():
    print("Mode Select in Process...")
    print("0. Linked List LeetCode Problems")
    x = input("Please select a desired datastructure type:")

    return(x)



#/////////////////////////////////
#Main Driver
#/////////////////////////////////
def main():
    ex = 'Y'
    while ex.lower()=='y':
        x = modeSelect()
        if x=='0': llprob.linkedListProbSelect()
        ex = input("\n\nDo you wish to continue with the program? (Y/N)")
            
    input("Finished! \nPress enter to close...")

#Main method call
if __name__ == "__main__":
    main()