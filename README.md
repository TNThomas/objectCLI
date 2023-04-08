# objectCLI
A simple CLI for interacting with the fields of an object
## Requirements
Python 3.10+
## Usage
Run the tests.
```sh
pytest .
```
Start the CLI (Windows).
```sh
python main.py
```
Start the CLI (Ubuntu).
```sh
python3 main.py
```
## CLI
### SET
Set or overwrite a property.
```
SET propertyname=value
```
Everything before the `=` character will become part of the property name, including trailing space. Everything after the `=` becomes part of the value, including leading space.

You may not set a property called `*`, as it is a reserved keyword.
### GET
Print a property value.
```
GET propertyname
```
Print all property values.
```
GET *
```
When using this syntax, each value is printed on a separate line in the format `propertyname=value`.

### EXIT
Exit the application.
```
EXIT
```