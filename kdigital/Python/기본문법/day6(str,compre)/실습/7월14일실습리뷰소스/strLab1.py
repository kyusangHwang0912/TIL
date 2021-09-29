def myemail_info(email):

    s = email

    if "@" in s:
        s2 = s.split("@")
        tu = tuple(s2)
        print(tu)
    else:
        print("none")


myemail_info('jh3672@gmail.com')
myemail_info('vdssnaver.com')

