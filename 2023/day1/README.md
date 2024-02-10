# 2023 AOC Day 1

Some how I discovered the *advent of code* programming platform and I really liked the atmosphere and the storry telling quality of it.

So I thought why not giving it a try and writing a blog about my problem solving journey.

## 2023 - Day 1 - Part 1

We’ll start with the part 1 of the day 1 challange, ***Trebuchet?!***

The out of story context goal is to get the first and last digit from each line of the input, then calculate the sum of them together.

For example:

```
1abc2 => 12
pqr3stu8vwx => 38
a1b2c3d4e5f => 15
treb7uchet => 77
```

This produces *142,* because `12 + 38 + 15 + 77 = 142` *smart!*

Let’s code it now.

We’ll create a part1 function that takes a string input (input.txt text string), then iterate through it line by line, converts each line into a vector of digits to help us calculate the total. We’ll then use .chars() to iterate through each character in the line, then use `.filter_map()` to filter out non-digit characters and convert the remaining characters into a digit. We’ll then use `.map()` to convert the digit into an i32 and collect the results into a vector of i32s then we'll call the `.collect()` method to collect the results into a vector of i32s.

```rust
fn part1(input: &str) -> i32 {
    let mut total = 0;

    for line in input.split('\n') {
        let nums: Vec<i32> = line
            .chars()
            .filter_map(|c| c.to_digit(10))
            .map(|digit| digit as i32)
            .collect();
        total += nums[0] * 10 + nums[nums.len() - 1];
    }

    total
}

fn main() {
    let puzzle = fs::read_to_string("input.txt").expect("Something went wrong reading the file");
    println!("Part 1: {}", part1(&puzzle));
}
```

This should give us a vector of digits for each line, that we can then use to calculate the total by multiplying the first and last digits of each line and adding the result to the total.

Let's move on to part 2 now.

Part 2 is partially similar to part 1 but more complex. We need to also get the spelled out numbers and convert them to digits.

For example:

```
two1nine => 29
eightwothree => 83
abcone2threexyz => 13
xtwone3four => 24
4nineeightseven2 => 42
zoneight234 => 14
7pqrstsixteen => 76
```

This produces *281,* because `29 + 83 + 13 + 24 + 42 + 14 + 76 = 281`

Let's again code the part 2 now.

```rust
fn part2(input: &str) -> i32 {
        let nums = [
            ("1", 1),
            ("2", 2),
            ("3", 3),
            ("4", 4),
            ("5", 5),
            ("6", 6),
            ("7", 7),
            ("8", 8),
            ("9", 9),
            ("one", 1),
            ("two", 2),
            ("three", 3),
            ("four", 4),
            ("five", 5),
            ("six", 6),
            ("seven", 7),
            ("eight", 8),
            ("nine", 9),
        ]; 

    let mut total = 0;

    for line in input.lines() {
        let mut forwards = line;
        let mut backwards = line;

        let first = 'refe: loop {
            for (pointer, num) in nums.iter() {
                if forwards.starts_with(pointer) {
                    break 'refe num;
                }
            }
            forwards = &forwards[1..];
        };

        let last = 'refe: loop {
            for (suffix, num) in nums.iter() {
                if backwards.ends_with(suffix) {
                    break 'refe num;
                }
            }
            backwards = &backwards[..backwards.len() - 1];
        };

        let num = first * 10 + last;
        total += num;
    }
    total
}
```

The idea is to iterate through the input line by line, then iterate through the `nums` which is a tuple array of spelled out numbers and their corresponding digits. We'll define a `forwards` and `backwards` variable to help us iterate through the line from the start and end. We'll then use a infinite labeled loop for the fist digit to iterate through the `nums` array and check if the line starts with the spelled out number, then break the loop and return the digit if it does.

If it doesn't, we'll remove the first character to get stuck in an infinite loop. We'll then do the same for the last digit.

This should give us the first and last digits of each line spelled out and non-spelled out, then we can calculate the total by multiplying the first and last digits of each line and adding the result to the total.

Thank you for reading and see you in the next blog post.