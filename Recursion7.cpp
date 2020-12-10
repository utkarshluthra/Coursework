// To print numbers in decreasing order from n to 0

#include<iostream>
using namespace std;

int dec(int n){
    if(n==0){
        return 0;
    }

    cout<<n<<endl;    
    dec(n-1);
}

int main(){
    int n;
    cin>>n;
    cout<<dec(n);
    return 0;
}