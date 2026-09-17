# Calculator Project

A simple Python calculator with automated CI testing.

## CI Status

![Python CI](https://github.com/fahmidabhuiyanproma/github-CI/actions/workflows/ci.yml/badge.svg)

## How to Run Tests

```bash
pip install pytest
pytest test_calculator.py -v
```
## Functions

- `add(a, b)` — adds two numbers
- `subtract(a, b)` — subtracts b from a
- `multiply(a, b)` — multiplies two numbers
- `divide(a, b)` — divides a by b (raises error if b is zero)