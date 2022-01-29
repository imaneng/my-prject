from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
import os, requests

url = ''

@dataclass
class Media:
    name : str
    location : str
    rating : float

    
class MediaFile(ABC):

    @abstractmethod
    def file_type_A(self):
        pass

    @abstractmethod
    def file_type_B(self):
        pass




class FileA(MediaFile):
    def fun(filename):
        filename = os.path.basename(filename)
        return filename




class FileB(MediaFile):
    def fun2(url):
        filename = requests.get(url)
        return filename






def play (file:MediaFile):

    file_type_a = file.file_type_A()
    file_type_b = file .file_type_B()


