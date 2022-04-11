# Code is uploaded in Github : https://github.com/kapilgangwani007/B9IS123_2122_TMD2.git
# In this script, we are calculating the tax deduction, gross pay and net pay of a person
#  based on the hours he/she has worked on a specific date.

# To validate the output of each test cases, importing unittest framework.
import unittest
# defining the class Employee.
class Employee:

    # Initialize to the data members of the class using constructor.
    def __init__(self, Staff_id, first_name, last_name, reg_hours, hourly_rate, ot_multiple, tax_credit, standard_band):
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
        # total hours worked by a person
        self.hours_worked = hours_worked
        self.date = date

        # declaring a dictionatary to store all the payment details
        emp_info = {}

        # regular rate is equal to the rate per hour which is already given
        self.regular_rate = self.hourly_rate

        # standard rate is equal to the standard band which is already given
        self.standard_rate_pay = self.standard_band  # if self.grossPay > self.standardBand else 0

        # regular hours is based on the hours worked, if hours worked is less than given reg hours then
        # regular hours will be same as hours worked.
        if self.reg_hours > self.hours_worked:
            self.reg_hours = self.hours_worked

        #regular pay is the multiple of regular rate and regular hours
        self.regular_pay = self.reg_hours * self.regular_rate

        # overtime hours worked depends on both hours worked and regular hours, if hours worked is greater than regular
        # hours then subtract of hours worked and reg hours is overtime hours worked
        if self.hours_worked > self.reg_hours:
            self.overtime_hours_worked = self.hours_worked - self.reg_hours
        else:
            self.overtime_hours_worked = 0

        # overtime rate is the multiple of overtime per hour rate and hourly rate.
        self.overtime_rate = self.ot_multiple * self.hourly_rate

        # overtime pay depends on both hours worked and regular hours, if regular hours is greater than hours worked then overtime pay is 0
        # otherwise its multiple of overtime rate and overtime hours worked.
        if self.overtime_rate != 0 and self.hours_worked > self.reg_hours:
            self.overtime_pay = self.overtime_rate * self.overtime_hours_worked
        else:
            self.overtime_pay = 0

        # Gross pay is the sum of regular pay and overtime pay if no overtime is done by person than overtime pay is 0.
        self.gross_pay = self.regular_pay + self.overtime_pay

        # higher rate pay depends on the gross pay and staandard band, if standard pay is greater than gross pay then higher rate pay is 0
        # otherwise its a substraction of standard rate from gross pay.
        if self.gross_pay > self.standard_band:
            self.higher_rate_pay = self.gross_pay - self.standard_rate_pay
            # As given standard tax is 20% of standard rate pay
            self.standard_tax = round(self.standard_rate_pay * 0.20, 2)
        else:
            self.standard_tax = self.gross_pay * 0.20
            self.higher_rate_pay = 0

        # As given higher tax is 40% of higher rate pay
        self.higher_tax = round(self.higher_rate_pay * 0.40,2)

        # As given PRSI is 4% of gross pay
        self.prsi = round(self.gross_pay * 0.04, 2)

        # total tax is sum of standard tax and higher tax
        self.total_tax = self.standard_tax + self.higher_tax

        # net tax depends on the total tax and tax credit, if tax tax is greater than total tax then net tax will be 0
        # otherwise substraction of given tax credit from total tax
        if self.total_tax > self.tax_credit:
            self.net_tax = round(self.total_tax - self.tax_credit,2)
        else:
            self.net_tax = self.total_tax

        # net deduction is sum of net tax and PRSI
        self.net_deductions = round(self.net_tax + self.prsi, 2)

        # net pay is substraction of net deduction from gross pay
        self.net_pay = round(self.gross_pay - self.net_deductions, 2)

        # Add employee data in the dictionary variable
        emp_info["Staff Id"] = self.Staff_id
        emp_info["First Name"] = self.first_name
        emp_info["Last Name"] = self.last_name
        emp_info["Date"] = self.date
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


