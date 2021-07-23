class Member:
    def __init__(self):
        self.name = None
        self.account = None
        self.passwd = None
        self.birthyear = None


회원1 = Member()
회원1.name = '철수'
회원1.account = 'cjftn1@naver.com'
회원1.passwd = 'cjftn'
회원1.birthyear = 1995

회원2 = Member()
회원2.name = '영희'
회원2.account = 'dudgml1@daum.net'
회원2.passwd = 'dudgml'
회원2.birthyear = 1994

회원3 = Member()
회원3.name = '민수'
회원3.account = 'alstn@naver.com'
회원3.passwd = 'alstn'
회원3.birthyear = 1993

print("{}:{}({},{},{})".format('회원1', 회원1.name, 회원1.account, 회원1.passwd, 회원1.birthyear))
print("{}:{}({},{},{})".format('회원2', 회원2.name, 회원2.account, 회원2.passwd, 회원2.birthyear))
print("{}:{}({},{},{})".format('회원3', 회원3.name, 회원3.account, 회원3.passwd, 회원3.birthyear))