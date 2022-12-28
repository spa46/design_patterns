from DataSource import DataSource

class FileDataSource(DataSource):
  def __init__(self, filename):
    self.filename = filename

  def writeData(self, data):
    print(data)

  def readData(self):
    pass