import datetime
now = datetime.datetime.now()
f = open("sample.txt", "rt", encoding="utf-8")
f2 = open(f"sample_{now.year}_{now.month:02d}_{now.day:02d}.txt", "at", encoding="utf-8")
f2.write(f.read())
f.close()
f2.close()
