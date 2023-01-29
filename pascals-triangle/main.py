# Pascal's Triangle
# Given a row of non-negative integer NumRows generate the first numRows of Pascal's triangle

numberOfRows = int(input())

triangle = []

triangle.append([1])

for i in range(1, numberOfRows):
    prevRow = triangle[i-1]
    xs = []

    xs.append(1)
    
    for j in range(1, i):
        xs.append(prevRow[j - 1] + prevRow[j])

    xs.append(1)
    triangle.append(xs)


#[1]
#[1, 1]
#[1, 2, 1]
#[1, 3, 3, 1]
#[1, 4, 6, 4, 1]
print(triangle)