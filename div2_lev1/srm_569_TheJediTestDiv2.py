"""===========================================================================================
* Name : srm_569_TheJediTestDiv2.py
* Author: taikido
* Description: TopCoder SRM 441: Div2 L1 (Simple Search, Iteration)
* Source: http://community.topcoder.com/stat?c=problem_statement&pm=12404
* Date: Tues.Dec.10.2013
*============================================================================================="""

from math import ceil

class TheJediTestDiv2:
    
    def sumJedis(self, students, J, k):        
        jedi_counts = [ceil(students[i]/(J*1.0)) for i in range(len(students)) if i != k]        
        #print "jedi_counts: ", jedi_counts
        return sum(jedi_counts)
        
    def countSupervisors(self, students, Y, J):
        minJ = 10000000
         
        for i in range(len(students)):
            
            jCount = 0
            
            if Y < students[i]:
                studentsLeft = students[i] - Y
                #print "studentsLeft: ", studentsLeft
                jCount += ceil(studentsLeft/(J*1.0))       

                
                 
            jCount += self.sumJedis(students, J, i)
             
            if jCount < minJ:
                minJ = jCount
                 
        return int(minJ)
    
if __name__ == "__main__":
    j = TheJediTestDiv2()
    print j.countSupervisors((11,13,15), 9, 5)
     
    print
    print j.countSupervisors((0, 0, 0, 0, 0), 145, 21)
     
     
     
    print
    print j.countSupervisors((4, 7, 10, 5, 6, 55, 2), 20, 3)

