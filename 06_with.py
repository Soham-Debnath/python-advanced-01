with(
    open("file1.txt") as f1,
    open("file2.txt") as f2
):
    
    print(f1.read(), f2.read())
    
    