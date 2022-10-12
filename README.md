# Fibonacci in WebAssembly

## Build

```
$ cargo build --target wasm32-unknown-unknown --release
```

## Optimize

```
$ wasm-gc target/wasm32-unknown-unknown/release/fib_rs.wasm
```

`wasm-opt` may be useful for optimization as well.

## Run

### Python (pywasm3)

```
$ ./fib.py 24
```

### Python (wasmtime.loader)

```
$ cd target/wasm32-unknown-unknown/release

$ ipython
>>> import wasmtime.loader
>>> import fib_rs
>>> fib_rs.fib(24)
```

### Wasmtime

```
$ wasmtime target/wasm32-unknown-unknown/release/fib_rs.wasm --invoke fib 24 
```

### Wasm3

```
$ wasm3 --func fib target/wasm32-unknown-unknown/release/fib_rs.wasm 24
```

## Links

- https://depth-first.com/articles/2020/06/29/compiling-rust-to-webassembly-a-simple-example/
- https://github.com/wasm3/pywasm3
- https://github.com/wasm3/wasm3
- https://github.com/vshymanskyy/awesome-wasm-tools
- https://www.sobyte.net/post/2022-04/rust-plugin-with-webassembly/

