import HashTable
import restaurantData

tea_data = restaurantData.tea_data

hash_table = HashTable.HashTable(len(tea_data))

# Put all data from a list to hashtable
def dataToHashTable():
    for tea in tea_data:
        hash_table.set_val(tea[restaurantData.name], tea)
    return hash_table






def main():
    # hash table with all the data
    hash_table = dataToHashTable()
    print(hash_table)
    print("May I help you?")
    user_inp = input("Search: ")


# The Start of the program
main()
