from ismobile.utils import get_is_mobil


def test_get_is_mobil_without_http_user_agent():
    assert get_is_mobil(None) is False


def test_get_is_mobil_with_http_user_agent():
    http_user_agent = (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) "
        "Version/12.1 Mobile/15E148 Safari/604.1"
    )
    assert get_is_mobil(http_user_agent) is True
