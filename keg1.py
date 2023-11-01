def convert_to_minutes(weeks, days, hours, minutes):
    return (weeks * 7 * 24 * 60) + (days * 24 * 60) + (hours * 60) + minutes

def curried_converter(weeks):
    def curry1(days):
        def curry2(hours):
            def curry3(minutes):
                return convert_to_minutes(weeks, days, hours, minutes)
            return curry3
        return curry2
    return curry1

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

output_data = []

for entry in data:
    parts = entry.split()
    weeks = int(parts[0])
    days = int(parts[2])
    hours = int(parts[4])
    minutes = int(parts[6])
    
    converter = curried_converter(weeks)(days)(hours)(minutes)
    output_data.append(converter)

print(output_data)
