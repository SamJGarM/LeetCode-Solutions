/**
Author: Samuel Jaden García Muñoz
Date: 30/04/2026
Revised: 
Note:-

**/

/**
 * @param {number[]} nums
 * @return {boolean}
 */

var containsDuplicate = function(nums) {
    return nums.length !== new Set(nums).size;
};

/**
Time Complexity: O(n)
Space Complexity: O(n)
**/