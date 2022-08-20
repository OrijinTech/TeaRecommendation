import TeaData
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

    def getRelated(self, userInput):
        # [('Dian Hong Gong Fu', ['Red Tea', 'China', 'Dian Hong Gong Fu', 0, 160])][('Jasmine Flower', ['Herbal', 'China', 'Jasmine Flower', 0, 140])]
        tea_hash = HashTable(100)
        for tea in TeaData.tea_data:
            val = self.get_val(tea[2])
            for data in val:
                data = str(data)
                if(userInput in data):
                    tea_hash.set_val(data[2], val)
                    break
        return tea_hash

# def printTea():
#     print()
#     print()


    