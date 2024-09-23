class HashTable:
    def __init__(self, initial_capacity=20):
        # Initialize the hash table with empty buckets
        self.buckets = [[] for _ in range(initial_capacity)]

    def insert(self, key, item):  # Define insert method
        bucket_index = hash(key) % len(self.buckets)
        bucket = self.buckets[bucket_index]

        # Check if key already exists and update it
        for i, kv in enumerate(bucket):
            if kv[0] == key:
                bucket[i] = (key, item)  # Use tuple to prevent mutability error
                return True

        # Key doesn't exist, append a new key-value pair
        bucket.append((key, item))
        return True

    def lookup(self, key):  # Define a method that allows for searching the hash table
        bucket_index = hash(key) % len(self.buckets)
        bucket = self.buckets[bucket_index]

        # Iterate over the bucket to find the key
        for k, v in bucket:
            if key == k:
                return v
        return None  # Return None if the key is not found

    def hash_remove(self, key):  # Define a method for removing key-value pairs from the hash table
        bucket_index = hash(key) % len(self.buckets)
        bucket = self.buckets[bucket_index]

        # Iterate and remove the key-value pair if found
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False  # Return False if the key is not found

    def to_list(self):
        keyv = []

        for bucket in self.buckets:
            for k, v in bucket:
                keyv.append([k] + v)
        return keyv