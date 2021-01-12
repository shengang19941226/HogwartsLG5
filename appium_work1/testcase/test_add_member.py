import pytest
from appium_work1.page.app import App

class TestAddMember:

    def setup_class(self):
        self.app = App()

    def teardown_class(self):
        self.app.quit()

    def test_add_member_success(self):
        pytest.assume(self.app.start().main().goto_contact().goto_add_member().manual_add_member().add_member('沈沈沈1','13913514468'))

if __name__ == '__main__':
        pytest.main(['test_add_member.py','-sq'])