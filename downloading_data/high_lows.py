import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename = 'death_valley_2014.csv'
# the uselfullness in doing this is that 
# it makes your code more usable by and easy to simplt
# change the filename and see a nice graph
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
# isnt this why data scientist spend time mining 

    print("\n Should print all the dates ")
    dates, highs, lows = [], [], []

    for row in reader:
        try:

            current_data = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])

        except ValueError:
            print(current_data, " missing data.")
        else:
            dates.append(current_data)
            lows.append(low)
            highs.append(high)

    print(dates)
    print(highs)

    # any_list = [(x[0]) for x in reader]
    # print(any_list)

    # highs = [(int(x[1])) for x in reader]
    # print(highs)


    # dates = []
    # for row in reader:
    #     current_data = datetime.strptime(row[0], "%Y-%m-%d")
    #     dates.append(current_data)
    # print(dates)

    # dates = [(datetime.strptime(int(x[0]), '%Y-%m-%d')) for x in reader]
    # print(dates)
    

    
        


# for index , column_header in enumerate(header_row):
#     print(index, column_header)
# the enumerte fucntion will let us see the index postito of
# every header item to make gathering data easier.



fig = plt.figure(dpi=100, figsize=(20, 6))
y = np.([range(100)
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)
# the shading being used here helps us better see and visualize the 
# main differnece in the tempeture

# format plot
plt.title("Daily high tempatures, 2014", fontsize=24)
plt.xlabel('', fontsize=6)
fig.autofmt_xdate()
plt.ylabel("Tempeture (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=15)

plt.show()


