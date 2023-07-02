import pytest

params = {
    "DB_URL": "fake_DB_URL",
    "DB_USERNAME": "fake_DB_USERNAME",
    "DB_PASSWORD": "fake_DB_PASSWORD",
    "OK_MSG": "fake_OK_MSG",
    "NOK_MSG": "fake_NOK_MSG",
}


def fake_config(param: str):
    return params.get(param)


class TestDbHandler:
    @pytest.fixture
    def set_config(self, mocker):
        mocker.patch("decouple.config", fake_config)

    def test_connect_to_database(self, set_config):
        from src.db_handler import DbHandler

        handler = DbHandler()
        result = handler.connect_to_database()
        expected = (
            "I am connecting to fake_DB_URL as "
            "fake_DB_USERNAME with pass: fake_DB_PASSWORD..."
        )
        assert result == expected

    def test_show_msg_when_connected(self, set_config):
        from src.db_handler import DbHandler

        handler = DbHandler()
        result = handler.show_msg_when_connected()
        expected = "fake_OK_MSG"
        assert result == expected

    def test_show_msg_when_interrupted(self, set_config):
        from src.db_handler import DbHandler

        handler = DbHandler()
        result = handler.show_msg_when_interrputed()
        expected = "fake_NOK_MSG"
        assert result == expected
