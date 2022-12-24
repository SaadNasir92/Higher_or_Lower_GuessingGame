import pandas

# table = pandas.read_csv('weather_data.csv')
# condition_temp = 0
# sunny_rows = (table[table.condition == 'Sunny'])
# monday_row = table[table.day == 'Monday']


gray_sq = 0
cinnamon_sq = 0
black_sq = 0

table = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
total = table.Hectare_Squirrel_Number.sum()
gray_rows = table[table.Primary_Fur_Color == 'Gray']
cinnamon_rows = table[table.Primary_Fur_Color == 'Cinnamon']
black_rows = table[table.Primary_Fur_Color == 'Black']

gray_sq += gray_rows.Hectare_Squirrel_Number.sum()
cinnamon_sq += cinnamon_rows.Hectare_Squirrel_Number.sum()
black_sq += black_rows.Hectare_Squirrel_Number.sum()

new_csv_data = {
    "Colors": ['Gray', 'Cinnamon', 'Black'],
    "Amount": [gray_sq, cinnamon_sq, black_sq]
}

blah = pandas.DataFrame(new_csv_data)
blah.to_csv('lit_squir.csv')


