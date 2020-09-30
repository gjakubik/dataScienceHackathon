#!/usr/bin/env python3

import pandas as pd 
import numpy as np

dropCols = [
            "attacktype3",
            "attacktype3_txt",
            "corp1",
            "target1",
            "targtype2",
            "targtype2_txt",
            "targsubtype2",
            "targsubtype2_txt",
            "corp2",
            "target2",
            "natlty2",
            "natlty2_txt",
            "targtype3",
            "targtype3_txt",
            "targsubtype3",
            "targsubtype3_txt",
            "corp3",
            "target3",
            "natlty3",
            "natlty3_txt",
            "gsubname",
            "gname2",
            "gsubname2",
            "gname3",
            "gsubname3",
            "motive",
            "guncertain2",
            "guncertain3",
            "claim2",
            "claimmode2",
            "claimmode2_txt",
            "claim3",
            "claimmode3",
            "claimmode3_txt",
            "compclaim",
            "propcomment",
            "addnotes",
            "scite1",
            "scite2",
            "scite3",
            "dbsource",
            "INT_LOG",
            "INT_IDEO",
            "INT_MISC",
            "INT_ANY"
        ]

class ReadCSV():
    def __init__(self, filename):
        
        self.dataFrame = pd.read_csv(filename, low_memory=False)
        self.dataFrame.drop(columns=dropCols, inplace=True)
        self.dataFrame.set_index("eventid", inplace=True)
        
