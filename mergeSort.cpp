#include<iostream>
#include<vector>

using namespace std;

void merge(vector<int> &nums, int start, int middle, int end){
    vector<int> left(nums.begin()+start, nums.begin()+middle+1);
    vector<int> right(nums.begin()+middle+1, nums.begin()+end+1);
    int indexLeft = 0;
    int indexRight = 0;
    for(int i=start; i<=end; i++){
        if(indexLeft==left.size()){
            nums[i] = right[indexRight];
            indexRight++;
        }else if(indexRight==right.size()){
            nums[i] = left[indexLeft];
            indexLeft++;
        }else if(left[indexLeft]<right[indexRight]){
            nums[i] = left[indexLeft];
            indexLeft++;
        }else{
            nums[i] = right[indexRight];
            indexRight++;
        }
    }
}

void mergeSort(vector<int> &nums, int start, int end){
    if(start==end)
        return;
    int middle = (start+end)/2;
    mergeSort(nums, start, middle);
    mergeSort(nums, middle+1, end);
    merge(nums, start, middle, end);
}

int main(){
    vector<int> nums = {6, 5, 1, 3, 4, 9, 8, 7, 2, 0, 6, 5, 10, 99, -20, 34};
    mergeSort(nums, 0, nums.size()-1);
    for(auto num: nums)
        cout<<num<<' ';
    cout<<endl;
    return 0;
}