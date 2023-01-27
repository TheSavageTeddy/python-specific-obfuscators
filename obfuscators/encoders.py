

def string_to_ords(text: str):
    '''
    Simply converts strings to their decimal equivalent, wrapped in ord() and concatenated.
    
    Example: "Hello" -> "ord(104)+ord(101)+ord(108)+ord(108)+ord(111)"
    '''
    return f'ord({")+ord(".join(map(str, map(ord, text)))})' # sorry for unreadable code

print(string_to_ords("hello"))