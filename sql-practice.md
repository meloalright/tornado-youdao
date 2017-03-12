#sql-practive   
   
```sql
>>> sqlite3
>>> \

CREATE TABLE STUDENT(
    SNO VARCHAR(3) NOT NULL, 
    SNAME VARCHAR(4) NOT NULL,
    SSEX VARCHAR(2) NOT NULL, 
    SBIRTHDAY DATETIME,
    CLASS VARCHAR(5)
);

CREATE TABLE COURSE(
    CNO VARCHAR(5) NOT NULL, 
    CNAME VARCHAR(10) NOT NULL, 
    TNO VARCHAR(10) NOT NULL
);

CREATE TABLE SCORE (
    SNO VARCHAR(3) NOT NULL, 
    CNO VARCHAR(5) NOT NULL, 
    DEGREE NUMERIC(10, 1) NOT NULL
);

CREATE TABLE TEACHER (
    TNO VARCHAR(3) NOT NULL, 
    TNAME VARCHAR(4) NOT NULL,
    TSEX VARCHAR(2) NOT NULL, 
    TBIRTHDAY DATETIME NOT NULL,
    PROF VARCHAR(6), 
    DEPART VARCHAR(10) NOT NULL
);

INSERT INTO STUDENT (SNO,SNAME,SSEX,SBIRTHDAY,CLASS) VALUES (108 ,'曾华' 
,'男' ,1977-09-01,95033);
INSERT INTO STUDENT (SNO,SNAME,SSEX,SBIRTHDAY,CLASS) VALUES (105 ,'匡明' 
,'男' ,1975-10-02,95031);
INSERT INTO STUDENT (SNO,SNAME,SSEX,SBIRTHDAY,CLASS) VALUES (107 ,'王丽' 
,'女' ,1976-01-23,95033);
INSERT INTO STUDENT (SNO,SNAME,SSEX,SBIRTHDAY,CLASS) VALUES (101 ,'李军' 
,'男' ,1976-02-20,95033);
INSERT INTO STUDENT (SNO,SNAME,SSEX,SBIRTHDAY,CLASS) VALUES (109 ,'王芳' 
,'女' ,1975-02-10,95031);
INSERT INTO STUDENT (SNO,SNAME,SSEX,SBIRTHDAY,CLASS) VALUES (103 ,'陆君' 
,'男' ,1974-06-03,95031);

INSERT INTO COURSE(CNO,CNAME,TNO)VALUES ('3-105' ,'计算机导论',825);
INSERT INTO COURSE(CNO,CNAME,TNO)VALUES ('3-245' ,'操作系统' ,804);
INSERT INTO COURSE(CNO,CNAME,TNO)VALUES ('6-166' ,'数据电路' ,856);
INSERT INTO COURSE(CNO,CNAME,TNO)VALUES ('9-888' ,'高等数学' ,100);

INSERT INTO SCORE(SNO,CNO,DEGREE)VALUES (103,'3-245',86);
INSERT INTO SCORE(SNO,CNO,DEGREE)VALUES (105,'3-245',75);
INSERT INTO SCORE(SNO,CNO,DEGREE)VALUES (109,'3-245',68);
INSERT INTO SCORE(SNO,CNO,DEGREE)VALUES (103,'3-105',92);
INSERT INTO SCORE(SNO,CNO,DEGREE)VALUES (105,'3-105',88);
INSERT INTO SCORE(SNO,CNO,DEGREE)VALUES (109,'3-105',76);
INSERT INTO SCORE(SNO,CNO,DEGREE)VALUES (101,'3-105',64);
INSERT INTO SCORE(SNO,CNO,DEGREE)VALUES (107,'3-105',91);
INSERT INTO SCORE(SNO,CNO,DEGREE)VALUES (108,'3-105',78);
INSERT INTO SCORE(SNO,CNO,DEGREE)VALUES (101,'6-166',85);
INSERT INTO SCORE(SNO,CNO,DEGREE)VALUES (107,'6-106',79);
INSERT INTO SCORE(SNO,CNO,DEGREE)VALUES (108,'6-166',81);

INSERT INTO TEACHER(TNO,TNAME,TSEX,TBIRTHDAY,PROF,DEPART) 
VALUES (804,'李诚','男','1958-12-02','副教授','计算机系');
INSERT INTO TEACHER(TNO,TNAME,TSEX,TBIRTHDAY,PROF,DEPART) 
VALUES (856,'张旭','男','1969-03-12','讲师','电子工程系');
INSERT INTO TEACHER(TNO,TNAME,TSEX,TBIRTHDAY,PROF,DEPART)
VALUES (825,'王萍','女','1972-05-05','助教','计算机系');
INSERT INTO TEACHER(TNO,TNAME,TSEX,TBIRTHDAY,PROF,DEPART) 
VALUES (831,'刘冰','女','1977-08-14','助教','电子工程系');
```
    
##题目   
     
