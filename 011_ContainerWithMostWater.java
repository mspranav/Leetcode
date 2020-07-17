import java.util.*;

// I have included only the method/function

public int maxArea(int[] height) {
    // maxarea, l = 0, 0
    // r = len(height) - 1
    // while(l < r):
    //     maxarea = max(maxarea, min(height[l],height[r]) * (r-l))
    //     if(height[l] < height[r]):
    //         l+=1
    //     else:
    //         r-=1
    // return maxarea
    
    int maxarea = 0;
    int l = 0;
    int r = height.length - 1 ;
    while(l < r){
        maxarea = Math.max(maxarea, Math.min(height[l],height[r]) * (r-l));
        if(height[l] < height[r]){
            l++;
        }       
        else{
            r--;
        }
        
    }
    
    return maxarea;
}
