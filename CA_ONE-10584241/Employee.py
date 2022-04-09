# To validate the output of each test cases, importing unittest framework.
import unittest

# Defining the class Employee.
class Employee:

    # Initialize to the data members of the class using constructor.
    def _init_(self, Staff_id, first_name, last_name, reg_hours, hourly_rate, ot_multiple, tax_credit, standard_band):
        # To access the variable in globally in class, defining self.
        # initialising the variable
        self.Staff_id = Staff_id
        self.first_name = first_name
        self.last_name = last_name
        self.reg_hours = reg_hours
        self.hourly_rate = hourly_rate
        self.ot_multiple = ot_multiple
        self.tax_credit = tax_credit
        self.standard_band = standard_band

    # defining a method computePayment by passing parameters of hours_worked and date
    def computePayment(self, hours_worked, date):
        self.hours_worked = hours_worked
        self.date = date
        # declaring a dictionatary
        emp_info = {}

        self.regular_rate = self.hourlyRate
        self.standard_rate_pay = self.standard_band  # if self.grossPay > self.standardBand else 0

        if self.reg_hours > self.hours_worked:
        else:
            self.overtime_hours_worked = 0

        if self.overtime_hours_worked != 0 and self.hours_worked > self.reg_hours:
            self.overtime_rate = round(self.regular_rate + (self.ot_multiple * self.overtime_hours_worked),2)
        else:
            self.overtime_rate = 0

        self.overtime_pay = self.overtime_rate * self.overtime_hours_worked if self.hoursWorked > self.regHours else 0


        if self.overtime_rate != 0 and self.hours_worked > self.reg_hours:
            self.overtime_pay = self.overtime_rate * self.overtime_hours_worked
        else:
            self.overtime_pay = 0

        #self.overtime_pay = self.overtime_rate * self.overtime_hours_worked if self.hours_worked > self.reg_hours else 0

        self.gross_pay = self.regular_pay + self.overtime_pay

        if self.gross_pay > self.standard_band:
            self.higher_rate_pay = self.gross_pay - self.standard_rate_pay
        else:
            self.higher_rate_pay = 0

        self.standard_tax = round(self.standard_rate_pay * 0.20,2)
        self.higher_tax = round(self.higher_rate_pay * 0.40,2)
        self.prsi = round(self.gross_pay * 0.04, 2)
        self.total_tax = self.standard_tax + self.higher_tax

        if self.total_tax > self.tax_credit:
            self.net_tax = round(self.total_tax - self.tax_credit,2)
        else:
            self.net_tax = self.total_tax

        self.net_deductions = round(self.net_tax + self.prsi, 2)
        self.net_pay = round(self.gross_pay - self.net_deductions, 2)

        emp_info["Staff Id"] = self.Staff_id
        emp_info["Last Name"] = self.last_name
        emp_info["First Name"] = self.first_name
        emp_info['Regular Hours Worked'] = self.reg_hours
        emp_info["Overtime Hours Worked"] = self.overtime_hours_worked
        emp_info["Regular Rate"] = self.hourly_rate
        emp_info["Overtime Rate"] = self.overtime_rate
        emp_info["Regular Pay"] = self.regular_pay
        emp_info["Overtime Pay"] = self.overtime_pay
        emp_info["Gross Pay"] = self.gross_pay
        emp_info["Standard Rate Pay"] = self.standard_band
        emp_info["Higher Rate Pay"] = self.higher_rate_pay
        emp_info["Standard Tax"] = self.standard_tax
        emp_info["Higher Tax"] = self.higher_tax
        emp_info["Total Tax"] = self.total_tax
        emp_info["Tax Credit"] = self.tax_credit
        emp_info["Net Tax"] = self.net_tax
        emp_info["PRSI"] = self.prsi
        emp_info["Net Deductions"] = self.net_deductions
        emp_info["Net Pay"] = self.net_pay
        print(emp_info)
        return emp_info
