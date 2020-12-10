// To check if an array is sorted or not (strictly increasing)

#include<iostream>
using namespace std;

bool sorted(int arr[], int n){ //n is the size of the array
    if(n==1){
        return true;
    }
    bool restArray = sorted(arr+1, n-1); //arr+1 means that the pointer is set to the index 1, i.e, the second element of the array
    if (arr[0]<arr[1] && restArray){
        return true;
    }
}

int main(){
    int arr1[5]={1,2,3,4,5};
    int arr2[5]={1,3,2,4,5};

    cout<<"Array 1 is sorted? "<<sorted(arr1, 5)<<endl;
    cout<<"Array 2 is sorted? "<<sorted(arr2, 5)<<endl;
    return 0;
}

/*

Working of the given program is as follows:

For the array {1,2,3,4,5}, we only check if the first two elements are sorted. The rest are checked via recursion.

{1,(2,3,4,5)} --> 1 < 2 --> Hence True
   {2,(3,4,5)} --> 2 < 3 --> Hence True
      {3,(4,5)} --> 3 < 4 --> Hence True
         {4,5} --> 4 < 5 --> Hence True

Finally: 1 AND 1 AND 1 AND 1 AND 1 = 1 (True)

For the array {1,3,2,4,5}, we only check if the first two elements are sorted. The rest are checked via recursion.

{1,(3,2,4,5)} --> 1 < 3 --> Hence True
   {3,(2,4,5)} --> 3 !< 2 --> Hence False --> Therefore the restArray variable becomes 0 (false)

Finally: 1 AND 0 = 0 (False)
*/