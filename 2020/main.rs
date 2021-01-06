// Rust skeleton provided by Discord user Tim#3509 (213389120829915136)

// --------------------------------------------------
// Check all files are in LF format before running
// --------------------------------------------------

use std::collections::HashMap;
use std::fs;

// Section A (35 Points)

fn chain(grid: Vec<Vec<char>>) -> bool {
    return true;
}

fn tic_tac_toe(grid: Vec<Vec<char>>) -> bool {
    return true;
}

// Section B (65 Points)

fn max_chain(grid: Vec<Vec<char>>) -> i32 {
    return 0;
}

fn tic_tac_no(n: i32) -> i32 {
    return 0;
}

fn chain_blocker(n: i32, k: i32) -> Vec<Vec<char>> {
    return vec![vec!['B', 'U'], vec!['B', 'U']];
}

// --------------------------------------------------
// You don't need to modify anything below this line
// --------------------------------------------------

fn grid_input<T>(letter: &str, func: fn(Vec<Vec<char>>) -> T) -> std::vec::Vec<T> {
    let file_str =
        fs::read_to_string(format!("inputs/input_{}.txt", letter)).expect("Unable to read file");
    let blocks = file_str.split("\n\n");

    let mut outputs: Vec<T> = Vec::new();
    println!("------ Challenge {} ------", letter.to_uppercase());
    for block in blocks {
        let mut grid: Vec<Vec<char>> = Vec::new();
        for row in block.split("\n") {
            grid.push(row.chars().collect());
        }
        outputs.push(func(grid));
    }

    return outputs;
}

fn integer_input<T>(letter: &str, func: fn(i32) -> T) -> std::vec::Vec<T> {
    let file_str =
        fs::read_to_string(format!("inputs/input_{}.txt", letter)).expect("Unable to read file");
    let lines = file_str.split("\n");
    println!("------ Challenge {} ------", letter.to_uppercase());
    let outputs = lines.map(|x| func(x.parse::<i32>().unwrap())).collect();
    return outputs;
}

fn two_integer_input<T>(letter: &str, func: fn(i32, i32) -> T) -> std::vec::Vec<T> {
    let file_str =
        fs::read_to_string(format!("inputs/input_{}.txt", letter)).expect("Unable to read file");
    let lines = file_str.split("\n");

    let mut outputs: Vec<T> = Vec::new();
    println!("------ Challenge {} ------", letter.to_uppercase());
    for line in lines {
        let split_line = line.split(" ").collect::<Vec<_>>();
        let n1 = split_line[0].parse::<i32>().unwrap();
        let n2 = split_line[1].parse::<i32>().unwrap();

        outputs.push(func(n1, n2));
    }
    return outputs;
}

fn boolean_output(letter: &str, outputs: Vec<bool>) {
    let write_str = outputs
        .iter()
        .map(|x| match x {
            true => "T",
            false => "F",
        })
        .collect::<Vec<_>>()
        .join("\n");
    fs::write(format!("outputs/{}.txt", letter), write_str).expect("Error writing to file");
}

fn integer_output(letter: &str, outputs: Vec<i32>) {
    let write_str = outputs
        .iter()
        .map(|x| x.to_string())
        .collect::<Vec<_>>()
        .join("\n");
    fs::write(format!("outputs/{}.txt", letter), write_str).expect("Error writing to file");
}

fn grid_output(letter: &str, grids: Vec<Vec<Vec<char>>>) {
    let mut write_str = String::new();

    for grid in grids.iter() {
        write_str.push_str(
            &grid
                .iter()
                .map(|x| x.iter().collect())
                .collect::<Vec<String>>()
                .join("\n"),
        );
        write_str.push_str("\n\n");
    }

    fs::write(format!("outputs/{}.txt", letter), write_str).expect("Error writing to file");
}

fn part_a1() {
    let outputs = grid_input("a1", chain);
    boolean_output("a1", outputs);
}

fn part_a2() {
    let outputs = grid_input("a2", tic_tac_toe);
    boolean_output("a2", outputs);
}

fn part_b1() {
    let outputs = grid_input("b1", max_chain);
    integer_output("b1", outputs);
}

fn part_b2() {
    let outputs = integer_input("b2", tic_tac_no);
    integer_output("b2", outputs);
}

fn part_b3() {
    let outputs = two_integer_input("b3", chain_blocker);
    grid_output("b3", outputs);
}

fn main() {
    part_a1();
    part_a2();
    part_b1();
    part_b2();
    part_b3();
}
