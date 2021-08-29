# effectiveShellShocker
This is a Python script that tests for http shellshocker vulnerability. If it exists, it allows you to run commands remotely.

Simple Usage:
```bash
python3 effectiveShellShocker.py -h
```
![Help](Images/help.png)

```bash
python3 effectiveShellShocker.py test http://172.16.80.22 /cgi-bin /calendar.cgi
```
![Test](Images/test.png)

```bash
python3 effectiveShellShocker.py attack http://172.16.80.22 /cgi-bin /calendar.cgi
```
![Attack](Images/attack.png)

Reverse shell:
![Reverse Shell](Images/reverseshell.png)

Thank you
