import random

syntax = "XXXYY-OEM-00SSSSS-ZZZZZ"

def doNothing():
    pass

x = str(random.randint(1, 366))
if len(x) == 1:
    x = "00" + x
elif len(x) == 2:
    x = "0" + x

y = str(random.randint(95, 103))
if len(y) == 2:
    y = "0" + y
y = y[-2:]

dash = "-"
oem = "OEM"

zeros = "00"
s = str(random.randint(0, 99999))
while int(s) % 7 != 0:
    s = str(random.randint(0, 99999))

z = str(random.randint(0, 99999))
if len(z) == 1:
    z = "0000" + z
elif len(z) == 2:
    z = "000" + z
elif len(z) == 3:
    z = "00" + z
elif len(z) == 4:
    z = "0" + z

result = x + y + dash + oem + dash + zeros + s + dash + z
print(result)

__import__("os").system("pause")