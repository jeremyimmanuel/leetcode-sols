#include <iostream>

#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {};
};

bool isPalindrome(ListNode* head) {
    ListNode* curr = head;
    
    vector<int> arr = vector<int>();
    while (curr != nullptr) {
        arr.push_back(curr->val);
        curr = curr->next;
    }

    int front, back;
    front = 0;
    back = arr.size() - 1;
    while(front < back) {
        if(arr[front] != arr[back])
            return false;
        front++;
        back--;
    }

    return true;
}

int main(){
    return 0;
}


