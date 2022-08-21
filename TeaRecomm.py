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
    print("=========================================================", '\n', 'WELCOME TO ORIJIN TEA', '\n', '\n')
    # hash table with all the data
    hash_table = dataToHashTable()
    # print(hash_table.get_val("Zao"))
    user_inp = ' '
    while(True):
        user_inp = input("Search here: ")
        if(user_inp != 'quit'):
            print("=================================", '\n', '\n')
            hash_table.getRelated(user_inp)
        else:
            break


# def test():
#     hash_t = HashTable.HashTable(2)
#     hash_t.set_val("hi", "value")
#     print(hash_t)

# The Start of the program
main()
