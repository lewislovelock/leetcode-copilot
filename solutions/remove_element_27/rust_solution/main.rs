pub struct Solution;

impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut slow_idx = 0;
        for pos in 0..nums.len() {
            if nums[pos] != val {
                nums[slow_idx] = nums[pos];
                slow_idx += 1;
            }
        }
        return slow_idx as i32;
    }
}

fn main() {
    let mut nums1 = vec![3,2,2,3];
    let res1 = Solution::remove_element(&mut nums1, 3);
    println!("Result1: {:?}", res1);

    let mut nums2 = vec![0,1,2,2,3,0,4,2];
    let res2 = Solution::remove_element(&mut nums2, 2);
    println!("Result2: {:?}", res2);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_remove_element() {
        let mut nums1 = vec![3,2,2,3];
        assert_eq!(Solution::remove_element(&mut nums1, 3), 2);

        let mut nums2 = vec![0,1,2,2,3,0,4,2];
        assert_eq!(Solution::remove_element(&mut nums2, 2), 5);
    }
}