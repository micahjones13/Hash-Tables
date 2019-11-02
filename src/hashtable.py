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
        # index is the hash of the key
        index = self._hash_mod(key)
        # the current pair is storage at the index
        current_pair = self.storage[index]
        # if current pair exists,
        if current_pair:
            # if the key passed into insert equals the pair key at the index, change the value to passed in value
            if key == current_pair.key:
                current_pair.value = value
            # if it doens't match, then we have some links
            else:
                # check to see if current pair has a next link
                if current_pair.next:
                    # walk through the links
                    while current_pair.next:
                        current_pair = current_pair.next
                    # once you hit the end, insert the new pair into the LL
                    else:
                        current_pair.next = LinkedPair(key, value)
                # if there is no next in LL, then make one and add the current pair value
                else:
                    current_pair.next = LinkedPair(key, value)
        # if it didn't already exist, then add it
        else:
            self.storage[index] = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # index is hashed key
        index = self._hash_mod(key)

        # If none: return none
        if self.storage[index] is None:
            print("Key not found")
            return None
        # Find the key:value pair in storage
        else:
            pair = self.storage[index]
            # If we get it from the top of the linked list:
            if pair.key == key:
                # replace pair with the next node
                self.storage[index] = pair.next
            elif pair.key != key and pair.next is not None:
                # Iterate through nodes in linked list
                while pair is not None:
                    # Record previous pair
                    prev_pair = pair
                    # Acquire next pair
                    pair = pair.next
                    # check to see if we have the right key
                    if pair is not None and pair.key == key:
                        # Remove middle pair
                        prev_pair.next = pair.next
                    else:
                        pass
            else:
                print("Key not found")

        # hash_key = self._hash_mod(key)
        # # print(hash_key, 'hash_key')
        # # print(key, 'key')
        # if self.storage[hash_key] != None:
        #     # print(self.storage[hash_key], 'self.stoarge[hash_key]')
        #     self.storage[hash_key] = None
        # else:
        #     print('Key not found')

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # index is hashed key
        index = self._hash_mod(key)
        # current _pair is storage at the index
        current_pair = self.storage[index]
        # if it exists, then go in and retireve the value
        if current_pair:
            # if the key matches the current_pair key, return the value, you're done
            if key == current_pair.key:
                return current_pair.value
            # if it doesn't, then we have some links. Walk through them
            elif current_pair.next:
                # set value to none so we can return that if we can't find key, return something else if we do
                value = None
                # walk through the LL
                while current_pair.next:
                    # if key's match, then store the value
                    if key == current_pair.next.key:
                        value = current_pair.next.value
                    # keep the while loop going through the LL
                    current_pair = current_pair.next
                else:
                    return value
        else:
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # Double self.capacity
        self.capacity = self.capacity * 2
        # rehash
        # creates new storage of twice the size
        new_storage = [None] * self.capacity
        old_storage = self.storage
        self.storage = new_storage
        for i in range(len(old_storage)):
            if old_storage[i] != None:
                if old_storage[i].next:
                    current = old_storage[i]
                    while current.next:
                        self.insert(current.key, current.value)
                        current = current.next
                    else:
                        self.insert(current.key, current.value)
                else:
                    self.insert(old_storage[i].key, old_storage[i].value)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    print("")
# ht1 = HashTable(2)

# print(ht1.storage, 'BEFORE INSERT')
# print(ht1._hash_mod('a'))
# print(ht1._hash_mod('z'))

# ht1.insert('a', 0)
# ht1.insert('b', 2)

# ht1.remove('a')
# ht1.retrieve('a')

# print(ht1.storage)
# ht = HashTable(8)

# ht.insert("key-0", "val-0")
# ht.insert("key-1", "val-1")
# ht.insert("key-2", "val-2")
# ht.insert("key-3", "val-3")
# ht.insert("key-4", "val-4")
# ht.insert("key-5", "val-5")
# ht.insert("key-6", "val-6")
# ht.insert("key-7", "val-7")
# ht.insert("key-8", "val-8")
# # ht.insert("key-9", "val-9")

# print(ht.retrieve('key-0'))
# print(ht.storage)
# ht.remove('key-0')

# print(ht.storage)
