# math-interpreter

Math-interpreter is a interpreter for simple mathematical expressions. It includes a lexer and a parser.

## EBNF Grammar

```ebnf
expr = term {("+" | "-") term}
term = factor {"*" | "/"} factor | factor
factor = {"+" | "-"} (number | "(" expr ")")
```

## Requirements

- Python 3

## Usage

Run the interpreter with the following command:

```bash
python math_interpreter
```

## Examples

```
>> 10 - (-15 - 2) - 3
24
>>
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
