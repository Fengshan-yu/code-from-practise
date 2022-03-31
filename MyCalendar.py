# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 08:21:51 2022

@author: adminstrator
"""

import calendar

class MyCalendar:
    def __init__(self, year, weekday):
        self.year = year
        self.weekday = weekday
       
    def count_weekday_in_year(self):
        day_list = []
        self.day_list = day_list
        c=calendar.Calendar()
        
        for x in range(1, 13):
            for data in c.monthdays2calendar(self.year, x):
                tuples = [t for t in data if t[0] != 0 and t[1] == self.weekday]
                for tuple in tuples:
                    day_list.append(tuple)       

        return len(self.day_list)
        
My_calender = MyCalendar(2019, 0)
print(My_calender.count_weekday_in_year())