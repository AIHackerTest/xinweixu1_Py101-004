## Input and Output Files
### Reading and Writing Files
  * `f = open('workfile', 'w')`: `open` returns a *file object*, and it takes two arguments, `open(filename, mode)`, whre the mode argument is optional and can takes four options
    * `'r'` = read only (the default)
    * `'w'` = write only(an existing file with the same name will be erased!);
    * `'a'` = open the file for appending (any data written will be added to the end);
    * `'r+'` = opens the file for both reading and writing
    * `'b'` = open the file in *binray mode* (e.g., `JPEG` or `EXE`, see "encoding" for more info), which can be appended to any of the four options mentiond, for example `f = open('workfile', 'rb+')`
  * use the `with` keyword, and the advantage is that the file will be properly closed after, and it's shorter than writing equivalent `try-finally` blocks
  `with open('workfile') as f:
         read_data = f.read()`
  * `f.readline()` reads a single line from the file
  * to read a few lines from a file, loop over the file object (which is memory efficient, fast, and leads to simple code!):
  `for line in f:
      print (line, end='')`
  * to read all the lines in a file, use `list(f)` or `f.readlines()`
  * to write *strings* into a file, use `f.write(string)`, and other types of objects need to be converted either to a string (in text mode) or a bytes object (in binary mode) before writing them
  

### Encoding and Decoding Files
