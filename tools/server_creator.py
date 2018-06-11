import smtplib


def server_creator(encryptation: str="smtp", server_name: str=None, server_port: str=None):
    # SMTP lib setup (use debug level for full output)
    if server_name is not None and server_port is not None:
        server = smtplib.SMTP(server_name, server_port)
    else:
        server = smtplib.SMTP()

    return {
        'a': lambda x: x * 5,
        'b': lambda x: x + 7,
        'c': lambda x: x - 2
    }[value](x)