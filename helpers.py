#check & replace to 2 single quote
def check_single_quote(string):
    if string.find("'") != -1:
        return string.replace("'", "''")
    else:
        return string