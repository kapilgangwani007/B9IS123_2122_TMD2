import unittest
import Employee

# Test class to validate some scenarios of above script.
class TestSalary(unittest.TestCase):

    # To validate, net pay should not be greater than gross pay.
    def testNetPayCannotExceedGrossPay(self):
        given_data = Employee.Employee(10584241, 'Gangwani', 'Kapil', 37, 16, 1.5, 72, 710)
        result = given_data.computePayment(22, '31/12/2021')
        self.assertLessEqual(result['Net Pay'], result['Gross Pay'])

    # To validate, higher tax should not be less than 0.
    def testHigherTaxCannotBeNegative(self):
        given_data = Employee.Employee(10584241, 'Gangwani', 'Kapil', 37, 16, 1.5, 72, 710)
        result = given_data.computePayment(42, '31/12/2021')
        self.assertGreaterEqual(result['Higher Tax'], 0)

    # To validate, overtime hours should not be less than 0.
    def testOvertimeHoursCannotBeNegative(self):
        given_data = Employee.Employee(10584241, 'Gangwani', 'Kapil', 37, 16, 1.5, 72, 710)
        result = given_data.computePayment(0, '31/12/2021')
        self.assertGreaterEqual(result['Overtime Hours Worked'], 0)

    # To validate, overtime pay should not be less than 0.
    def testOvertimePayCannotBeNegative(self):
        given_data = Employee.Employee(10584241, 'Gangwani', 'Kapil', 37, 16, 1.5, 72, 710)
        result = given_data.computePayment(2, '31/12/2021')
        self.assertGreaterEqual(result['Overtime Pay'], 0)

    # To validate, net pay should not be less than 0.
    def testNetPayCannotBeNegative(self):
        given_data = Employee.Employee(10584241, 'Gangwani', 'Kapil', 37, 16, 1.5, 72, 710)
        result = given_data.computePayment(10, '31/12/2021')
        self.assertGreaterEqual(result['Net Pay'], 0)

    # To validate, regular hours should not be greater than hours worked.
    def testRegularHoursCannotBeMoreThanHoursWorked(self):
        given_data = Employee.Employee(10584241, 'Gangwani', 'Kapil', 37, 16, 1.5, 72, 710)
        result = given_data.computePayment(37, '31/12/2021')
        self.assertLessEqual(result['Regular Hours Worked'], result["Regular Hours Worked"] + result["Overtime Hours Worked"])


if __name__ == '__main__':
    unittest.main()
