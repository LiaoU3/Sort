#include<iostream>
#include<vector>

using namespace std;

void quickSort(vector<int> &nums, int start, int end){
    if(start>=end) return;
    int pivot = nums[start];
    int left = start+1;
    int right = end;
    while(1){
        while(left<end && nums[left]<=pivot)left++;
        while(start<right && nums[right]>=pivot)right--;
        if(left>=right)break;
        swap(nums[left], nums[right]);
    }
    swap(nums[start], nums[right]);
    quickSort(nums, start, right-1);
    quickSort(nums, right+1, end);
}

void swap(int &a, int &b){
    int tmp;
    tmp = a;
    a = b;
    b = tmp;
}

int main(){
    vector<int> nums = {6, 5, 1, 3, 4, 9, 8, 7, 2, 0, 6, 5, 10, 99, -20, 34};
    quickSort(nums, 0, nums.size()-1);
    for(auto num: nums)
        cout<<num<<' ';
    cout<<endl;
    return 0;
}