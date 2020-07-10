# UNSW Engg1811 Assignment1 Test Scripts

This repository contains improved test scripts for Assignment 1 of Engg1811. If you create more test cases, feel free to create pull requests.

## Important Note

These scripts are improved versions of the provided testing scripts for this assignment. Although effort has been made to sure the validity of these scripts,
 no guarantees can be made of the accuracy of either the testing scripts, or the tests themselves. If you find issues, please fix them and create a pull request.

These scripts are intended to assist students with testing their own code, without providing any solutions to them.

## How to use these scripts

In order to use these scripts, do the following.

1. Extract them to your existing assignment folder.

2. Open the scripts using your IDE of choice, and run them.

In order to specify which tests to run, you can replace the variable `RUN` with a list of test numbers. For example, to run tests 0, 3, 4 and 7, you would change this to `RUN = [0, 3, 4, 7]`.
 To run all tests, set it to `RUN = "ALL"`

When run, the script outputs information about tests to the console. If a test passes, only that info is given, but if a test is failed, or your script produces an unhandled exception,
 more detailed information is printed.

In order to add or modify tests, open the JSON files corresponding to the scripts, and make edits as neccesary. It may help to be familiar with the JSON file format, but you should just be able to
 copy-paste one of the tests, provided you get the commas right (they work the same as commas in Python lists).
