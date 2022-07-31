import os
cwd = os.getcwd() # sloppy but whatever

spark_notes = 'spark_notes.txt' # chapter notes obtained from https://www.bookseriesrecaps.com/what-happened-in-the-name-of-the-wind/
premise_path = 'premises' # folder to store them

# splitting each paragraph into chapter premises
chapter_num = 0
for premise in open(spark_notes).readlines():
    new_chapter = open('\\'.join([cwd, premise_path, 'chapter_'+str(chapter_num)])+'.txt', 'w')
    new_chapter.write(premise)
    new_chapter.close()
    chapter_num+=1