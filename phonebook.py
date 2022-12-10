from sys import exit
people = {
    "EMMA" : "077-090-8871",
    "RODRIGO" : "078-999-2122",
    "BRIAN" : "061-661-1717",
    "DAVID" : "021-211-2212"
}

if "EMMA" in people:
    print(F"Found {people['EMMA']}")
    exit(0)
print("Not found")
exit(1)