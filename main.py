#!/usr/bin/env python3
import sqlite3
import time
import smtplib
import sys
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import traceback

# -------------------请修改以下部分的配置-------------------

# QQ号
qq = 1840686745

# 检测间隔时间(秒)
sleep_time = 60

# 邮箱服务器地址
mail_host = 'smtp.kokona.tech'
# SMTP端口
mail_port = 465
# SMTP是否使用SSL
mail_use_ssl = True
# 邮箱用户名
mail_user = 'suhui@kokona.tech'
# 邮箱密码(部分邮箱为授权码)
mail_pass = ''
# 邮件发送方邮箱地址
sender = 'suhui@kokona.tech'
# 邮件接受方邮箱地址
receivers = ['1840686745@qq.com', 'zzq1840686745@outlook.com']
# 邮件标题
mail_subject = '酷Q监测: 警告'
# 发件人昵称
mail_sender_nick = 'CoolQ错误监测系统'
# 邮件内容, 可以使用sprintf格式化占位符
mail_content = '警告: \n%d: %s'
# 邮件格式化占位符的对应参数, 以str保存, ele[1]代表检测到的错误信息
mail_para = '(qq, ele[1])'

# -------------------配置部分结束-------------------

# 数据库文件位置
file_loc = './data/%d/eventv2.db' % qq

# 版本
ver = 'V1.0.0'

print('CoolQ异常监视系统: %s' % ver)
print('提示: 请将此文件放于CQA/CQP.exe同文件夹下运行(非app文件夹!)')
print()
print('[INFO] QQ: %d' % qq)
print('[INFO] 监测间隔时间: %d 秒' % sleep_time)
print('[INFO] SMTP服务器: %s:%d' % (mail_host, mail_port))
print('[INFO] SMTP SSL: %s' % mail_use_ssl)
print('[INFO] SMTP 用户名: %s' % mail_user)
print('[INFO] SMTP 发送地址: %s' % sender)
print('[INFO] SMTP 收件人: %s' % receivers)
print('[INFO] 邮件发件人昵称: %s' % repr(mail_sender_nick))
print('[INFO] 邮件标题: %s' % repr(mail_subject))
print('[INFO] 邮件内容: %s' % repr(mail_content))
print('[INFO] 邮件内容参数: %s' % repr(mail_para))
print('[INFO] 开始监测')

# 获取当前最后一次日志的id
last_id = 0
try:
    last_id = sqlite3.connect(file_loc).cursor().execute('select id from event order by id desc ').fetchone()[0]
except sqlite3.OperationalError:
    print('[ERROR] 数据库连接错误')
    print(traceback.format_exc())
    print('[CRITICAL] 致命错误, 正在退出')
    sys.exit()


while True:
    time.sleep(sleep_time)
    conn = None
    try:
        conn = sqlite3.connect(file_loc)
    except sqlite3.OperationalError:
        print('[ERROR] 数据库连接错误')
        print(traceback.format_exc())
        continue
    new_id = conn.cursor().execute('select id from event order by id desc ').fetchone()[0]
    res = conn.cursor().execute('select type,content from event where id > ? and type = 1101', (last_id,)).fetchall()
    for ele in res:
        print("[INFO] 检测到酷Q异常: %s" % str(ele))
        message = MIMEText(mail_content % eval(mail_para), 'plain', 'utf-8')
        message['From'] = formataddr([Header(mail_sender_nick, 'utf-8').encode(), sender])
        message['To'] = ';'.join(receivers)
        message['Subject'] = Header(mail_subject, 'utf-8')
        try:
            if mail_use_ssl:
                smtpObj = smtplib.SMTP_SSL(mail_host, mail_port)
            else:
                smtpObj = smtplib.SMTP(mail_host, mail_port)
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            smtpObj.quit()
            print("[INFO] 邮件发送成功")
        except smtplib.SMTPException:
            print("[ERROR] 无法发送邮件")
            print(traceback.format_exc())
    last_id = new_id
