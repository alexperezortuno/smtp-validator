#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import re


def email_verificator(email: str = None, match_type: str = "email") -> bool:
    if email is None:
        return None

    match = {
        'email': '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
    }

    type = re.compile(match[match_type])
    response = type.match(email)

    if response is not None:
        return True

    return False