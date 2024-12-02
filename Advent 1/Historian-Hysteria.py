rightlist = []
leftlist = []
with open("example.txt","r")as file:
    for line in file:
        parts = line.strip().split('   ')
        if len(parts)==2:
            left,right = map(int,parts)
            leftlist.append(left)
            rightlist.append(right)
def bubbleSort(list):
    swappedSomething = True
    while(swappedSomething):
        swappedSomething=False
        for i in range(len(list)-1):
            if(list[i]>list[i+1]):
                swappedSomething=True;
                temp = list[i];
                list[i]=list[i+1];
                list[i+1]=temp;
    return list;
orderedRight = bubbleSort(rightlist);
orderedLeft = bubbleSort(leftlist);
def totalDistance(orderedRight, orderedLeft):
    distance = 0;
    for i in range(len(orderedRight)):
        if orderedLeft[i]>orderedRight[i]:
            distance = distance+(orderedLeft[i]-orderedRight[i]);
        elif orderedLeft[i]<orderedRight[i]:
            distance = distance+(orderedRight[i]-orderedLeft[i]);
    return distance;
def similarityScore(orderedRight,orderedLeft):
    similarity = 0;
    for i in range(len(orderedLeft)):
        for j in range(len(orderedRight)):
            if orderedLeft[i]==orderedRight[j]:
                similarity=similarity+orderedRight[j];
    return similarity;
print(totalDistance(orderedRight,orderedLeft))
print(similarityScore(orderedRight,orderedLeft))



    


