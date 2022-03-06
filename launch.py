import imp


import main as m


### This will just launch the program and catch any excepts
try:
    print("launching...")
    m.runmain()
except Exception as e:
    print("DURING EXECUTION, THE FOLLOWING ERROR HAS OCCURED:")
    print(e)