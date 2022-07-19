# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 17:22:18 2022

@author: tanvi
"""
import unittest
import sys
from io import StringIO
from Task import DateTime

class TestDateTime(unittest.TestCase):
    
    def setUp(self):
        self.dt1 = DateTime()
        self.out, sys.stdout = sys.stdout, StringIO()
    
    def test_storedata(self):
        self.dt1.StoreData("29.02.2023 04:30")
        self.dt1.StoreData("01.01.2023 12:30")
        self.dt1.StoreData("31.01.2023 23:59")
        self.dt1.StoreData("31.12.2023 00:01")
        self.assertEqual(self.dt1.store_datetime, ["29.02.2023 04:30", "01.01.2023 12:30", "31.01.2023 23:59", "31.12.2023 00:01" ])
        
    def test_checkdataWithString(self):
        self.dt1.CheckData("29.02.2024", "04:30")
        self.dt1.CheckData("01.01.2023", "12:30")
        self.dt1.CheckData("31.01.2023", "23:59")
        self.dt1.CheckData("31.12.2023", "00:01")
        self.assertEqual(self.dt1.store_datetime, ["29.02.2024 04:30", "01.01.2023 12:30", "31.01.2023 23:59", "31.12.2023 00:01"])
        
    def test_checkdataWithWrongFormat(self):      
        self.dt1.CheckData("29.02.2024", "04.30")
        self.assertEqual(sys.stdout.getvalue().strip(), "please enter the date(dd.mm.yyyy) and time(hh:mm) in correct format.")
    
    def test_checkdataWithPastDate(self):        
        self.dt1.CheckData("29.02.2020", "04:30")
        self.assertEqual(sys.stdout.getvalue().strip(), "please enter a future date & time.")
                
    def test_DisplayMessage(self):
        list1 = ["19.07.2022 15:28"]
        self.dt1.DisplayMessage(list1)
        self.assertEqual(sys.stdout.getvalue().strip(),'The first date has been reached!(19.07.2022-15:28)')
        


if __name__ == '__main__':
    unittest.main()