#coding=utf-8

import smtplib
from email.mime.text import MIMEText

mail_to_list = ['ray.tan@corp.globalmarket.com', 'sugar.lin@corp.globalmarket.com', 'kale.lin@corp.globalmarket.com']

mail_host = 'smtp.globalmarket.com'
mail_user = 'ittest@corp.globalmarket.com'
mail_pwd = '111111'

def send_mail(to_list, subject, content):
    '''
    to_list: 发送目标
    subject: 邮件标题
    content: 邮件正文
    send_mail('xxx@xxx.com', 'subject', 'content')
    '''

    msg = MIMEText(content)
    msg['subject'] = subject
    msg['From'] = mail_user
    msg['To'] = ';'.join(to_list)

    try:

    	s = smtplib.SMTP()
    	s.connect(mail_host)
    	s.login(mail_user, mail_pwd)
    	s.sendmail(mail_user, to_list, msg.as_string())
    	s.close()

    	return True

    except Exception as ex:
    	print(ex)
    	return False