import random

def addEval(text: str, doEval = True) -> str:
    return f"eval({text})" if doEval else text

class StringManipulators:
    def string_to_decimal(self, text: str) -> list[int]:
        return list(map(ord, text))

    def decimal_to_chrs(self, array: list, evaluate = True) -> str:
        '''
        Wraps each element of array in `chr()` and concatenates them.
        `evaluate` : Wrap in `eval()` (default True)

        Example: `[101, 102]` -> `eval(chr(101)+chr(102))`
        '''
        return addEval(f'chr({")+chr(".join(map(str, array))})', evaluate)

    def string_to_chrs(self, text: str, evaluate = True) -> str:
        '''
        Converts strings to their decimal equivalent, wrapped in `chr()` and concatenated.
        `evaluate` : Wrap in `eval()` (default True)

        Example: `Hello` -> `eval(chr(72)+chr(101)+chr(108)+chr(108)+chr(111))`
        '''
        return addEval(self.decimal_to_chrs(list(map(ord, text)), evaluate=False), evaluate)

class NumberManipulators:
    def int_addition(self, num: int, evaluate = True) -> str:
        '''
        Self explanatory look at the example
        `evaluate` : Wrap in `eval()` (default True)

        Example: `10` -> `eval(1+1+1+1+1+1+1+1+1+1)`
        '''
        return addEval("+".join(["1"] * num), evaluate)

class FormatManipulators:
    def format_to_string(self, array: list|tuple, doubleQuotes = False, evaluate = True) -> str:
        '''
        Takes in an iterable, and formats into string, concatenated
        `evaluate` : Wrap in `eval()` (default True)

        Example: `["A","B",1,2,3]` -> `'%s%s%s%s%s'%('A', 'B', 1, 2, 3)`
        '''
        quotes = '"' if doubleQuotes else "'"
        return addEval(f'''{quotes}{"%s"*len(array)}{quotes}%{str(tuple(array))}''', evaluate) # wtf is this 1 liner

    def format_to_number(self, number: int, primitives=["bool", "comparison", "number"], doubleQuotes = False, nesting = True, percentLetters = ['s', 'd'], evaluate = True):
        '''
        Returns a format string that evaluates to the number.
        `primitives` : List of primitives to use to construct. valid are ["bool", "comparison", "number"]. Will be used randomly
        `evaluate` : Wrap in `eval()` (default True)

        Example:
        '''
        assert len(primitives) >= 1, 'You must choose at least 1 primitive. Valid include ["bool", "comparison", "number"]'
        assert ('s' in percentLetters or 'd' in percentLetters), "Invalid percent letter. Must any of these ['s', 'd']"
        assert type(number) == int, 'Specified number must be an integar'

        quotes = '"' if doubleQuotes else "'"

        isNegative = number != abs(number)
        number = abs(number)
        if nesting:
            payloadList = []
            for digit in str(number):
                # Construct single digit
                prim = random.choice(primitives)
                if prim == "number":
                    zero = 0
                else:
                    zero = "-(1==0)" if prim == "comparison" else "-False"
                payloadList.append(f"{'-~'*int(digit)}{zero}")

            if isNegative:
                payloadList[0] = "-" + payloadList[0]
            
            # amazing one-liner very readable good coding
            return addEval(f'''{quotes}{"".join([f'%{random.choice(percentLetters)}' for _ in range(len(payloadList))])}{quotes}%{str(tuple(payloadList)).replace("'","")}''', evaluate)
        else:
            prim = random.choice(primitives)
            if prim == "number":
                zero = 0
            else:
                zero = "-(1==0)" if prim == "comparison" else "-False"
            if evaluate:
                return addEval(f'''{quotes}{'-' if isNegative else ''}{'-~'*int(number)}{zero}{quotes}''', evaluate)
            else:
                return f'''{'-' if isNegative else ''}{'-~'*int(number)}{zero}'''
