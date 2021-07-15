def myemail_info(email):
    if '@' not in email:
        result = None
    else:
        result = email.split("@")
        result = tuple(result)
    return result


print(myemail_info('rbtkd912@naver.com'))
print(myemail_info('rbtkd912naver.com'))