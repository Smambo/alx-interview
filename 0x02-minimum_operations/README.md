## Minimum Operations <br>
## Task: <br>
### [0. Minimum Operations](./0-minoperations.py) <br>
In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

* Prototype: `def minOperations(n)`
* Returns an integer
* If `n` is impossible to achieve, return `0`

<b>Example:</b>

`n = 9`

`H` => `Copy All` => `Paste` => `HH` => `Paste` => `HHH` => `Copy All` => `Paste` => `HHHHHH` => `Paste` => `HHHHHHHHH`

Number of operations: `6`

```
simam@DESKTOP-5QTVNRV:~/alx-interview/0x02-minimum_operations$ ./0-main.py
Min # of operations to reach 4 char: 4
Min # of operations to reach 12 char: 7
simam@DESKTOP-5QTVNRV:~/alx-interview/0x02-minimum_operations$
```
