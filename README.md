# TDD Python 

## Install all requirements
~~~~~ 
 pip3 install -r requirements_dev.txt
~~~~~ 
 
## Building artifact 
Togenerate a source OR binary artifact from source code, you can use, which then you can upload it to PyPI(Python Package Index,
 similar to maven repo) by registerin in PyPI: 
~~~~~
 binary: 
 python3 setup.py sdist bdist bdist_wheel
~~~~~
## Testing
Python test/test-runner frameworks analysis and usage that was studied for this project: 
* built-in unittest framework
* pytest framework
* nosetest runner

###### Run tests using unittest built-in framework
~~~~~
python3 -m unittest
OR for individual files and verbose 
python3 -m unittest -v  tests/calculator/calculator_tests.py tests/helloworld/helloworld_tests.py 
~~~~~

###### Run tests using pytest framework (***** use this framework!)
~~~~~
look at pytest.ini for configuration
pytest 
OR for individual files and verbose 
python3 -m pytest -v tests/calculator/calculator_tests.py tests/helloworld/helloworld_tests.py   
~~~~~

###### Run tests with nosetest runner with coverage
Nose is not being actively supported. We shouldn't use this. 
~~~~~
 nosetests  -v tests --with-coverage
~~~~~
