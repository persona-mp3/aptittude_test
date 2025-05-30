# import zlib
#
# with open(".git/index", "rb") as f:
#     compressed = f.read()
#
# dcmp = zlib.decompress(compressed)
#
# with open("gitIndex", "wb") as f:
#     f.write(decompressed)
with open(".git/index", "rb") as f:
    magic = f.read(4)   # should be b'DIRC'
    version = int.from_bytes(f.read(4), 'big')
    entries = int.from_bytes(f.read(4), 'big')
    # Then loop over binary entries...
