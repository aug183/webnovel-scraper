import os

i = 0
for x in range(1):
    name = f"Chapter{x+1}.txt"
    print(name)
    name2 = f"Chapter{x+1}.xhtml"
    
    with open(name, 'r') as chapter, open(name2, 'w') as writeChapter:
        print(name2)
        if chapter:
            if writeChapter:
                print(f"Chapter {x + 1}")
                holder = chapter.readline().strip()
                while not holder:
                    holder = chapter.readline().strip()

                writeChapter.write("<html xmlns=\"http://www.w3.org/1999/xhtml\">\n")
                writeChapter.write(f"  <head><title>{holder}</title></head>\n")
                writeChapter.write("    <body>\n")
                writeChapter.write(f"      <h1>{holder}</h1>\n")

                for line in chapter:
                    writeChapter.write(f"      <p>{line.strip()}</p>\n")

                writeChapter.write("    </body>\n")
                writeChapter.write("</html>")

    i += 1

print("number of files", i)
input("Press Enter to continue...")
