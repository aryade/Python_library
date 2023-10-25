*** Settings ***
Library     PythonKeywords.py

*** Test Cases ***
Use Custom Keywords
    No Arguments
    One Argument    Test Argument
    Three Arguments    One    Two    Three
    One Default    
    Multiple Defaults    Argument 1    arg3=Argument 3
    My Keyword    Argument 1    Argument 2    Named Argument=One Value