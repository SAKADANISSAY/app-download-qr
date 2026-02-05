import qrcode

url = "https://chiefbankcspp-app.github.io/chiefbankapp/QR"

qr = qrcode.make(url)
qr.save("chief_mobile_bank_qr.png")

print("ONE QR with Android + iOS links created")


