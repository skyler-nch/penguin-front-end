def css_injection(css_file_name:str, scss:bool=False) -> None:
    if scss == False:
        css_file = open(f"./src/styles/{css_file_name}.css",'r')
    else:
        css_file = open(f"./src/styles/{css_file_name}.scss",'r')
    css_str = css_file.read()
    css_file.close()
    return css_str