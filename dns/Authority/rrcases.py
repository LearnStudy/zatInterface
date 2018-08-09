#coding ==utf-8
import pytest

class Rrcases:

    def addRr(self):
        pass

    def modifyRr(self):
        pass

    def deleteRr(self):
        pass

    @pytest.fixture(scope=function)
    def deleteAll(self):
        pass

class shareZoneRr:

    def addRr(self):
        pass

    def modifyRr(self):
        pass

    def deleteRr(self):
        pass

    @pytest.fixture(scope=function)
    def deleteAll(self):
        pass

class shareRr:

    @pytest.fixture(scope=function)
    def deleteAll(self):
        pass
    def addRr(self):
        pass

    def modifyRr(self):
        pass

    def deleteRr(self):
        pass