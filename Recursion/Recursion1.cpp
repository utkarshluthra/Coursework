/*

Create a program to find the summation of n numbers using recursion.

*/

#include<iostream>
using namespace std;

int summation(int n){
    if (n==0){
        return 0;
    }
    int prevSum = summation(n-1);
    return n + prevSum;
}

int main(){
    int n;
    cin>>n;
    cout<<"The sum of the first "<<n<<" numbers is: "<<summation(n);
    return 0;
}

/*
The workings of the program is as follow:

Let n be 4

1. The main() function calls summation(4)
2. The summation(4) function calls summation(3)
3. The summation(3) function calls summation(2)
4. The summation(2) function calls summation(1)
5. The summation(1) function calls summation(0)
6. The summation(0) function returns 0
7. The summation(1) function returns n+prevSum as 1 + 0 = 1
8. The summation(2) function returns 2 + 1 = 3
9. The summation(3) function returns 3 + 3 = 6
10. The summation(4) function returns 4 + 6 = 10
11. The main() function gives output of 10
*/