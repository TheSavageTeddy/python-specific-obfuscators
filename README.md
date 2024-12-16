# Python Custom Obfuscator

Build your own custom obfuscated python code from a list of obfuscators!

## StringManipulators
Class of obfuscators that allow obfuscation of the strings of code to their equivalent devimal values. Upon evaluation, the code is returned to orignal format.

### string_to_decimal(text: str) -> list[int]
  - Converts a string to a list of its decimal ASCII values.
### string_to_chrs(text: str, evaluate = True) -> str
  -  **If evaulate is True:** Converts code lines into decimal equivalents and returns the list of decimal values encoded wraped in chr() and eval() functions, ready to be executed in the script.
  -  **If evaluate is False:** Converts code lines into decimal equivalents and returns it as a string of decimal values encoded wraped in chr() function, but not in eval() function. The returned string is not ready to be executed in the script, but can be executed using the eval() function.
### decimal_to_chrs(array: list, intWrap = False, evaluate = True) -> str
  - Takes in a list of decimal (preferably) or float (get typecasted to integers) ASCII values that represent the characters of the code. Returns string of the decimal characters wraped in the char() function, to create executable code using eval() function.
#### Options:
  - **intWrap** *(Boolean)*: Decides whether or not to wrap every element into the array in the int() function. Useful for converting float values into decimal values prior to conversion into characters.
  - **evaluate** *(Boolean)*: Decides whether or not to wrap the returned string in the eval() function.

## NumberManipulators
Class of obfuscators that allow obfuscation of code by encoding the ASCII values of the characters of the code as repeated sums of 1's. Use this obfuscation wisely as it results in an extremely high character count that can amke th code base extremely heavy. 

### int_addition(num: int, evaluate = True) -> str
  - Converts the input number into a string of 1's and '+' added 'num' times. If evaluate is set to True, the returned string is wrapped in eval() function. Otherwise, the raw string is returned.

## FormatManipulators
This class provides methods for code obfuscation by generating format strings for both strings and numbers.

### format_to_string(array: list | tuple, percentLetters=["c"], doubleQuotes=False, removeQuotes=False, evaluate=True) -> str
  - Takes an iterable and formats it into a concatenated string using specified percent letters. Optionally wraps the result in eval(). The method retuens the formatted string of code.
#### Parameters:
  - array (list | tuple): The input iterable.
  - percentLetters (list[str], optional): Letters to use in the format string. Defaults to ["c"].
  - doubleQuotes (bool, optional): Whether to use double quotes. Defaults to False.
  - removeQuotes (bool, optional): Whether to remove quotes in the formatted string. Defaults to False.
  - evaluate (bool, optional): Whether to wrap the result in eval(). Defaults to True.


### format_to_number(number: int, primitives=["bool", "comparison", "number"], doubleQuotes=False, nesting=True, percentLetters=["s", "d"], evaluate=True)
  - Generates a format string that evaluates to the specified number using various primitives. Optionally wraps the result in eval().

#### Parameters:

  - number (int): The target number.
  - primitives (list[str], optional): List of primitives to use. Valid options are ["bool", "comparison", "number"]. Defaults to ["bool", "comparison", "number"].
  - doubleQuotes (bool, optional): Whether to use double quotes. Defaults to False.
  - nesting (bool, optional): Whether to use nesting in the format string. Defaults to True.
  - percentLetters (list[str], optional): Letters to use in the format string. Defaults to ["s", "d"].
  - evaluate (bool, optional): Whether to wrap the result in eval(). Defaults to True.

## License Information
This project is issues under ```GPL-3.0 LICENSE```. For more information, please check the ```LICENSE``` file.


