from io import StringIO
import sys

def test_question():
    original_stdout = sys.stdout

    try:
        sys.stdout = StringIO()
        
        try:
            from . import q2  # should automatically run as no functions yet
        except Exception as e:
            raise AssertionError(f"Error when running the code: {e}")
            exit()
        
        output = sys.stdout.getvalue().strip().split('\n')
        
        if len(output) == 0:
            raise AssertionError("No output detected. Did you forget to print the result?")

        # Check if the output matches the expected format
        assert len(output) == 1, "Output should be a single line."
        expected_start = "Name: Alice Smith, Age: 30, Height: 5.7"
        assert output[0] == expected_start, f"Output should be '{expected_start}' but got '{output[0]}'."

    finally:
        sys.stdout = original_stdout
        
if __name__ == "__main__":
    test_question()
    print("All tests passed!")