```sql
1、 查询Student表中的所有记录的Sname、Ssex和Class列。 

>> SELECT SNAME,SSEX,CLASS FROM STUDENT;

曾华|男|95033
匡明|男|95031
王丽|女|95033
李军|男|95033
王芳|女|95031
陆君|男|95031



2、 查询教师所有的单位即不重复的Depart列。

>> SELECT DISTINCT DEPART FROM TEACHER;

计算机系
电子工程系



3、 查询Student表的所有记录。

>> SELECT * FROM STUDENT;

108|曾华|男|1967|95033
105|匡明|男|1963|95031
107|王丽|女|1952|95033
101|李军|男|1954|95033
109|王芳|女|1963|95031
103|陆君|男|1965|95031



4、 查询Score表中成绩在60到80之间的所有记录。

sqlite> SELECT * FROM SCORE WHERE DEGREE >= 60 AND DEGREE <= 80;

105|3-245|75
109|3-245|68
109|3-105|76
101|3-105|64
108|3-105|78
107|6-106|79



5、 查询Score表中成绩为85，86或88的记录。

sqlite> SELECT * FROM SCORE WHERE DEGREE IN (85, 86, 88);

103|3-245|86
105|3-105|88
101|6-166|85



6、 查询Student表中“95031”班或性别为“女”的同学记录。

sqlite> SELECT * FROM STUDENT WHERE CLASS = '95031' OR SSEX = '女';

105|匡明|男|1963|95031
107|王丽|女|1952|95033
109|王芳|女|1963|95031
103|陆君|男|1965|95031


7、 以Class降序查询Student表的所有记录。

sqlite> SELECT * FROM STUDENT ORDER BY CLASS DESC;

108|曾华|男|1967|95033
107|王丽|女|1952|95033
101|李军|男|1954|95033
105|匡明|男|1963|95031
109|王芳|女|1963|95031
103|陆君|男|1965|95031



8、 以Cno升序、Degree降序查询Score表的所有记录。

sqlite> SELECT * FROM SCORE ORDER BY CNO ASC , DEGREE DESC;

103|3-105|92
107|3-105|91
105|3-105|88
108|3-105|78
109|3-105|76
101|3-105|64
103|3-245|86
105|3-245|75
109|3-245|68
107|6-106|79
101|6-166|85
108|6-166|81



9、 查询“95031”班的学生人数。

sqlite> SELECT COUNT(*) FROM STUDENT WHERE CLASS = '95031';

3



10、查询Score表中的最高分的学生学号和课程号。

sqlite> SELECT SNO, CNO FROM SCORE WHERE DEGREE = (SELECT MAX(DEGREE) FROM SCORE);

103|3-105



11、查询‘3-105’号课程的平均分。

sqlite> SELECT AVG(DEGREE) FROM SCORE WHERE CNO = '3-105';

81.5



12、查询Score表中至少有5名学生选修的并以3开头的课程的平均分数。

sqlite> SELECT AVG(DEGREE) FROM SCORE WHERE CNO LIKE '3%' GROUP BY CNO HAVING COUNT(SNO) >= 5;

81.5



13、查询最低分大于70，最高分小于90的Sno列。

sqlite> SELECT SNO FROM SCORE WHERE DEGREE >= 70 AND DEGREE <= 90;

103
105
105
109
108
101
107
108

==ANSWER==
sqlite> SELECT SNO FROM SCORE GROUP BY SNO HAVING MIN(DEGREE)>70 AND MAX(DEGREE)<90;

105
108



14、查询所有学生的Sname、Cno和Degree列。

sqlite> SELECT A.SNAME, B.CNO, B.DEGREE FROM STUDENT AS A JOIN SCORE AS B ON A.SNO = B.SNO;

曾华|3-105|78
曾华|6-166|81
匡明|3-105|88
匡明|3-245|75
王丽|3-105|91
王丽|6-106|79
李军|3-105|64
李军|6-166|85
王芳|3-105|76
王芳|3-245|68
陆君|3-105|92
陆君|3-245|86




15、查询所有学生的Sno、Cname和Degree列。

sqlite> SELECT ST.SNO, CR.CNAME, SC.DEGREE FROM (STUDENT AS ST JOIN SCORE AS SC ON ST.SNO=SC.SNO)
        AS MIX LEFT JOIN COURSE AS CR ON MIX.CNO=CR.CNO;

108|计算机导论|78
108|数据电路|81
105|计算机导论|88
105|操作系统|75
107|计算机导论|91
107||79
101|计算机导论|64
101|数据电路|85
109|计算机导论|76
109|操作系统|68
103|计算机导论|92
103|操作系统|86



16、查询所有学生的Sname、Cname和Degree列。

sqlite> SELECT ST.SNAME, CR.CNAME, SC.DEGREE FROM (STUDENT AS ST JOIN SCORE AS SC ON ST.SNO=SC.SNO)
        AS MIX LEFT JOIN COURSE AS CR ON MIX.CNO=CR.CNO;

曾华|计算机导论|78
曾华|数据电路|81
匡明|计算机导论|88
匡明|操作系统|75
王丽|计算机导论|91
王丽||79
李军|计算机导论|64
李军|数据电路|85
王芳|计算机导论|76
王芳|操作系统|68
陆君|计算机导论|92
陆君|操作系统|86




17、查询“95033”班所选课程的平均分。

sqlite> SELECT AVG(T2.DEGREE) FROM (STUDENT  AS T1  LEFT JOIN SCORE AS T2 ON T1.SNO =T2.SNO) 
        WHERE T1.CLASS = '95033';

79.6666666666667





18、假设使用如下命令建立了一个grade表：

create table grade(low number(3,0),upp number(3),rank char(1));
insert into grade values(90,100,'A');
insert into grade values(80,89,'B');
insert into grade values(70,79,'C');
insert into grade values(60,69,'D');
insert into grade values(0,59,'E');
commit;
现查询所有同学的Sno、Cno和rank列。

>> select t1.sno, t2.cno, bt2.rank from ((student as t1 join score as t2 on t1.sno = t2.sno) 
   as bt1 join grade as bt2 on bt1.degree > bt2.low and bt1.degree < bt2.upp);

108|6-166|B
108|3-105|C
105|3-105|B
105|3-245|C
107|3-105|A
101|6-166|B
101|3-105|D
109|3-105|C
109|3-245|D
103|3-105|A
103|3-245|B




19、查询选修“3-105”课程的成绩高于“109”号同学成绩的所有同学的记录。

sqlite> select * from student as t1 join score as t2 on t1.sno = t2.sno
        where cno = '3-105' and degree > (select degree from student as
        t1 join score as t2 on t1.sno = 108);

103|陆君|男|1965|95031|103|3-105|92
105|匡明|男|1963|95031|105|3-105|88
107|王丽|女|1952|95033|107|3-105|91




20、查询score中选学一门以上课程的同学中分数为非最高分成绩的记录。

>>  SELECT * FROM score s WHERE DEGREE<(SELECT MAX(DEGREE) FROM SCORE) GROUP BY SNO HAVING 
    COUNT(SNO)>1 ORDER BY DEGREE

109|3-105|76
107|6-106|79
108|6-166|81
101|6-166|85
105|3-105|88




21、查询成绩高于学号为“109”、课程号为“3-105”的成绩的所有记录。

同19



22、查询和学号为108的同学同年出生的所有学生的Sno、Sname和Sbirthday列。

sqlite> select sno, sname, sbirthday from student where sbirthday = 
        (select sbirthday from student where sno = 108);

108|曾华|1967




23、查询“张旭“教师任课的学生成绩。

sqlite> select s1.sname, s2.degree from student as s1 join score as s2 
        on s1.sno = s2.sno where cno = (select cno from teacher as t1 
        join course as t2 on t1.tno = t2.tno where t1.tname='张旭');

李军|85
曾华|81




24、查询选修某课程的同学人数多于5人的教师姓名。

sqlite> select bt2.tname from ((select count(cno),* from score group by cno limit 1)
        as t1 join course as t2 on t1.cno = t2.cno) as bt1 join teacher as bt2 on 
        bt1.tno = bt2.tno;

王萍

25、查询95033班和95031班全体学生的记录。

sqlite> select * from student where class in (95033, 95031);

108|曾华|男|1967|95033
105|匡明|男|1963|95031
107|王丽|女|1952|95033
101|李军|男|1954|95033
109|王芳|女|1963|95031
103|陆君|男|1965|95031



26、查询存在有85分以上成绩的课程Cno.

sqlite> select cno from (select * from score as t1 join course as t2
        on t1.cno = t2.cno where t1.degree > 85) group by cno;

3-105
3-245



27、查询出“计算机系“教师所教课程的成绩表。

sqlite> select o1.degree from (score as t1 join course as t2 on t1.cno = t2.cno) 
        as o1 join teacher as o2 on o1.tno = o2.tno where o2.depart = '计算机系';

86
75
68
64
92
88
91
78
76



28、查询“计算机系”与“电子工程系“不同职称的教师的Tname和Prof。


29、查询选修编号为“3-105“课程且成绩至少高于选修编号为“3-245”的同学的Cno、Sno和Degree,并按Degree从高到低次序排序。


30、查询选修编号为“3-105”且成绩高于选修编号为“3-245”课程的同学的Cno、Sno和Degree.


31、查询所有教师和同学的name、sex和birthday.


32、查询所有“女”教师和“女”同学的name、sex和birthday.


33、查询成绩比该课程平均成绩低的同学的成绩表。


34、查询所有任课教师的Tname和Depart.


35  查询所有未讲课的教师的Tname和Depart. 


36、查询至少有2名男生的班号。


37、查询Student表中不姓“王”的同学记录。


38、查询Student表中每个学生的姓名和年龄。


39、查询Student表中最大和最小的Sbirthday日期值。


40、以班号和年龄从大到小的顺序查询Student表中的全部记录。


41、查询“男”教师及其所上的课程。


42、查询最高分同学的Sno、Cno和Degree列。


43、查询和“李军”同性别的所有同学的Sname.


44、查询和“李军”同性别并同班的同学Sname.


45、查询所有选修“计算机导论”课程的“男”同学的成绩表





























```