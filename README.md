# usergen
Create a range of possible usernames from peoples names

```
usage: usergen.py [-h] [-n NAMES] [-o OUTFILE]

A small program to generate a list of usernames from names

optional arguments:
  -h, --help            show this help message and exit
  -n NAMES, --names NAMES
                        a file containing a list os peoples names
  -o OUTFILE, --outfile OUTFILE
                        File name to save output

```

USAGE:

Create a file with a list of firstname lastname:
```
joe bloggs
jane doe
```

EXAMPLE: python3 usergen.py -n testnames.txt

OUTPUT:
```
joebloggs
joe.bloggs
joebloggs
jbloggs
bloggsj
janedoe
jane.doe
janedoe
jdoe
doej
```


