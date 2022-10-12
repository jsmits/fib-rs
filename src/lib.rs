#[no_mangle]
pub extern "C" fn fib(x: i64) -> i64 {
    if x < 2 {
        return x;
    }
    fib(x - 2) + fib(x - 1)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = fib(9);
        assert_eq!(result, 34);
    }
}
