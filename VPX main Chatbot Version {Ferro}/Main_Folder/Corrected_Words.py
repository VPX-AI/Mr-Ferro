def Remove_Char_Not_Req(input_string):
    special_characters =["~","`","!","@","#","$","%","^","&","*","(",")","_","-","=","+",
                        "{","}","[","]",":",";","\"","'","|","\\","<",">",",",".","?","/",]
    cleaned_string = ''
    for char in input_string:
        if char not in special_characters:
            cleaned_string += char
    return cleaned_string