class Employee :

   def __init__(self,StaffID, LastName, FirstName, RegHours, HourlyRate, OTMultiple, TaxCredit, StandardBand):
    self.StaffID = StaffID
    self.LastName = LastName
    self.FirstName = FirstName
    self.RegHours = RegHours
    self.HourlyRate = HourlyRate
    self.OTMultiple = OTMultiple
    self.TaxCredit = TaxCredit
    self.StandardBand = StandardBand

    def Computepayment(self, HoursWorked, date):
      self.HoursWorked = HoursWorked
      self.date = date


    def Calculate():

 /*
Worked hours = Entered by User (42)
Regular Worked Hours = if(RegHours)RegHours (37)
Overtime Hours Worked = if(Worked hours > RegHours) ? RegHours - Worked hours: Worked hours; (5)
Regular Rate = Hourlyrate (16)
Overtime Rate = if((Worked hours > RegHours) ? Hourlyrate+(OTMultiple*Overtime Hours Worked) : 0) 16+(1.5*5) = 23.5
Regular Pay = RegHours*Hourlyrate (37*16 = 592)
Overtime Pay = if((Worked hours > RegHours) ? Overtime Rate*Overtime Hours Worked : 0; (23.5*5) = 117.5 
Gross Pay = Regular Pay + Overtime Pay (592+117.5 = 709.5)
Standard Rate Pay = StandardBand
Higher Rate Pay = if(Gross Pay>Standard Rate Pay) ? Gross Pay - Standard Rate Pay : 0 ; 712-710 = 2 
Standard Tax = 20% of Standard Rate Pay (710*.20 = 142)
Higher Tax = 40% of Higher Rate Pay (2*.40 = 0.8)
Total Tax = Standard Tax + Total Tax (142.80)
Tax Credit = TaxCredit (72)
Net Tax = Total Tax - TaxCredit(142.80 - 72 = 70.8)
PRSI = 4% of Net Tax (70.8*.04 = 28.32)
Net Deductions = Net Tax + Net Deductions = 70.8+28.32= 99.12
Net Pay = Gross Pay - Net Deductions = 712 - 99.12 = 612.88
*/
        
       




