"""
Author: Miguel Guthridge

This script automates testing for pattern_search_multiple using a JSON file containing test cases.
Modify the JSON to add more test cases if you want. Enjoy!

"""

# Tests to run. Either "ALL" for all tests, or a list of test numbers for only certain tests
RUN = [15]

import pattern_search_multiple as psm
import json

PASS = 1
FAIL = 0
CRASH = -1

class test_case:

    def __init__(self, test_type, input_data_series, input_pattern_width, input_threshold, expected_output):
        self.test_type = test_type
        self.data_series = input_data_series
        self.pattern_width = input_pattern_width
        self.threshold = input_threshold
        self.expected_output = expected_output
    
    # Runs function and collects results
    def run(self, test_num):
        print("-------------------------------------------------")
        print("Running test " + str(test_num) + ": " + self.test_type)
        print("")

        # Run the function
        try:
            result = psm.pattern_search_multiple(self.data_series.copy(), self.pattern_width, self.threshold)
        except Exception as error:
            print("Test failed to complete due to exception:")
            print(error)
            return CRASH # Test failed
        

        if result == self.expected_output:
            print("Test generated correct results")
            return PASS # Test passed
        else:
            print("Test generated incorrect results:")
            print("Input data_series:   ", self.data_series)
            print("Input pattern_width: ", self.pattern_width)
            print("Input threshold:     ", self.threshold)
            print("")
            print("Expected result:     ", self.expected_output)
            print("Actual result:       ", result)
            return FAIL # Test failed

print("-------------------------------------------------")
print("Pattern Search Multiple Tester")
print("Author: Miguel Guthridge")
print("-------------------------------------------------")
print("")

# Load all tests from JSON file
print("Loading test data...")
test_file = open("json pattern_search_multiple.json")
trials_data = test_file.read()
test_file.close()

# Parse JSON into accessible object
print("Parsing JSON...")
trials_object = json.loads(trials_data)
# Put each trial into list of test_case objects
trials = []
for ctr in range(len(trials_object)):
    case = trials_object[ctr]
    try:
        trials.append( test_case( case["test_type"], case["data_series"], case["pattern_width"], case["threshold"], case["expected_output"] ) )
    except:
        print("Failed to import test case " + str(ctr) + ". Is this case typed correctly?")

# Run each test, storing results
print("Running Tests...")
results = []

# Run all tests
if type(RUN) is str:
    if RUN == "ALL": 
        print("Running all tests...")
        for ctr in range(len(trials)):
            results.append( trials[ctr].run(ctr) )

# Run listed tests
elif type(RUN) is list: 
    print("Running tests: ", RUN)
    for ctr in RUN:
        results.append( trials[ctr].run(ctr) )

print("-------------------------------------------------")
print("Testing complete! Compiling results...")

# Print results summary
pass_ct, fail_ct, crash_ct = 0, 0, 0
for result in results:
    if result is PASS: 
        pass_ct += 1
    if result is FAIL: 
        fail_ct += 1
    if result is CRASH: 
        crash_ct += 1


print("-------------------------------------------------")
print("RESULTS:")
print("Passed: ", pass_ct)
print("Failed: ", fail_ct)
print("Crashed: ", crash_ct)
