from VideoConverter import VideoConverter 

if __name__ == '__main__':
    converter = VideoConverter()
    mp4 = converter.convert('sample.ogg', 'mp4')
    # mp4.save()
