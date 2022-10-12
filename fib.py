#!/usr/bin/env python

import sys
import wasm3


def init_runtime():
    env = wasm3.Environment()
    wasm_file = open("target/wasm32-unknown-unknown/release/fib_rs.wasm", "rb")
    wasm = wasm_file.read()
    mod = env.parse_module(wasm)
    rt = env.new_runtime(2048)
    rt.load(mod)
    return rt


if __name__ == "__main__":
    value = int(sys.argv[1])
    rt = init_runtime()
    fib = rt.find_function("fib")
    print(fib(value))