# Test class to validate some scenarios of above script.
class TestSalary(unittest.TestCase):

    # To validate, net pay should be or equal to the gross pay.
    def testNetPayCannotExceedGrossPay(self):
        given_data = Employee(10584241, 'Gangwani', 'Kapil', 37, 16, 1.5, 72, 710)
        result = given_data.computePayment(22, '31/12/2021')
        self.assertLessEqual(result['Net Pay'], result['Gross Pay'])

    # To validate, higher tax should be greater than or equal to 0.
    def testHigherTaxCannotBeNegative(self):
        given_data = Employee(10584241, 'Gangwani', 'Kapil', 37, 16, 1.5, 72, 710)
        result = given_data.computePayment(42, '31/12/2021')
        self.assertGreaterEqual(result['Higher Tax'], 0)

    # To validate, overtime hours should be greater than or equal to 0.
    def testOvertimeHoursCannotBeNegative(self):
        given_data = Employee(10584241, 'Gangwani', 'Kapil', 37, 16, 1.5, 72, 710)
        result = given_data.computePayment(0, '31/12/2021')
        self.assertGreaterEqual(result['Overtime Hours Worked'], 0)

    # To validate, overtime pay should be greater than or equal to 0.
    def testOvertimePayCannotBeNegative(self):
        given_data = Employee(10584241, 'Gangwani', 'Kapil', 37, 16, 1.5, 72, 710)
        result = given_data.computePayment(2, '31/12/2021')
        self.assertGreaterEqual(result['Overtime Pay'], 0)

    # To validate, net pay should greater than or equal to 0.
    def testNetPayCannotBeNegative(self):
        given_data = Employee(10584241, 'Gangwani', 'Kapil', 37, 16, 1.5, 72, 710)
        result = given_data.computePayment(10, '31/12/2021')
        self.assertGreaterEqual(result['Net Pay'], 0)

    # To validate, regular hours should be less than or equal to worked hours.
    def testRegularHoursCannotBeMoreThanHoursWorked(self):
        given_data = Employee(10584241, 'Gangwani', 'Kapil', 37, 16, 1.5, 72, 710)
        result = given_data.computePayment(37, '31/12/2021')
        self.assertLessEqual(result['Regular Hours Worked'], result["Regular Hours Worked"] + result["Overtime Hours Worked"])


# Test class to validate some scenarios of above script.
class TestSalary(unittest.TestCase):

    # To validate, net pay should be or equal to the gross pay.
    def testNetPayCannotExceedGrossPay(self):
        given_data = Employee(10584241, 'Gangwani', 'Kapil', 37, 16, 1.5, 72, 710)
        result = given_data.computePayment(22, '31/12/2021')
        self.assertLessEqual(result['Net Pay'], result['Gross Pay'])

    # To validate, higher tax should be greater than or equal to 0.
    def testHigherTaxCannotBeNegative(self):
        given_data = Employee(10584241, 'Gangwani', 'Kapil', 37, 16, 1.5, 72, 710)
        result = given_data.computePayment(42, '31/12/2021')
        self.assertGreaterEqual(result['Higher Tax'], 0)

    # To validate, overtime hours should be greater than or equal to 0.
    def testOvertimeHoursCannotBeNegative(self):
        given_data = Employee(10584241, 'Gangwani', 'Kapil', 37, 16, 1.5, 72, 710)
        result = given_data.computePayment(0, '31/12/2021')
        self.assertGreaterEqual(result['Overtime Hours Worked'], 0)

    # To validate, overtime pay should be greater than or equal to 0.
    def testOvertimePayCannotBeNegative(self):
        given_data = Employee(10584241, 'Gangwani', 'Kapil', 37, 16, 1.5, 72, 710)
        result = given_data.computePayment(2, '31/12/2021')
        self.assertGreaterEqual(result['Overtime Pay'], 0)

    # To validate, net pay should greater than or equal to 0.
    def testNetPayCannotBeNegative(self):
        given_data = Employee(10584241, 'Gangwani', 'Kapil', 37, 16, 1.5, 72, 710)
        result = given_data.computePayment(10, '31/12/2021')
        self.assertGreaterEqual(result['Net Pay'], 0)

    # To validate, regular hours should be less than or equal to worked hours.
    def testRegularHoursCannotBeMoreThanHoursWorked(self):
        given_data = Employee(10584241, 'Gangwani', 'Kapil', 37, 16, 1.5, 72, 710)
        result = given_data.computePayment(37, '31/12/2021')
        self.assertLessEqual(result['Regular Hours Worked'], result["Regular Hours Worked"] + result["Overtime Hours Worked"])