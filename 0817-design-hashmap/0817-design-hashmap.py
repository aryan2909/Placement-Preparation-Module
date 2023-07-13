class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [None] * self.size

    def _hash_function(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash_function(key)
        if self.buckets[index] is None:
            self.buckets[index] = ListNode(key, value)
        else:
            current = self.buckets[index]
            while True:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = self._hash_function(key)
        current = self.buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        index = self._hash_function(key)
        current = prev = self.buckets[index]
        if not current:
            return
        if current.key == key:
            self.buckets[index] = current.next
        else:
            current = current.next
            while current:
                if current.key == key:
                    prev.next = current.next
                    return
                current, prev = current.next, prev.next
