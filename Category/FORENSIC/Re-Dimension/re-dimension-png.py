from binascii import crc32

with open("./dimas-profile-picture-A.png", "rb") as f:
    img = f.read()

ihdr_ofset = img.find(b'IHDR')

w = 600
h = 800
crc = b"\x49\x48\x44\x52" + w.to_bytes(4, "big") + h.to_bytes(4, "big") + b"\x08\x06\x00\x00\x00"
crc = crc32(crc)

with open("./result.png", "wb") as f:
    nimg = (crc.to_bytes(4, "big")).join([img[:29], img[29+4:]])
    nimg = (w.to_bytes(4,"big")).join([nimg[:ihdr_ofset+4], nimg[ihdr_ofset+4+4:]])
    nimg = (h.to_bytes(4,"big")).join([nimg[:ihdr_ofset+8], nimg[ihdr_ofset+8+4:]])
    f.write(nimg)
