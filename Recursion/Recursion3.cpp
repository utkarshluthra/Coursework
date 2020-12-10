/*
To create a program to find the factorial of a number n
*/

#include<iostream>
using namespace std;

int fact(int n){
    if(n==1){
        return 1;
    }
    int prevFact = fact(n-1);
    return n * prevFact;
}

int main(){
    int n;
    cout<<"Enter the value of n in n!: ";
    cin>>n;
    cout<<fact(n);
     return 0;
}


/*

The working of the program is as follows:

Let n be 5

1. main() function calls fact(5)
2. fact(5) calls fact(4)
3. fact(4) calls fact(3)
4. fact(3) calls fact(2)
5. fact(2) calls fact(1)
6. fact(1) returns the value 1
7. fact(2) returns 2 from prevfact (2 * 1 = 2)
8. fact(3) returns 6 from prevfact (3 * 2 = 6)
9. fact(4) returns 6 from prevfact (4 * 6 = 24)
10. fact(5) returns 6 from prevfact (5 * 24 = 120)
11. main() returns the output as 120


*/