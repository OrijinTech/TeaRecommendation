import TeaData
import time
# Why using hash table? --> Hash Table provides faster speed of retrieval over other data structures.
# This is because Hash Table is index based data structure, we access elements by its index. 
class HashTable:

    def __init__(self, size) -> None:
        self.size = size
        self.hash_table = self.create_buckets()
    
    def create_buckets(self):
        return [[] for _ in range(self.size)]


    # insert values into the hash map
    def set_val(self, key, val):
        # get the index from the key
        hashed_key = hash(key) % self.size
        # get the bucket corrensponding to index
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))


    def get_val(self, key):
        hashed_key = hash(key) % self.size
        
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                break
    
        if found_key:
            return record_val
        else:
            return "No record found."
    
    def delete_val(self, key):
        hashed_key = hash(key) % self.size
        
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return
    
    def __str__(self) -> str:
        return "".join(str(item) for item in self.hash_table)

    # Return a hash table with all the related outputs
    def getRelated(self, user_input):
        # Corner case:
        if (user_input == ""):
            print("Please start entering...")
            return
        # We need to create a new hash table, because we canno't use the one with the complete data.
        tea_table = HashTable(len(TeaData.tea_data))
        # this holds the value for the emptiness of the hash table
        empty_table = True
        # Time the following process
        # start_time = time.time()
        for tea in TeaData.tea_data:
            tea_info = self.get_val(tea[TeaData.name])
            # tea_info is a single tea ['White Tea', 'China', 'Bai Lan Ye Sheng', 0, 220]
            for data_piece in tea_info:
                data_piece = str(data_piece)
                # convert everything in lower case --> making case insensitive
                if(user_input.lower() in data_piece.lower()):
                    empty_table = False
                    tea_table.set_val(data_piece[TeaData.name], tea_info)
                    printTea(tea_info)
                    break
        # print("Time used to retreive data:", time.time() - start_time)
        if(empty_table):
            print("We couldn't find any related products. QAQ")
        return tea_table

# Outputing the data for the user.
def printTea(val):
    print("---------------------------------")
    print('||', val[TeaData.name], '||')
    print("Origin:", val[TeaData.country])
    print("Ratings:", val[TeaData.rating])
    print("Tea Type:", val[TeaData.type])
    print("Price:", val[TeaData.price])
    print("---------------------------------")
    print('\n')

