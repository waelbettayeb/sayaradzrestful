from abc import ABC, abstractmethod

class FileReader(ABC):
    """
    Reads a file and retrieves data from that file
    """

    @abstractmethod
    def get_file_data(self, file_path):
        pass

