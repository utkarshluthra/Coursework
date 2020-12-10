// To find the first and last occurance of a number in an array

#include<iostream>
using namespace std;

//n is the size of the array, i is the position of the variable, key is the number we are trying to find
int firstocc(int arr[], int n, int i, int key){ 
    if(i==n){
        return -1;
    }
    
    if (arr[i]==key){
        return i;
    }
    return firstocc(arr, n, i+1, key);
}

int lastocc(int arr, int n, int i, int key){
    int restArray = lastocc(arr, n, i+1, key);
    if(restArray!=1){
        return restArray;
    }
    if(arr[i]==key){
        return i;
    }
    return -1;
}

int main(){
    int key;
    cout<<"ENter the number you want to find";
    cin>>key;
    int arr[7]={4,2,1,2,5,2,7};
    cout<<"The first occurance of "<<key<<" is "<<firstocc(arr,7,0,key)<<endl;
    cout<<"The last occurance of "<<key<<" is "<<firstocc(arr,7,0,key)<<endl;

    return 0;
}