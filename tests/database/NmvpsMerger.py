from lib.database.NmvpsMerger import *
from tests.my_base_test_case import BaseTestCase


class NmvpsMergerTests(BaseTestCase):

    def setUp(self):
        self.subject = NmvpsMerger()
        print("setup             class:NmvpsMergerTests")

    def tearDown(self):
        print("teardown          class:NmvpsMergerTests")

    def test_connection(self):
        self.subject.connect()

    def test_run_merge(self):
        self.subject.run_merge()