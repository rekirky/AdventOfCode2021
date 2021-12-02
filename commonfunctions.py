def process_input(file):
    clean = []
    with open(file) as f:
        input = f.readlines()
    for i in input:
        clean.append(i.strip())
    return(clean)