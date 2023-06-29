import textgrid
import csv
import os


dir_path = os.path.dirname(os.path.abspath(__file__))
fiel_name = "common_voice_de_27916918"
file_path = dir_path + "/" + fiel_name


tg = textgrid.TextGrid.fromFile(dir_path + "/" + fiel_name + ".TextGrid")
csv_input = [["phone"], ["end_time"]]


print("------- IntervalTier Example -------")
t = tg.tiers
for i in range (len(tg.getNames())): 
    if (tg[i].name == "phones"): 
        print(tg[i].name)
        for j in range (len(tg[i].intervals)):
            print(tg[i][j].mark)
            csv_input[0].append(tg[i][j].mark)
            csv_input[1].append(tg[i][j].maxTime)

with open(dir_path + "/" + fiel_name +".csv", 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(csv_input)
