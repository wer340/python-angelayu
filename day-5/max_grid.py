print("average highest grid of student")
#you cant use  sum()  and len() function
grids=input("type list of height of student ? ").split()
max_grid=0

for grid in grids:
    #grid=int(grid)
    if max_grid<int(grid):
        max_grid =int(grid)


print(f"maximum of student is = {max_grid}")