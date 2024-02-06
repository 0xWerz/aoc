use std::fs;

fn main() {
    let file_name = "input.txt";
    println!("Reading from file {}", file_name);
    let content = fs::read_to_string(file_name).expect("Something went wrong reading the file");
    let mut total = 0;
    for (i, line) in content.lines().enumerate() {
        let mut first = 0;
        let mut last = 0;
        for (j, c) in line.chars().enumerate() {
            if c.is_digit(10) {
                if first == 0 {
                    first = c.to_digit(10).unwrap();
                }
                last = c.to_digit(10).unwrap();
            }
        }
        let sum: i32 = format!("{}{}", first, last).parse().unwrap();
        total += sum;
        println!("Line {}: {} + {} = {}", i, first, last, sum);
    }
    println!("Total: {}", total);
}
