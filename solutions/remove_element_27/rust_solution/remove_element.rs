impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut slowIdx = 0;
        for pos in (0..nums.len()) {
            if nums[pos] != val {
                nums[slowIdx] = nums[pos];
                slowIdx += 1;
            }
        }
        return slowIdx as i32;
    }
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