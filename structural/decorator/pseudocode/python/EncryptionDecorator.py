from DataSourceDecorator import DataSourceDecorator

import rsa
publicKey, privateKey = rsa.newkeys(512)

class EncryptionDecorator(DataSourceDecorator):
  

  def writeData(self, data):
    print(rsa.encrypt(data.encode(), publicKey))

  def readData(self):
    pass