from DataSourceDecorator import DataSourceDecorator

import zlib

class CompressionDecorator(DataSourceDecorator):
  def __init__(self, filename):
    self.filename = filename

  def writeData(self, data):
    print(zlib.compress(bytearray(data, encoding='utf-8'), -1))

  def readData(self):
    pass