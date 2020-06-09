import csv
def read_data ():
    data = []
    with open('./data/avocado.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data

def extract_data ():
    data = read_data()

    year = []
    averagePrice = []
    volume = []
    region = []
    date = []

    for row in data:
        year_t = int(row['year'])
        year.append(year_t)

        averageprice_t = int(row['averagePrice'])
        averagePrice.append(averageprice_t)

        volume_t = int(row['volume'])
        volume.append(volume_t)

        region_t = row['region']
        region.append(region_t)

        date_t = int(row['date'])
        date.append(date_t)

    return year, averagePrice, volume, region, date

