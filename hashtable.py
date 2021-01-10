# code written by Timo Kats

class hashtable:
    def __init__(self, size):
        self.size = size
        self.hashtable = {}

    def linear_probing(self, key):
        new_key = key
        while self.check_key(new_key):
            new_key = (new_key + 1) % self.size
            if new_key == key:
                print("table is full")
                exit()
        return new_key

    def check_key(self, key):
        if key in self.hashtable.keys():
            return True
        else:
            return False

    def get_key(self, value):
        # (ord(value[0]) - 97) gets the aplhabet value of the first letter
        key = (ord(value[0]) - 97) % self.size
        return key

    def insert(self, value):
        key = self.get_key(value)
        if self.check_key(key):
            key = self.linear_probing(key)
        self.hashtable[key] = value

    def delete(self, value):
        key = self.get_key(value)
        del self.hashtable[key]

    def read_index(self, key):
        print(self.hashtable[key])

    def read_table(self):
        print(self.hashtable)

if __name__ == '__main__':
    table_1 = hashtable(10)
    table_1.insert("alice")
    table_1.insert("bob")
    table_1.insert("bill")
    table_1.read_table()
    table_1.delete("bob")
    table_1.read_index(2)
