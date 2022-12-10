from cs50 import get_string
import re

s = get_string ("Do you agree?\n")

#if s == "Y" or s == "y":
#if s in ["y", "Y"]:
# if s.lower() in ["y", "yes"]:
if re.search("y(es)?", s):
    print("Agreed.")

#elif s == "N" or s == "n":
#if s in ["N", "n"]:
# if s.lower() in ["n", "no"]:
if re.search("no", s):
    print("Not agreed.")