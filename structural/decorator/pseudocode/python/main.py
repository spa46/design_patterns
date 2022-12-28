from FileDataSource import FileDataSource
from CompressionDecorator import CompressionDecorator
from EncryptionDecorator import EncryptionDecorator

data = 'name: Sea Son, address: Sky'

if __name__ == "__main__":
  source = FileDataSource("somefile.dat")
  source.writeData(data)

  # Compression
  print('Compress data')
  source = CompressionDecorator(source)
  source.writeData(data)
  print()

  # Encryption
  print('Encrypt data')
  source = EncryptionDecorator(source)
  source.writeData(data)
  print()