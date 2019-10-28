# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"{self.value}"


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        # returns index int
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        pair = LinkedPair(key, value)
        hash_key = self._hash_mod(key)

        # if exceeds storage, ressize
        if self.capacity >= len(self.storage):
            self.resize()
    # insert wherever the hash index is
        if self.storage[hash_key] is None:
            self.storage[hash_key] = pair
        #!Handle collisions tomorrow
        #! Need something for if the key already exits

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hash_key = self._hash_mod(key)
        # print(hash_key, 'hash_key')
        # print(key, 'key')
        if self.storage[hash_key] != None:
            # print(self.storage[hash_key], 'self.stoarge[hash_key]')
            self.storage[hash_key] = None
        else:
            print('Key not found')

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hash_key = self._hash_mod(key)

        if self.storage[hash_key] is not None:
            # print(self.storage[hash_key], 'retrieved')
            return self.storage[hash_key]
        else:
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass


# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))
#     print("")
# ht1 = HashTable(2)

# print(ht1.storage, 'BEFORE INSERT')
# print(ht1._hash_mod('a'))
# print(ht1._hash_mod('z'))

# ht1.insert('a', 0)
# ht1.insert('b', 2)

# ht1.remove('a')
# ht1.retrieve('a')

# print(ht1.storage)
ht = HashTable(8)

ht.insert("key-0", "val-0")
ht.insert("key-1", "val-1")
ht.insert("key-2", "val-2")
ht.insert("key-3", "val-3")
ht.insert("key-4", "val-4")
ht.insert("key-5", "val-5")
ht.insert("key-6", "val-6")
ht.insert("key-7", "val-7")
ht.insert("key-8", "val-8")
# ht.insert("key-9", "val-9")

print(ht.retrieve('key-0'))
print(ht.storage)
ht.remove('key-0')

print(ht.storage)
