class StringManipulators:
    def decimal_to_chrs(self, array: list) -> str:
        '''
        Wraps each element of array in `chr()` and concatenates them.

        Example: `[101, 102]` -> `chr(101)+chr(102)`
        '''
        return f'chr({")+chr(".join(map(str, array))})'

    def string_to_chrs(self, text: str) -> str:
        '''
        Converts strings to their decimal equivalent, wrapped in `chr()` and concatenated.

        Example: `Hello` -> `chr(72)+chr(101)+chr(108)+chr(108)+chr(111)`
        '''
        return self.decimal_to_chrs(list(map(ord, text)))

class NumberManipulators:
    def int_addition(self, num: int) -> str:
        '''
        '''
        return "+".join(["1"] * num)

