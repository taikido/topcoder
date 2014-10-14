"""===========================================================================================
* Name : srm_258_AutoLoan.py
* Author: taikido
* Description: TopCoder SRM 258: Div2 L2 or Div1 L1 (Advanced Math, Search)
* Source: http://community.topcoder.com/stat?c=problem_statement&pm=3970&rd=7993
* Date: Fri.Jan.10.2014
*============================================================================================="""


class AutoLoan:    
    def p(self, x, target):
        return True if x >= target else False
    

    def computeBalance(self, price, monthlyPayment, loanTerm, annualInterest):
        monthlyInterest = annualInterest/12/100
        #         print "-----------------------------------------\n\n"
        #         print "annualInterest: ", annualInterest
        #         print
        
        balance = price
        
        for i in range(loanTerm):
            interest = (balance + balance*monthlyInterest)
            balance = interest - monthlyPayment
            #             print "[{0}]: interest: {1}, balance: {2}".format(i+1, interest, balance)
            
        return balance
    
    #The return value must be within 1e-9 absolute or relative error of the actual result.
    def interestRate(self, price, monthlyPayment, loanTerm):
        low = 0
        high = 100
        
        max_steps = 100
        steps = 0  
        
        while steps < max_steps:
            annualInterest =  (low + high)/2.0   
            balance = self.computeBalance(price, monthlyPayment, loanTerm, annualInterest)  
            
            if balance >= 0:
                high = annualInterest
            else:
                low = annualInterest
                
            #             print "{0} --> low: {1}, high: {2}, balance: {3}".format(steps, low, high, balance)
                
            steps += 1
            
        return low                
    
   

    
def run_trivial_test_cases():

    s = AutoLoan()
    
    #Test Case 0
    price, monthlyPayment, loanTerm = 6800, 100, 68
    print s.interestRate(price, monthlyPayment, loanTerm)      
    
    #Test Case 1
    price, monthlyPayment, loanTerm = 2000, 510, 4
    print s.interestRate(price, monthlyPayment, loanTerm)     
    
    #Test Case 2
    price, monthlyPayment, loanTerm = 15000, 364, 48
    print s.interestRate(price, monthlyPayment, loanTerm)   


    '''
    #9.56205462458368
    price = 2000
    monthlyPayment = 510
    loanTerm = 4 
    annualInterest = 9.56205462458368
    s.computeBalance(price, monthlyPayment, loanTerm, annualInterest)
    
    #From Problem Statement
    Here, we do pay a little interest. At 9.562% annual interest, that means each month we pay 0.7968% 
    of the balance in interest. Our payment schedule looks like this:
    Month | + Interest | - Payment | = Balance
    ------------------------------------------
       |            |           |  2000.00
    1  |     15.94  |   510.00  |  1505.94
    2  |     12.00  |   510.00  |  1007.94
    3  |      8.03  |   510.00  |   505.97
    4  |      4.03  |   510.00  |     0.00
    '''
        
if __name__ == "__main__":
    run_trivial_test_cases()

