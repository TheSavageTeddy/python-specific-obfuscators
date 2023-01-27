

def string_to_chrs(text: str):
    '''
    Simply converts strings to their decimal equivalent, wrapped in chr() and concatenated.
    
    Example: "Hello" -> "chr(72)+chr(101)+chr(108)+chr(108)+chr(111)"
    '''
    return f'chr({")+chr(".join(map(str, map(ord, text)))})' # sorry for unreadable code

