from datetime import datetime
from num2words import num2words
import time

class DateTime():
    
    def __init__(self):
        self.store_datetime = []
        
    def CheckData(self, Date_str, Time_str):
        try:
            datetime.strptime(Date_str, "%d.%m.%Y")
            datetime.strptime(Time_str, "%H:%M")
            DateTimeStr = Date_str +" "+ Time_str
            DateTimeStr = datetime.strptime(DateTimeStr, "%d.%m.%Y %H:%M")
            DateTimeNow = datetime.strptime(datetime.now().strftime("%d.%m.%Y %H:%M"), "%d.%m.%Y %H:%M")
            assert DateTimeStr > DateTimeNow
            
        except ValueError:
            print("please enter the date(dd.mm.yyyy) and time(hh:mm) in correct format.\n")              
        
        except AssertionError:
            print("please enter a future date & time.") 
                    
        else:
            self.StoreData(DateTimeStr.strftime("%d.%m.%Y %H:%M"))
            return True
        
        
    def StoreData(self, DateTimeStr):
        return self.store_datetime.append(DateTimeStr)
    
    def DisplayMessage(self, input_list):        
        for i in input_list:
            index = input_list.index(i)
            i = datetime.strptime(i, "%d.%m.%Y %H:%M")
            j = datetime.strptime(datetime.now().strftime("%d.%m.%Y %H:%M:%S"), "%d.%m.%Y %H:%M:%S")
            diff = (i - j).total_seconds()
            time.sleep(diff)
            print("The "+ num2words(index+1, to = 'ordinal') + " date has been reached!(" + i.strftime("%d.%m.%Y-%H:%M")+")")


if __name__ == "__main__":
    
    carry_on = True
    dt = DateTime()
    while True:
        try:
            input_num = int(input("How much data do you want to enter?"))
            break
        except ValueError:
            print("please enter an integer number only.")       
    for i in range(input_num):
        while carry_on:           
            Date_str = str(input("\nPlease enter a date: " ))
            Time_str = str(input("Please enter a time: "))
            if not dt.CheckData(Date_str, Time_str):
                continue
            break
    print("Thank you very much. I will notify them!")
    print("......")
    dt.DisplayMessage(dt.store_datetime)
    
