import re


s = '''
%test SQL Comment Sequence Detected (981231)
########################################
%output 981231
%var sig=SELECT%2F*avoid-spaces*%2Fpassword%2F**%2FFROM%2F**%2FMembers
%var sig=%E2%80%98%20or%201%3D1%23%0A
%var sig=%E2%80%98%20or%201%3D1--%20-
%endtest


%test SQL Hex Encoding Identified (981260)
########################################
%output 981260
%var sig=1%20and%201%3D0%20%20Union%20Select%20%20%20UNHEX(HEX(concat(0x5B6B65795D%2Ctable_name%2C0x5B6B65795D)))%20%20%20FROM%20INFORMATION_SCHEMA.tables%20where%20table_schema%3DConcat(char(109)%2Cchar(101)%2Cchar(115)%2Cchar(115)%2Cchar(110)%2Cchar(101)%2Cchar(114)%2Cchar(98)%2Cchar(95)%2Cchar(119)%2Cchar(114)%2Cchar(100)%2Cchar(49)%2Cchar(50))%20LIMIT%201%2C1--
%var sig=999999.9%20union%20all%20select%200x31303235343830303536%2C0x31303235343830303536--
%endtest


%test SQL Injection Attack: Common Injection Testing Detected (981318)
########################################
%output 981318
%var sig='%20and%200%20union%20select%201%2C2%2C3%2Cusername%2C5%2Cpassword%2C7%2C8%2C9%2C10%2C11%20from%20%23__users%23
%var sig=-1)%20UNION%20SELECT%201%2C2%2C3%2Cconcat(USER()%2C'
%endtest


%test SQL Injection Attack: SQL Operator Detected (981319)
########################################
%output 981319
%var sig=-4%20union%20select%201%2C2%2C(select(%40x)from(select(%40x%3A%3D0x00)%2C(select(null)from(information_schema.columns)where(table_schema!%3D0x696e666f726d6174696f6e5f736368656d61)and(0x00)in(%40x%3A%3Dconcat(%40x%2C0x3c62723e%2Ctable_schema%2C0x2e%2Ctable_name%2C0x3a%2Ccolumn_name))))x)--
%var sig=14380586%20and%20user()%3C%3E1
%var sig=2946%20and%20ascii(substring((user())%2C1%2C1))%3E%3D1%2F*
%endtest


%test SQL Injection Attack: SQL Tautology Detected (950901)
########################################
%output 950901
%var sig=-9'%20union%20select%20concat(version())%2C2%2C3%2C4%2C5%2C6and'1'%3D'1
%var sig=1'%20or%20'1'!%3D'2%20order%20by%201--
%endtest


%test SQL Injection Attack: Common DB Names Detected (981320)
########################################
%output 981320
%var sig=3%20union%20select%201%2C2%2C3%2C4%2C5%2C6%2Cconcat(user()%2Cversion()%2Cdatabase())%2C8%20from%20information_schema.tables
%var sig=918%20union%20select%200%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C8%2C9%2C10%2C11%2C12%20from%20msysobjects%20in%20'.'
%endtest


%test SQL SELECT Statement Anomaly Detection Alert (981317)
########################################
%output 981317
%var sig=247'%20and%201%3D1%20union%20all%20select%201%2C2%2C3%2C4%2C5%2Cconcat(username%2Cchar(58)%2Cpasswort)%2C7%2C8%2C9%2C10%2C11%2C12%2C13%2C14%2C15%2C16%2C17%2C18%2C19%2C20%2C21%2C22%2C23%2C24%2C25%20from%20az_user%2F*
%var sig=5%20and%201%3D(select%20first%201%20distinct%20rdb%24relation_name%20from%20rdb%24relations%20where%20rdb%24system_flag%3D0)--
%endtest


%test Blind SQL Injection Attack (950007)
########################################
%output 950007
%var sig=-2511%20union%20select%20table_name%20from%20sys.all_tables--
%var sig=1%20union%20select%201%2Cnull%2Cnull%2Cnull%2Ctable_name%7C%7Cchr(58)%7C%7Ccolumn_name%7C%7Cchr(58)%7C%7Cdata_type%20from%20(select%20a.*%2Crownum%20rnum%20from%20(select%20*%20from%20user_tab_columns%20where%20table_name%3Dchr(76)%7C%7Cchr(79)%7C%7Cchr(71)%7C%7Cchr(73)%7C%7Cchr(78)%7C%7Cchr(83)%20order%20by%20column_name)%20a%20where%20rownum%20%3C%3D%201)%20where%20rnum%20%3E%3D%201--
%endtest


%test SQL Injection Attack (950001)
########################################
%output 950001
%var sig=10%20UNION%20exec%20master..xp_cmdshell%20'dir'
%var sig=1'%20or%20(select%20count(*)%20from%20(select%201%20union%20select%202%20union%20select%203)x%20group%20by%20concat(mid(concat_ws(0x0b%2Cversion()%2Cuser()%2Cdatabase()%2C%40%40version_compile_os%2C0x0b)%2C1%2C63)%2C%20floor(rand(0)*2)))--
%endtest


%test SQL Injection Attack (959070)
########################################
%output 959070
%var sig=-247%20union%20select%201%2C2%2C3%2C4%2C5%2C6%2C7%2C8%2C9%2C10%2C11%2C12%2C13%2Cconcat_ws(0x3a%2Cversion()%2Cdatabase()%2CuseR())%2C15%2C16%2C17%2C18%2C19%2C20%2C21%2C22%2C23%2C24%2C25%2C26%2C27%2C28%2C29%2C30%2C31%2C32%2C33%2C34%2C35%2C36%2C37%2C38%2C39%0A1%20having%201%3D1--
%var sig=256%20%20AND%201%3Cascii(substring((SELECT%20column_name%20FROM%20information_schema.columns%20WHERE%20table_name%20like%20char(105%2C109%2C103%2C101%2C115)%20limit%201%2C1)%2C1%2C1))
%endtest


%test SQL Injection Attack (959071)
########################################
%output 959071
%var sig=1'%20or%201%3D(SELECT%20TOP%201%20email%20FROM%20cdrequests%20where%20id%3D2000)--
%var sig=1'%20or%20'1'%3D'1%20order%20by%201--
%endtest


%test SQL Injection Attack (959072)
########################################
%output 959072
%var sig=99999999%20and%201%3D2%20union%20select%201%2Cconcat(user()%2Cchar(58)%2Cversion()%2Cchar(58)%2Cdatabase())%2C3%2C4%2F*
%var sig=-9'%20union%20select%20concat(version())%2C2%2C3%2C4%2C5%2C6%2Cand'1'%3D'1
%endtest



%test SQL Injection Attack (950908)
########################################
%output 950908
%var sig=6%20AND%20ASCII(SUBSTR((COALESCE(5%2C%20NULL))%2C%201%2C%201))%20%3E%2063
%endtest


%test SQL Injection Attack (959073)
########################################
%output 959073
%var sig=-120%20union%20all%20select%201%2Ccast(table_name%20as%20text)%20from%20information_schema.columns--
%var sig=-1100%20UNION%20SELECT%201%2C2%2C3%2C4%2C5%2C6%2C7%2C8%2Cconcat_ws(0x2b%2Cversion()%2Cuser()%2C%40%40version_compile_os)%2C10%2C11%2C12%20--
%endtest



%test Detects blind sqli tests using sleep() or benchmark() (981272)
########################################
%output 981272
%var sig=-207%20union%20select%201%2Cconcat(%40i%3A%3D0x00%2C%40o%3A%3D0x0d0a%2Cbenchmark(23%2C%40o%3A%3DCONCAT(%40o%2C0x0d0a%2C(SELECT%20concat(table_schema%2C0x2E%2C%40i%3A%3Dtable_name)%20from%20information_schema.tables%20WHERE%20table_name%3E%40i%20order%20by%20table_name%20LIMIT%201)))%2C%40o)%2C3%2C4%2C5--
%var sig=13%20and%20sleep(3)%23
%endtest


%test Detects basic SQL authentication bypass attempts 1/3 (981244)
########################################
%output 981244
%var sig=aaa'%20or%20(1)%3D(1)%20%23!asd
%var sig=aa'%20LIKE%20md5(1)%20or%20'1
%endtest


%test Detects MSSQL code execution and information gathering attempts (981255)
########################################
%output 981255
%var sig='%20union%20select%20concat(UserId%2Cchar(58)%2CUserPassword)%20from%20users%20into%20outfile%20'content%2F1.php'%2F*
%var sig=1'%20or%201%3D(%40%40version%20)%3Bexec%20master..xp_cmdshell
%endtest


%test Detects MySQL comment-/space-obfuscated injections and backtick termination (981257)
########################################
%output 981257
%var sig=1%0bAND(SELECT%0b1%20FROM%20mysql.x)
%endtest



%test Detects chained SQL injection attempts 1/2 (981248)
########################################
%output 981248
%var sig=0%20div%201%20-%20union%23foo*%2F*bar%0Aselect%23foo%0A1%2C2%2Ccurrent_user
%endtest



%test Detects SQL benchmark and sleep injection attempts including conditional queries (981250)
########################################
%output 981250
%var sig=SELECT%20BENCHMARK(1000000%2CMD5(%E2%80%98A%E2%80%99))%3B
%var sig=SELECT%20SLEEP(5)%3B%20%23%20%3E%3D%205.0.12
%endtest


%test Detects conditional SQL injection attempts (981241)
########################################
%output 981241
%var sig=1194%20or%201%20group%20by%20concat(version()%2Cfloor(rand(0)*2))having%20min(0)%20or%201--
%endtest


%test Detects MySQL charset switch and MSSQL DoS attempts (981252)
########################################
%output 981252
%var sig=-1'%3B%20if%20'1'%3D'1'%3B%20waitfor%20time%20'00%3A00%3A01'--
%endtest



%test Detects MATCH AGAINST, MERGE, EXECUTE IMMEDIATE and HAVING injections (981256)
########################################
%output 981256
%var sig=-148)%20or%201%20group%20by%20concat(%40%40version%2Cfloor(rand(0)*2))%20having%20min(0)%20or%201%20--
%endtest


%test Detects basic SQL authentication bypass attempts 2/3 (981245)
########################################
%output 981245
%var sig=-121%20union%20all%20select%201%2Cgroup_concat(Username%2C0x3a%2CPassword%2C0x3a%2CUserGroup)%2C3%2C4%2C5%20from%20uvp_Users
%var sig=-10'%20union%20select%201%2Cconcat_ws(0x3a%2Ctable_name%2Ctable_schema)%2C3%20from%20information_schema.columns%20where%20column_name%20like%20'name'%23
%endtest
'''


state = 0
container = {}
i = -1
for line in s.splitlines():
	if line.startswith('%test'):
		state = 1
		i = i + 1
		container[i] = []
	else:
		if line.startswith('%endtest'):
			state = 0

	if state == 1:
		container[i].append(line)

newcontainer = []
for k, v in container.items():
    data = {
        "var": []
    }
    for line in v:
        if line.startswith('%test'):
            data['title'] = line[5:]
            m = re.search('(\(\d+\))', data['title'])
            data['id'] = m.group(0)[1:-1]
        elif line.startswith('%var'):
            data['var'].append(line[4:])
    newcontainer.append(data)



# # to openresty test code
i = 0
for c in newcontainer:
    for v in c['var']:
        i = i + 1
        print '''
=== TEST#i#: #title#
--- http_config eval: $::http_config
--- config
location /abcd {
  root html;
}
--- request
GET /abcd?#v#
--- error_code: 403
--- error_log: #id#'''.replace('#i#', str(i)).replace('#title#', c['title']).replace('#id#', c['id']).replace('#v#', v.strip())
