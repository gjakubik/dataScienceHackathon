#!/usr/bin/env python3

from readCsv import ReadCSV

def main():
    data = ReadCSV("terrorismData.csv")
    topData = data.dataFrame.head()
    print(topData)
    for i, line in enumerate(data.dataFrame):
        if i > 50:
            break
        
        #print(line)


if __name__ == "__main__":
    main()