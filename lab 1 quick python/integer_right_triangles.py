def integer_right_triangles(perimeter):
    lists = []
    for i in range(1,perimeter):
        for j in range(i,perimeter):
            k = perimeter-i-j
            triangle = (i,j,k)
            triangle = sorted(triangle)
            if triangle[0]<=0 or triangle[1]<=0 or triangle[2]<= 0:
                break
            if triangle[0]**2 + triangle[1]**2 == triangle[2]**2:
                lists.append((triangle[0],triangle[1],triangle[2]))
    lists = list(set(lists))
    return lists
