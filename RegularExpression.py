#Regular Expression:

import re
line = "Hello, my name is SBiswas"
a = re.findall("SBiswas$",line)

if a:
    print("yes, It's exist")
else:
    print("No")