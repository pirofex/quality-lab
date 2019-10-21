# Quality Lab - TDD

## Tools

Please install the following tools:

- Python >=3.6
- Visual Studio Code

Run the following commands on your command line in order to install the missing dependencies:

```
pip install coverage
```

## Test

Run the following command to run all tests and generate a coverage report:

```
cd coverage/
coverage run --source calculator -m unittest discover
coverage html
```