import re

is_mobile_re = re.compile(
    r".*(ip(hone|od|ad)|mobile|androidtouch|opera m(ob|in)i|(android|chrome).+mobile)",
    re.IGNORECASE,
)


def get_is_mobil(http_user_agent):
    if http_user_agent is None:
        # Default to assuming desktop if no user-agent header is
        # present.
        return False
    return is_mobile_re.match(http_user_agent) is not None
