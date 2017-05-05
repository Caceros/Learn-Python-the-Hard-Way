from nose.tools import *
import my_module

def setup():
    print('SETUP!')


def teardown():
    print("Tear Down!")


def test_basic():
    print('I Ran!')