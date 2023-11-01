def is_float(value):
    return isinstance(value, float)

def is_int(value):
    return isinstance(value, int)

def is_string(value):
    return isinstance(value, str)

def map_to_digits(value):
    if is_int(value):
        ratusan = value // 100
        puluhan = (value // 10) % 10
        satuan = value % 10
        return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}
    return value

random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]


data_float = tuple(filter(is_float, random_list))
data_int = tuple(filter(is_int, random_list))
data_string = list(filter(is_string, random_list))

data_int_mapped = tuple(map(map_to_digits, data_int))

print("Data Float:", data_float)
print("Data Int:")
for item in data_int_mapped:
    if isinstance(item, dict):
        print(item)
print("Data String:", data_string)
