def sd():
  line3=""
  with open("/Users/yanchenghao/Desktop/33.txt", "r", encoding="utf-8") as f1, open("/Users/yanchenghao/Desktop/log33.txt", "w", encoding="utf-8") as f2:

    for line in f1.readlines():
        line1=line[:-4]
        line2 = line1[1:]
        line3 = line2[0:2]
        lin4=line2[6:]
        lin5='"'+line3+'"'+","
        print(lin5)
        f2.write(lin5)
sd()