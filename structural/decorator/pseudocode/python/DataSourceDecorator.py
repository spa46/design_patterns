from DataSource import DataSource

class DataSourceDecorator(DataSource):
  def __init__(self, source: DataSource) -> None:
    wrappee = source

  def writeData(self, data):
    wrappee.writeData(data)

  def readData(self):
    return wrappee.readData()