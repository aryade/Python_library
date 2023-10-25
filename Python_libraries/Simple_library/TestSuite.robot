*** Settings ***
Library    calculate.py

*** Test Cases ***
Perform Calculations
    ${result}    Calculate    1 + 2
    Should Be Equal As Numbers    ${result}    3
    ${result}    Calculate    10 * 5
    Should Be Equal As Numbers    ${result}    50
    ${result}    Calculate    8 / 4
    Should Be Equal As Numbers    ${result}    2
    ${result}    Calculate    2 - 1
    Should Be Equal As Numbers    ${result}    1