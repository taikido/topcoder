"""===========================================================================================
* Name : srm_441_DifferentStrings.py
* Author: taikido
* Description: TopCoder SRM 441: Div2 L1 (Brute Force, Greedy, Simulation, String Manipulation)
* Source: http://community.topcoder.com/stat?c=problem_statement&pm=10376
* Date: Tues.Dec.10.2013
*============================================================================================="""

class DifferentStrings:    
    def countDiffs(self, A, B):
        count = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                count += 1
                
        return count
    
    #didn't need to explicitly Add chars to both ends of A (see simple_minimize)
    def shiftAndCountDiffs(self, A, B):
        diffLen = len(B) - len(A)
        
        endLen = diffLen

        startLen = 0
        
        min_diff = 51
        min_index = 0
        
        newA = ""
        minA = ""
        
        for i in range(diffLen + 1):
            endStr = "9" * endLen
            startStr = "9" * startLen
            newA = startStr + A + endStr

            
            diff = self.countDiffs(newA, B)

            
            if diff < min_diff:
                min_diff = diff
                min_index = i
                minA = newA

                
            endLen -= 1
            startLen += 1
                
        return [minA, min_diff, min_index]
            
            
            
    
    def minimize(self, A, B):
        if len(A) == len(B):
            return self.countDiffs(A, B)        
        else:
            #len(A) < len(B)
            if A in B:
                return 0
            else:
                [newA, min_diff, min_index] = self.shiftAndCountDiffs(A, B)                
                return self.countDiffs(newA[min_index:len(A)+min_index], B[min_index:len(A)+min_index])
            
    #Solution from Match Editorial
    def simple_minimize(self, A, B):      
        result = 999999999
        diff = len(B) - len(A)
        
        for shift in range(0, diff + 1):
            difference = 0            
            for i in range(len (A)):
                if A[i] != B[i + shift]:
                    difference += 1
            
            result = min(result, difference)
            
        return result

        
        
if __name__ == "__main__":
    d = DifferentStrings()
    A = "koder"
    B = "topcoder"
     
    A = "adaabc"
    B = "aababbc"
    diff = d.minimize(A, B)
     
    print "min diff: ", diff
     
    A = "kzmlggn"
    B = "egaegibovgisdrobpbrlxeqgdbicxueyqkewimbwvrhsouhuf"
    
    diff = d.minimize(A, B)    
    print "min diff: ", diff
    
    diff = d.simple_minimize(A, B)   
    print "min diff: ", diff

        
