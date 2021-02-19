import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename = 'history_data.csv'
# the uselfullness in doing this is that 
# it makes your code more usable by and easy to simplt
# change the filename and see a nice graph
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)


    for index , column_header in enumerate(header_row):
        print(index, column_header)
    # dates = []
    # for row in reader:
    #     date_row = row[1]
    #     dates.append(date_row)
    # print(dates)
    


    print("\n Should print all the dates ")
 
    dates, wind_speed = [], []
    for row in reader:
        try:

            current_data = datetime.strptime(row[1], "%m/%d/%Y")
            speed = row[10]
          

        except ValueError:
            print(current_data, " missing data.")
        else:
            if speed != int:
                wind = int(float(speed))
                wind_speed.append(wind)


            dates.append(current_data)
            

    print(dates)
   


fig = plt.figure(dpi=100, figsize=(20, 6))


plt.plot(dates, wind_speed, c='blue', alpha=0.5)
# plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)
# the shading being used here helps us better see and visualize the 
# main differnece in the tempeture

# format plot
plt.title("Daily wind in Netherlands", fontsize=24)
plt.xlabel('', fontsize=6)
plt.ylim(0, 50)
fig.autofmt_xdate()
plt.ylabel("Weather in miles", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=15)

plt.show()
