# Hidden XML
> Write-up author: vreshco
## DESCRIPTION:
vreshco hiding the flag somewhere, can you find it?
## HINT:
- NONE
## STEPS:
1. I made this challenge, so i share the solver for this challenge.
2. Crack the zip file using **fcrackzip**, then open every directories and decode it manually using this script.

```py
from dicttoxml import dicttoxml
import xmltodict
import xml
import random
def toflag():
    mydict = xmltodict.parse(open("output.xml").read())['root']
    tmp = {}
    for i in mydict:
        tmp[int(i.replace('n', ''))] = mydict[i]
    for i in range(len(tmp)):
        print(tmp[i]['#text'], end='')
toflag()
```

3. Well the flag is at the 4th directory, decode the xml file shall resulting to base64 text.
4. Decode the base64 and got the flag.

## FLAG

```
TCP1P{somewhat_special_chiper_whith_xml}
```
