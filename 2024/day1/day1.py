#!/usr/bin/env python3

#define and initialize variables for part 1
totalDistance = 0
firstCol = list()
secondCol = list()

#iterate through each line in the file and add to 2 separate lists
with open('input.txt', 'r') as file:
    for line in file:
        numbers = list(map(int, filter(None, line.strip().split())))
        firstCol.append(numbers[0])
        secondCol.append(numbers[1])

#define and initialize variables for part 2
sortedFirstCol = sorted(firstCol)
sortedSecondCol = sorted(secondCol)
similarityScoreDict = dict()
similarityScore = 0

#count the occurrences that col 1 list value appears in col 2 list
for value in sortedFirstCol:
    if value in similarityScoreDict:
        currentCount = similarityScoreDict[value]
        similarityScoreDict[value] = currentCount + sortedSecondCol.count(value)
    elif value not in similarityScoreDict:
        similarityScoreDict[value] = sortedSecondCol.count(value)

#calculate the similarity scores
for key, value in similarityScoreDict.items():
    similarityScore += key * value

#calculate the total distance for part 1
for i in range(len(firstCol)):
    totalDistance += abs(sortedFirstCol[i] - sortedSecondCol[i])

print('Total Distance: ' + str(totalDistance))
print('Similarity Score: ' + str(similarityScore))
