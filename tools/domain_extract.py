import re


def domain_extract(email: str = None) -> str:
    if email is None:
        return False

    response = email.split("@")[1]

    if check_domain(response) is False:
        return False

    return response


def check_domain(domain: str) -> bool:
    reg_exp = "^(\w{3,}\.\w{2,})$"
    type = re.compile(reg_exp)
    response = type.match(domain)

    if response is not None:
        return True

    return False