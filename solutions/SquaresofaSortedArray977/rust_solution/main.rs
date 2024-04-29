pub struct Solution;

impl Solution {
    pub fn sorted_squares(nums: Vec<i32>) -> Vec<i32> {
        if nums.is_empty() {
            return vec![];
        }

        let n = nums.len();
        let (mut i, mut j, mut k) = (0, n - 1, n);
        let mut res = vec![0;n];
        while i <= j {
            if nums[i] * nums[i] > nums[j] * nums[j] {
                res[k-1] = nums[i] * nums[i];
                i += 1;
            } else {
                res[k-1] = nums[j] * nums[j];
                j -= 1;
            }
            k -= 1;
        }
        res
    }
}

fn main() {
    let nums = vec![-4,-1,0,3,10];
    let res = Solution::sorted_squares(nums);
    println!("Result: {:?}", res);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sorted_squares() {
        assert_eq!(Solution::sorted_squares(vec![-4,-1,0,3,10]), vec![0,1,9,16,100]);
        assert_eq!(Solution::sorted_squares(vec![-7,-3,2,3,11]), vec![4,9,9,49,121]);
        assert_eq!(Solution::sorted_squares(vec![]), vec![]);
    }
}