use std::cmp::Ordering;

pub struct Solution;

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let (mut left, mut right) = (0, nums.len() as i32 - 1);
        while left <= right {
            let mid = left + (right - left) / 2;
            match nums[mid as usize].cmp(&target) {
                Ordering::Less => left = mid + 1,
                Ordering::Greater => right = mid - 1,
                Ordering::Equal => return mid,     
            }
        }
        -1
    }
}

fn main() {
    let result = Solution::search(vec![-1, 0, 3, 5, 9, 12], 9);
    println!("The index of the target is: {}", result);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_search() {
        assert_eq!(Solution::search(vec![1, 2, 3, 4, 5], 3), 2);
        assert_eq!(Solution::search(vec![1, 2, 3, 4, 5], 6), -1);
        assert_eq!(Solution::search(vec![], 1), -1);
    }
}