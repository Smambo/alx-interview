## Log Parsing
### Task:
### [0. Log parsing](./0-stats.py)
Write a script that reads `stdin` line by line and computes metrics:

* Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (if the format is not this one, the line must be skipped)
* After every 10 lines and/or a keyboard interruption (`CTRL + C`), print these statistics from the beginning:
  * Total file size: `File size: <total size>`
  * where `<total size>` is the sum of all previous `<file size>` (see input format above)
  * Number of lines by status code:
    * possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500`
    * if a status code doesn’t appear or is not an integer, don’t print anything for this status code
    * format: `<status code>: <number>`
    * status codes should be printed in ascending order
<b>Warning:</b> In this sample, you will have random value - it’s normal to not have the same output as this one.<br>

```
simam@DESKTOP-5QTVNRV:~/alx-interview/0x03-log_parsing$ ./0-generator.py | ./0-stats.py
File size: 5485
200: 2
301: 1
400: 1
403: 1
404: 2
405: 2
500: 1
File size: 9970
200: 4
301: 2
400: 6
403: 1
404: 2
405: 3
500: 2
File size: 15572
200: 6
301: 4
400: 9
403: 2
404: 3
405: 4
500: 2
^CFile size: 18926
Traceback (most recent call last):
  File "/home/simam/alx-interview/0x03-log_parsing/./0-generator.py", line 8, in <module>
200: 6
301: 5
400: 11
403: 2
404: 4
405: 6
500: 2
    sleep(random.random())
KeyboardInterrupt

simam@DESKTOP-5QTVNRV:~/alx-interview/0x03-log_parsing$
```
