#!/usr/bin/env python3
from subprocess import check_output

from StorCLIParser import StorCLIParser

# output = check_output(["/opt/MegaRAID/storcli/storcli64", "/c0", "show all"]).decode("utf-8")


# #Create the controller dict
# d = s.ctrl_info_dict(output)

# #Loop through all keys and get their values
# for key in d:
# 	print(key, '->', d[key])


# #Lookup a value with single key
# print("\n")
# print(d['Serial Number'])


# output = check_output(["/opt/MegaRAID/storcli/storcli64", "/c0/e252/s1", "show", "all"]).decode("utf-8")

# #print(output)
# s = StorCLIParser()
# #Create the controller dict
# p = s.pd_info_dict(output)
# #print(p)
# #Loop through all keys and get their values
# for key in p:
# 	print(key, '->', p[key])


s = StorCLIParser()

print(s.generate_storcli_json())