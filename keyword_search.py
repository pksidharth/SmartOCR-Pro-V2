def search_keyword(text, keyword):

    matches = []

    lines = text.split("\n")

    for line in lines:

        if keyword.lower() in line.lower():

            matches.append(line)

    return matches