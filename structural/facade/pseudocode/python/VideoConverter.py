from VideoSource import VideoFile, OggCompressionCodec, MPEG4CompressionCodec, CodecFactory, BitrateReader, AudioMixer

class VideoConverter():
    def convert(self, filename, format):
        file = VideoFile(filename)
        sourceCodec = CodecFactory().extract(file)
        s = CodecFactory().extract(file)
        if format == 'mp4':
            destinationCodec = MPEG4CompressionCodec()
        else:
            destinationCodec = OggCompressionCodec()

        buffer = BitrateReader().read(filename, sourceCodec)
        result = BitrateReader().convert(buffer, destinationCodec)
        result = AudioMixer().fix(result)
