// To create a program to find the nth fibonacci number without using Dynamic Programming methods

#include<iostream>
using namespace std;

int fib(int n){
    if(n<=1){
        return 1;
    }
    if(n==0){
        return 0;
    }
    int prevfib= fib(n-1)+fib(n-2);
    return n + prevfib;

}


int main(){
    int n;
    cout<<"Enter the value of index in fibonacci sequence"<<endl;
    cin>>n;
    cout<<"The number at the "<<n<<"th position in the fibonacci sequence is: "<<fib(n)<<endl;

    return 0;
}

/*

The working of the above program is as follows:

1. main() calls fib(7)
2. fib(7) calls fib(6)
3. fib(6) calls fib(5)
4. fib(5) calls fib(4)
5. fib(4) calls fib(3)
6. fib(3) calls fib(2)
7. fib(2) calls fib(1)
8. fib(1) returns 1
9. fib(2) returns 0+1=1
9. fib(3) returns 1+1=2
9. fib(4) returns 2+1=3
9. fib(5) returns 3+2=5
9. fib(6) returns 5+3=8
9. fib(7) returns 8+5=13
10. main() returns the output as 13


*/