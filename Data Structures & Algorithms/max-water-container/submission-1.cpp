class Solution {
public:
    int maxArea(vector<int>& height) {
        int max_water; 
        int left;
        int right;
        max_water = 0;
        left = 0;
        right = height.size() - 1;
        while(left < right) {
            int width = right - left;
            int current_height = min(height[left] , height[right]);
            int current_water = width * current_height;
            max_water = max(max_water,current_water);
            if(height[left] < height[right]) {
                left +=1;
            }
            else{
                right -= 1;
            }
        }
        return max_water;
    }
};