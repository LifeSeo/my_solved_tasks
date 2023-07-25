class Entity:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Node:
    def __init__(self, node_value: Entity):
        self.next = None
        self.node_value = node_value

    def __str__(self):
        return f'{self.node_value.key}:{self.node_value.value}'


class Bucket:
    def __init__(self, index):
        self.head: Node = None
        self.index = index

    def add(self, entity: Entity):
        node = Node(entity)
        if self.head is None:
            self.head = node
            return None

        current_node: Node = self.head
        while True:
            if current_node.node_value.key == entity.key:
                buf = current_node
                current_node.node_value.value = entity.value
                return buf
            if current_node.next is not None:
                current_node = current_node.next
            else:
                current_node.next = node
                return None

    def get(self, key):
        node: Node = self.head
        while node is not None:
            if node.node_value.key == key:
                return node.node_value.value
            node = node.next
        return None

    def remove(self, key):
        if self.head is None:
            return None
        if self.head.node_value.key == key:
            buf = self.head.node_value.value
            self.head = self.head.next
            return buf
        node = self.head
        while node.next is not None:
            if node.next.node_value.key == key:
                buf = node.next.node_value.value
                node.next = node.next.next
                return buf
            node = node.next
        return None

    def __str__(self):
        strings = list[str]()
        node = self.head
        while node is not None:
            strings.append(str(node))
            node = node.next
        return '\n'.join(strings)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        count = 0
        for i in self:
            count += 1
        return count




class HashMap:
    __BUCKETS_COUNTS_DEFAULT = 16

    __LOAD_FACTOR = 0.5

    def __init__(self, init_count=__BUCKETS_COUNTS_DEFAULT):
        self._buckets_count = init_count
        self._buckets = list[Bucket]([None for _ in range(self._buckets_count)])
        self.size = 0

    def __calculate_bucket_index(self, key):
        return abs(hash(key)) % len(self._buckets)

    def recalculate(self):
        self.size = 0
        old = self._buckets
        self._buckets = list[Bucket]([None for _ in range(len(self._buckets) * 2)])
        for i in range(len(old)):
            bucket = old[i]
            if bucket is not None:
                node = bucket.head
                while node is not None:
                    self.put(node.node_value.key, node.node_value.value)
                    node = node.next

    def put(self, key, value):
        if len(self._buckets) * self.__LOAD_FACTOR <= self.size:
            self.recalculate()

        index = self.__calculate_bucket_index(key)
        bucket = self._buckets[index]
        if bucket is None:
            bucket = Bucket(index)
            self._buckets[index] = bucket
        entity = Entity(key, value)
        ret = bucket.add(entity)
        if ret is None:
            self.size += 1
        return ret

    def get(self, key):
        index = self.__calculate_bucket_index(key)
        bucket = self._buckets[index]
        if bucket is None:
            return None
        return bucket.get(key)

    def remove(self, key):
        index = self.__calculate_bucket_index(key)
        bucket = self._buckets[index]
        if bucket is None:
            return None
        ret = bucket.remove(key)
        if ret is not None:
            self.size -= 1
        return ret

    def __str__(self):
        strings = list[str]()
        for i in range(len(self._buckets)):
            if self._buckets[i] is not None and self._buckets[i].head is not None:
                strings.append(f'{i}:\n{self._buckets[i]}')
        return '\n'.join(strings)

    def print(self):
        print(self, end=f'\n{"-" * 20}\n')

    def __iter__(self):
        for bucket in self._buckets:
            if bucket is not None and bucket.head is not None:
                yield bucket

    def __len__(self):
        count = 0
        for bucket in self:
            count += len(bucket)
        return count
