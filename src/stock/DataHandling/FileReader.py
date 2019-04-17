from abc import ABC, abstractmethod


class FileReader(ABC):
    """
    Reads a file and retrieves data from that file
    """
    def __init__(self, file_validator):
        self.file_validator = file_validator

    @abstractmethod
    def get_file_data(self, file_path):
        pass

