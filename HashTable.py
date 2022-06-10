class HashTable:

    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # gets bucket list where this item will go
    def find_bucket(self, item):
        bucket = hash(item) % len(self.table)
        bucket_list = self.table[bucket]
        return bucket_list

    # inserts a new item into bucket list
    def insert(self, key, item):
        key_value = [key, item]
        self.find_bucket(key).append(key_value)
        return True

    # updates existing key in bucket list
    def update(self, key, item):
        for kv in self.find_bucket(key):
            if kv[0] == key:
                kv[1] = item
                return True

    # removes item from bucket list
    def remove(self, key):
        for kv in self.find_bucket(key):
            if kv[0] == key:
                self.find_bucket(key).remove([kv[0], kv[1]])

    # searches for item in bucket list
    def search(self, key):
        if self.find_bucket(key) is not None:
            for kv in self.find_bucket(key):
                if kv[0] == key:
                    return kv[1]  # value
        return None
