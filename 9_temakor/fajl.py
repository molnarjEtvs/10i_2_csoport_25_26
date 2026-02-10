'''
with open("hello.txt","r",encoding="utf-8") as f:
    for sor in f:
        print(sor.strip())
'''
with open("iras.txt","w",encoding="utf-8") as f:
    f.write("Hello világ")