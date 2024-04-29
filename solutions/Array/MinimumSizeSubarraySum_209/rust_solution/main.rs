pub struct Solution;

impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        let mut min_len = nums.len() + 1;
        let (mut left, mut right) = (0, 0);
        let mut sum = 0;
        while right < nums.len() {
            sum += nums[right];
            while sum >= target {
                min_len = std::cmp::min(min_len, right - left + 1);
                sum -= nums[left];
                left += 1;
            }
            right += 1;
        }
        if min_len == nums.len() + 1 {
            0
        } else {
            min_len as i32
        }
    }
}

fn main() {
    let target = 7;
    let nums = vec![2, 3, 1, 2, 4, 3];
    let result = Solution::min_sub_array_len(target, nums);
    println!("{}", result);
}
