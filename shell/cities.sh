# code written by Timo Kats 
#!/bin/bash

tail -7 'data.csv' | cut -d ',' -f 4 | sort | uniq -c
