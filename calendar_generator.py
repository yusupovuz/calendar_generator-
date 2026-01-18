class CalendarGenerator:
    def is_leap_year(self,year):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        return False

    def get_days_in_month(self,month,year):
        if month in [1,3,5,7,8,10,12]:
            return 31
        elif month == 2:
            if self.is_leap_year(year):
                return 29
            return 28
        elif month<12:
            return 30
        else:
            return 'Wrong month number!!!'
        

    def get_start_day_of_month(self,month,year):
        if month == 1:
            month = 13
            year -= 1
        elif month == 2:
            month = 14
            year -= 1
        k = year%100
        j = year//100
        wd = ((1+13*(month+1)//5+k+k//4+j//4+5*j)%7-1)%7
        return wd 
    
    def build_grid_string(self,start_day_index,total_days):
        s = ''
        print('   '*start_day_index,end='')
        for i in range(1,total_days+1):
            if (i+start_day_index)%7 == 0:
                s+=f'{i:2d} '
                s+='\n'
            else:
                s+=f'{i:2d} '
        return s


    def generate_calendar(self,month,year):
        print('      ',month,year)
        print('Su Mo Tu We Th Fr Sa')
        return self.build_grid_string(self.get_start_day_of_month(month,year),self.get_days_in_month(month,year))

    


a = CalendarGenerator()
print(a.generate_calendar(1,2026))