import HashTable
import TeaData

tea_data = TeaData.tea_data

hash_table = HashTable.HashTable(len(tea_data))

# Put all data from a list to hashtable
def dataToHashTable():
    for tea in tea_data:
        hash_table.set_val(tea[TeaData.name], tea)
    return hash_table

def main():
    # hash table with all the data
    hash_table = dataToHashTable()
    # print(hash_table.get_val("Zao"))
    print("May I help you?")
    user_inp = input("Search: ")
    hash_table.getRelated(user_inp)


# The Start of the program
main()
