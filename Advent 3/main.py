import re

isdo = True
results = [];

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

def mul(a,b):
    return a*b;
with open("sample.txt","r")as file:
    for line in file:
        tokens = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)",line)
        for token in tokens:
            if re.match(do_pattern,token):
                print("Found a do() command, Multiplation Turned On:")
                isdo = True
            elif re.match(dont_pattern,token):
                print("Found a don't() command, Multiplication Turned Off")
                isdo = False
            elif re.match(pattern,token):
                num1,num2=map(int,re.findall(r"\d+",token))
                if isdo:
                    result = mul(num1,num2)
                    print(f"Multiplying {num1} and {num2}")
                    results.append(result)
def addresults(results):
    sum=0;
    for result in results:
        sum+=result;
    return sum;
print(tokens)
print(addresults(results))











