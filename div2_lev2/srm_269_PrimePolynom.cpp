/** ===========================================================================================
* Name : srm_269_PrimePolynom.cpp
* Author: taikido
* Description: TopCoder SRM 269: Div2 L2 (Brute Force)
* Source: http://community.topcoder.com/stat?c=problem_statement&pm=4475
* Date: Sun.Dec.8.2013
*=============================================================================================**/


#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;

class PrimePolynom{

	public:
		bool isPrime(int x){
			if (x < 2) return false;

			for (int i=2; i < sqrt(x) + 1; i++){
				if (x % i == 0 ) return false;
			}
			return true;
		}

		int sqr(int x){
			return x*x;
		}

		int reveal(int A, int B, int C){

			cout << "\n\n---------------------------\n\n";
			for (int i=0; i< 90; i++){
				int sum = (A * sqr(i)) + (B * i) + C;

				printf("sum: %d, i %d \n", sum, i);
				if (! isPrime(sum))
					return i;
			}

			return -1;

		}
		void printPrimes(){
			for (int i=0; i <= 100; i++){
				if (isPrime(i)) cout << i << endl;
			}
		}


};


//Passed 289/290 System Tests
//Fails system test 78: args {1, -1, 2}, Expected 2, Got 0
void testClass(){

	PrimePolynom p;
	//p.printPrimes();

	cout << p.reveal(1, -1, 2) << endl;
	cout << p.reveal(1, -1, 41) << endl;
	cout << p.reveal(1, 1, 41) << endl;
	cout << p.reveal(1, 1, -13) << endl;
	cout << p.reveal(1, -15, 97) << endl;
	cout << p.reveal(1, -79, 1601) << endl;
}

int main(){
	testClass();
	return 0;
}
