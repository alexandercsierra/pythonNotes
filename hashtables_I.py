table_size = 8
hash_table = [None] * table_size

def myHash(key):
    str_bytes = key.encode()
    total = 0

    for letter in str_bytes:
        total+=letter

    return total % table_size

def insert(key, value):
    index = myHash(key)

    hash_table[index] = value


def get(key):
    return hash_table[myHash(key)]


insert('blue', 'favorite')
insert('green', 'okay')
print(hash_table)

print(get('blue'))


