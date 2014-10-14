/** ===========================================================================================
* Name : srm_304_RugSizes.cpp
* Author: taikido
* Description: TopCoder SRM 304: Div2 L1 (Brute Force, Simple Math)
* Source: http://community.topcoder.com/stat?c=problem_statement&pm=6195
* Date: Sun.Dec.8.2013
*=============================================================================================**/


#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;

class RugSizes{

	public:
		bool isEven(int x){
			return (x % 2 == 0);
		}

		int rugCount(int area){
			int numRugs = 0;

			for (int i=1; i <= sqrt(area); i++){
				int x = area/i;
				if (area % i == 0 && (isEven(x) && isEven(i)) && x != i) continue;
				if (area % i == 0 )	numRugs++;
			}
			return numRugs;
		}
};

void testRugSizes(){
	RugSizes r;
	printf("Num of rugs: %d \n", r.rugCount(4));
	printf("Num of rugs: %d \n", r.rugCount(8));
	printf("Num of rugs: %d \n", r.rugCount(30));
}

int main() {

	testRugSizes();
	return 0;
}
