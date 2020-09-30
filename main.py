#!/usr/bin/env python3

from readCsv import ReadCSV

def main():
    data = ReadCSV("terrorismData.csv")
    topData = data.df.head()
    print(topData)
    print(data.df.dtypes)
    


if __name__ == "__main__":
    main()