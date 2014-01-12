"""===========================================================================================
* Name : srm_277_UnionOfIntervals.py
* Author: taikido
* Description: TopCoder SRM 277: Div2 L3 or Div1 L1 (Search, Sorting)
* Source: http://community.topcoder.com/stat?c=problem_statement&pm=4823
* Date: Sat.Jan.11.2014
*============================================================================================="""


class UnionOfIntervals:
    def nthElement(self, lowerBound, upperBound, n):
#         seq_lists = [range(lowerBound[i], upperBound[i]+1) for i in range(len(lowerBound))] #[[1, 2, 3], [5, 6, 7]]
        seq_lists = [j for i in range(len(lowerBound)) for j in range(lowerBound[i], upperBound[i]+1)] #[1, 2, 3, 5, 6, 7]
        seq_lists.sort()
        print seq_lists
        print seq_lists[n]
        print
        

s = UnionOfIntervals()
# print sorted(s.merge([1,2,3,5], [4,5]))
s.nthElement([1,5], [3,7], 4)
s.nthElement([1,3], [4, 5], 3)
s.nthElement([-1500000000], [1500000000], 1500000091) #memory error


