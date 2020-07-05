class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        arr = date.split('-')
        y=int(arr[0])
        m=int(arr[1])
        d=int(arr[2])
        if m ==1 : return d
        calender ={1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        if ((y%4 ==0) and (y%100) !=0) or (y%400==0):
            calender[2]=29
        for i in range(1,m):
            d += calender[i]
            return d