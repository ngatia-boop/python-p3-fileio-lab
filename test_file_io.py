import os
import pytest
from file_io import write_file, append_file, read_file  # Import your functions

@pytest.fixture(scope='module', autouse=True)
def setup_temp_dir():
       """Create a temporary directory for tests."""
       temp_dir = '/tmp/test_dir'
       os.makedirs(temp_dir, exist_ok=True)
       yield temp_dir
       # Cleanup after tests
       for filename in os.listdir(temp_dir):
           file_path = os.path.join(temp_dir, filename)
           os.remove(file_path)
       os.rmdir(temp_dir)

def test_write_file(setup_temp_dir):
       """Test writing to a file."""
       test_file = os.path.join(setup_temp_dir, 'test_file.txt')
       write_file(test_file, 'Hello, World!')
       assert os.path.exists(test_file)

def test_append_file(setup_temp_dir):
       """Test appending to a file."""
       test_file = os.path.join(setup_temp_dir, 'test_file.txt')
       append_file(test_file, 'Appending text.')
       with open(test_file, 'r') as f:
           content = f.read()
       assert 'Appending text.' in content
   