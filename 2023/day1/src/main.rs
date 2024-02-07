use std::fs;

fn part1(input: &str) -> i32 {
    let mut total = 0;
    for line in input.lines() {
        let mut first = 0;
        let mut last = 0;
        for c in line.chars() {
            if c.is_digit(10) {
                if first == 0 {
                    first = c.to_digit(10).unwrap();
                }
                last = c.to_digit(10).unwrap();
            }
        }
        let sum: i32 = (first * 10 + last) as i32;
        total += sum;
    }
    total
}

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

fn main() {
    let puzzle = fs::read_to_string("input.txt").expect("Something went wrong reading the file");

    println!("Part 1: {}", part1(&puzzle));
    println!("Part 2: {}", part2(&puzzle));
}
