from unittest import TestCase
import src.util.flatten as fl

class TestFlatten(TestCase):
    def test_flatten_data(self):
        input = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
                 'emp2': {'name': 'Kim', 'job': 'Dev'},
                 'emp3': {'name': 'Sam', 'job': 'Dev'}}
        expected_result = [{'emp1_name': 'Bob', 'emp1_job': 'Mgr'},{'emp2_name': 'Kim', 'emp2_job':'Dev'},{'emp3_name':'Sam', 'emp3_job': 'Dev'}]
        result = fl.flatten_data(input)
        assert result== expected_result

    def test_flatten_data1(self):
        input = {'emp1': {'name': 'Bob'},
                 'emp2': {'name': 'Kim', 'job': 'Dev'},
                 'emp3': {'name': 'Sam', 'job': 'Dev'}}
        expected_result = [{'emp1_name': 'Bob'},{'emp2_name': 'Kim', 'emp2_job':'Dev'},{'emp3_name':'Sam', 'emp3_job': 'Dev'}]
        result = fl.flatten_data(input)
        assert result== expected_result

    def test_flatten_data2(self):
        input = {'emp1': {},
                 'emp2': {'name': 'Kim', 'job': 'Dev'},
                 'emp3': {'name': 'Sam', 'job': 'Dev'}}
        expected_result = [{'emp2_name': 'Kim', 'emp2_job':'Dev'},{'emp3_name':'Sam', 'emp3_job': 'Dev'}]
        result = fl.flatten_data(input)
        print(result)
        assert result== expected_result

    def test_flatten_data3(self):
        input = {'emp1': {},
                 'emp2': {},
                 'emp3': {'name': 'Sam', 'job': 'Dev'}}
        expected_result = [{'emp3_name':'Sam', 'emp3_job': 'Dev'}]
        result = fl.flatten_data(input)
        print(result)
        assert result== expected_result