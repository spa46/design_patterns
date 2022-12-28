class VideoFile:
    def __init__(self, filename):
        pass

class OggCompressionCodec:
    pass

class MPEG4CompressionCodec:
    pass

class CodecFactory:
    def extract(self, file):
        pass

class BitrateReader:
    def read(self, filename, format):
        pass
    def convert(self, buffer, codec):
        pass

class AudioMixer:
    def fix(self, result):
        pass

