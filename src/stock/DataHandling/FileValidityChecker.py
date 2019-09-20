from abc import ABC, abstractmethod


class FileValidityChecker(ABC):

    @abstractmethod
    def check_validity(self, file):
        pass