"""===========================================================================================
* Name : srm_587_InsertZ.py
* Author: taikido
* Description: TopCoder SRM 587: Div2 L1 (Simple Search, Iteration, String Manipulation)
* Source: http://community.topcoder.com/stat?c=problem_statement&pm=12700
* Date: Tues.Dec.10.2013
*============================================================================================="""

class InsertZ:    
    def canTransform(self, init, goal):        
        if init == goal:
            return "Yes"
        newS = ""
        
        for i in range(len(goal)):
            if goal[i] != "z":
                newS += goal[i]
                
        if init == newS:
            return "Yes"
        else:
            return "No"
        
        
    #Using string Replacement
    def canTransform_simple(self, init, goal):
        return "Yes" if (goal.replace('z','') == init) else "No"
        
if __name__ == "__main__":
    init = "opdlfmvuicjsierjowdvnx"
    goal = "zzopzdlfmvzuicjzzsizzeijzowvznxzz"  
    
    init = "mvixrdnrpxowkasufnvxaq"
    goal = "mvizzxzzzrdzznzrpxozzwzzkazzzszzuzzfnvxzzzazzq"
    
    s = InsertZ()
    print s.canTransform_simple(init, goal)
    print s.canTransform(init, goal)
 