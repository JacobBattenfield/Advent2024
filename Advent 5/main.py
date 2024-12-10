import re,math
#patterns
rulesPattern = r"(\d+)\|(\d+)";
pagesPattern = r"^\d+(?:,\d+)*$"
#storage
rules = []
pages = []
validPages = []
invalidPages = []
#openfile, get info
with open("input.txt","r")as file:
    for line in file:
        line = line.strip()
        if re.match(rulesPattern,line):
            matches = re.findall(rulesPattern,line)
            rules.extend(matches)
        elif re.match(pagesPattern,line):
            pages.append(line.split(","))
#checks if line is valid by index checking all the rules
def isValidLine(rules,page):
    for rule in rules:
        first,second = rule
        try:
            first_index = page.index(first)
            second_index=page.index(second)

            if first_index>=second_index:
                return False
        except ValueError:
            continue
    return True
#will apply fixes where violations occur in the invalid lists
def fixInvalid(rules,page):
    while True:
        fixed_this_round = False
        for rule in rules:
            first,second = rule
            try: 
                first_index=page.index(first)
                second_index=page.index(second)

                if(first_index>=second_index):
                    print(f"Violation Found {first} after {second}...fixing...")
                    page.remove(first)
                    page.insert(second_index,first)
                    fixed_this_round=True
                    break
            except ValueError:
                continue
        if not fixed_this_round:
            break
#stores valid pages in an array as well as invalid pages
for page in pages:
    if isValidLine(rules,page):
        validPages.append(page)
    else:
        invalidPages.append(page)
#returns the middle index of a list
def getMiddleNumber(page):
    middleindex = math.ceil(len(page)/2)-1
    return middleindex
#sums all of the middle indexes of a array of lists
def SumMiddles(pages):
    sum = 0
    for page in pages:
        sum+=int(page[getMiddleNumber(page)])
    return sum
#Part One Answer
print(SumMiddles(validPages))
for page in invalidPages:
    print(invalidPages[int(page)])
    fixInvalid(rules,page)
print(SumMiddles(invalidPages))
    


