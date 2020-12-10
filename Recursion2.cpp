/*
To create a program which finds the pth power of a number n
*/

#include<iostream>
using namespace std;

int pow(int a, int b){ //a to the power b (a^b)
    if(b==0){
        return 1;
    }
    int prevPow = pow(a, b-1);
    return a*prevPow;

}

int main(){
    int n, p;
    cout<<"Enter the value of n and p (as n^p)";
    cin>>n>>p;
    cout<<"The answer is: "<<pow(n,p)<<endl;
    return 0;
}

/*

The working of the program is as follows:

Let n be 4 and p be 3 for n^p:

1. main() function calls pow(4,3)
2. pow(4,2) function calls pow(4,1)
3. pow(4,1) function calls pow(4,0)
4. pow(4,0) returns 1
5. pow(4,1) returns 4*1=4 to prevPow
6. pow(4,2) returns 4*4=16 to prevPow
7. pow(4,3) returns 4*16=64 to the main() function
8. main() function gives output of 64

*/