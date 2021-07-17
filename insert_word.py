import pymysql
f=open('dict.txt','r')
db=pymysql.connect(user='root',
                   passwd='123456',
                   database='dict',
                   charset='utf8')
cur=db.cursor()
sql = "insert into words (word,mean) values (%s,%s);"
for line in f:
    list01=line.split(' ',1)
    word=list01[0]
    mean=list01[1].strip()
    cur.execute(sql,[word,mean])
try:
    db.commit()
except Exception as e:
    db.rollback()
cur.close()
db.close()
