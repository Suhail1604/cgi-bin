#!/usr/bin/python3

import subprocess
import cgi

print("content-type: text/html")
print()

form = cgi.FieldStorage();
cmd = form.getvalue("c");

if "date" in cmd:
        output = subprocess.getoutput("date");
        print(output);
elif "cal" in cmd:
        output = subprocess.getoutput("cal");
        print(output);
elif "ls -l" in cmd:
    output = subprocess.getoutput("ls -l");
    print(output);
elif "pwd" in cmd:
    output = subprocess.getoutput("pwd");
    print(output);

else:
        print("i m coming");
