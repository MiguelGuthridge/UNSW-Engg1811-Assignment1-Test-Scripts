"""
Author: Miguel Guthridge

This script automates testing for calculate_similarity_list using a JSON file containing test cases.
Modify the JSON to add more test cases if you want. Enjoy!

"""

# Tests to run. Either "ALL" for all tests, or a list of test numbers for only certain tests
RUN = "ALL"

import calculate_similarity_list as csl
import json

PASS = 1
FAIL = 0
CRASH = -1

class test_case:

    def __init__(self, test_type, input_data_series, input_pattern, expected_output):
        self.test_type = test_type
        self.data_series = input_data_series
        self.pattern = input_pattern
        self.expected_output = expected_output
    
    # Runs function and collects results
    def run(self, test_num):
        print("-------------------------------------------------")
        print("Running test " + str(test_num) + ": " + self.test_type)
        print("")

        # Run the function
        try:
            result = csl.calculate_similarity_list(self.data_series, self.pattern)
        except Exception as error:
            print("Test failed to complete due to exception:")
            print(error)
            return CRASH # Test failed
        
        TOL = 0.00001
        is_correct = True
        for i in range(0, len(self.expected_output)):
            if isinstance(result[i], str) :
                    is_correct = False        
            elif  abs(result[i] - self.expected_output[i]) > TOL:
                    is_correct = False

        if is_correct:
            print("Test generated correct results")
            return PASS # Test passed
        else:
            print("Test generated incorrect results:")
            print("Input data_series:   ", self.data_series)
            print("Input pattern: ", self.pattern)
            print("")
            print("Expected result:     ", self.expected_output)
            print("Actual result:       ", result)
            return FAIL # Test failed

print("-------------------------------------------------")
print("Calculate Similairty List Tester")
print("Author: Miguel Guthridge")
print("-------------------------------------------------")
print("")

# Load all tests from JSON file
print("Loading test data...")
test_file = open("json calculate_similarity_list.json")
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
        trials.append( test_case( case["test_type"], case["data_series"], case["pattern"], case["expected_output"] ) )
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
