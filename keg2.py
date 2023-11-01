def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

integer_data = []

for entry in data:
    parts = entry.split()
    integer_parts = list(filter(is_integer, parts))
    integer_data.append(integer_parts)

for item in integer_data:
    print(item)
