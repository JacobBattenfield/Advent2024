safenum=0
def determineSaftey(data):
    increasing = data[1]>data[0];
    violations = 0
    for i in range(len(data)-1):
        diff=data[i+1]-data[i]
        if abs(diff)>3 or diff==0:
            violations+=1
        if (diff>0 and not increasing) or (diff<0 and increasing):
            violations+=1
        if(violations>1):
            return False
    return True;
with open("input.txt","r") as file:
    for line in file:
        numbers = []
        for num in line.split():
            numbers.append(int(num));
        if determineSaftey(numbers):
            safenum+=1;
print(safenum)
        
