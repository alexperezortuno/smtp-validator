import dns.resolver
from dns.resolver import NoAnswer
import logging
import socket
import smtplib
from smtplib import SMTPServerDisconnected, SMTPSenderRefused
from tools import email_verificator, domain_extract, MxRecord, Log

log = Log()

emailToVerify = "alexperezortuno@gmail.com"

server_port = None
server_name = None
server_encryption = 'smtp'
user_name = None
password = None
debug_level = 0

email_verify = email_verificator(emailToVerify)

if email_verify is False:
    log.error("Email invalid" + emailToVerify)
    raise ValueError("Email invalid")

domain = domain_extract(emailToVerify) if server_name is None else server_name

try:
    records = dns.resolver.query(domain, 'MX')
except NoAnswer as e:
    log.error(message=e)
    raise ValueError("Error response: {message}".format(message=e))

mx_record = MxRecord()

for mx in records:
    mx_record.add(str(mx.preference), str(mx.exchange))

if mx_record is not None:
    mx_records = mx_record.get()

    # Get local server hostname
    host = socket.gethostname()

    log.info("connecting...")

    try:
        # SMTP lib setup (use debug level for full output)
        if server_name is not None and server_port is not None:
            server = smtplib.SMTP(server_name, server_port)
        else:
            server = smtplib.SMTP()

        server.set_debuglevel(debug_level)
    except Exception as e:
        log.error("Error: {message}".format(message=e))
        raise ValueError("Connecting error with the server")

    for mx in mx_records:
        try:
            server.connect(mx_records[mx])
            server.helo(host)
            server.mail('alexperezortuno@gmail.com')
            code, message = server.rcpt(str(emailToVerify))
            log.info(message="{c} {m}".format(c=code, m=message))
            server.quit()
        except (SMTPServerDisconnected, SMTPSenderRefused) as e:
            print(e)
        except Exception as e:
            print(e)

    server = smtplib.SMTP(SERVER_NAME, SERVER_PORT)
    print('connected..')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(USER_NAME, PASSWORD)
    text = 'TEST 123'
    server.sendmail('whoever@whatever.com', 'another@hatever.com', text)
    server.quit()
