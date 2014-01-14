"""===========================================================================================
* Name : srm_189_Mortgage.py
* Author: taikido
* Description: TopCoder SRM 189: Div2 L3 or Div1 L1 (Math, Search)
* Source: http://community.topcoder.com/stat?c=problem_statement&pm=2427&rd=4765
* Date: Tues.Jan.14.2014
*============================================================================================="""

from math import ceil

class Mortgage:
    def isPaymentEnough(self, loan, interest, term, monthlyPayment):
        interestRate = interest/(1000.0) #interest/(loan*1.0)
        monthlyTerms = term*12        
        verbose = 0
        amt_owed = loan
        
        if verbose:        
            print "\n\n****Monthly terms: {0},  monthlyPayment: {1}".format(monthlyTerms, monthlyPayment)        
            print "month    after making payment    after interest accrues"
            print "-------------------------------------------------------"
        
        for i in range(monthlyTerms):
            amt_owed1 = amt_owed - monthlyPayment
            #Could pay off loan early?
            if amt_owed1 <= 0:
                return True
            amt_owed = ceil(amt_owed1 * (term + interestRate/monthlyTerms))
            if verbose:
                print "{0}    \t{1}    \t{2}".format(i+1, amt_owed1, amt_owed)

            
        return False
    
    def p(self, x, val):
        return True if x >= val else False
    
    def monthlyPayment(self, loan, interest, term):
        low, high = 0, loan
        
        max_steps = 200
        steps = 0  
        
        while steps < max_steps:
            monthlyPayment =  (low + high)/2.0   
            monthlyPaymentEnough = self.isPaymentEnough(loan, interest, term, monthlyPayment)

            
            if monthlyPaymentEnough:
                high = monthlyPayment
            else:
                low = monthlyPayment    
                
            steps += 1  
        return int(ceil(high))     
  

  
def run_trivial_tests():
    
    m = Mortgage()

    #Test Case 0
    loan, interest, term = 1000, 50, 1 #86
    print "monthly payment: ", m.monthlyPayment(loan, interest, term)
    
    #Test Case 1
    loan, interest, term = 2000000000, 6000, 1 #671844808
    print "monthly payment: ", m.monthlyPayment(loan, interest, term)  
    
    #Test Case 2
    loan, interest, term = 1000000, 1000000, 1000 #988143
    print "monthly payment: ", m.monthlyPayment(loan, interest, term)    
    
    #Test Case 3   
    loan, interest, term = 1000000, 129, 30 #10868
    print "monthly payment: ", m.monthlyPayment(loan, interest, term)     
    
    #Test Case 4
    loan, interest, term = 1999999999, 1000000, 1 #1976284585
    print "monthly payment: ", m.monthlyPayment(loan, interest, term)   
   

  
if __name__ == "__main__":
    run_trivial_tests()


"""
Current Output

monthly payment:  86
monthly payment:  671844808
monthly payment:  999001        Should be: #988143
monthly payment:  966668        Should be: #10868
monthly payment:  1976284585
"""

  
        
def test_isPaymentEnough():
    m = Mortgage()

    loan, interest, term, monthlyPayment = 1000, 50, 1, 86 #50/1000
    m.isPaymentEnough(loan, interest, term, monthlyPayment)
    
    loan, interest, term, monthlyPayment = 2000000000, 6000, 1, 671844808
    m.isPaymentEnough(loan, interest, term, monthlyPayment)     
    
    loan, interest, term, monthlyPayment = 1000000, 1000000, 1000, 988143
    m.isPaymentEnough(loan, interest, term, monthlyPayment) 
     
    loan, interest, term, monthlyPayment = 1000000, 129, 30, 10868
    m.isPaymentEnough(loan, interest, term, monthlyPayment)     
     
    loan, interest, term, monthlyPayment = 1999999999, 1000000, 1, 1976284585
    m.isPaymentEnough(loan, interest, term, monthlyPayment)
