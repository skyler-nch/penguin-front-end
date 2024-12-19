def svg_injection(svg_file_name:str) -> None:
    svg_file = open(f"./src/svgs/{svg_file_name}.svg",'r')
    svg_str = svg_file.read()
    svg_file.close()
    return svg_str