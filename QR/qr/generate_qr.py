import qrcode

url = "https://sakadanissay.github.io/chiefbank/"

qr = qrcode.make(url)
qr.save("chief_mobile_bank_qr.png")

print("ONE QR with Android + iOS links created")

