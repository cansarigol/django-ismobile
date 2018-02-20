import re
import tkinter as tk

def get_is_mobil(http_user_agent):
    is_mobile_re=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
    return is_mobile_re.match(http_user_agent) != None
