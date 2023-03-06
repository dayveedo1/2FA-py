import time
import pyotp
import qrcode

#Generate the key: a random value(should be a secret)
#key = pyotp.random_base32()
#print(key)

key = "Thereisnosuchthingasalifebetterthanyours"



#One-Time Password
# Every 30 seconds, we get a new otp
totp = pyotp.TOTP(key)
#print(totp.now())                                          #uncomment


#input_code = input("Enter 2FA code: ")                     #uncomment
#print(totp.verify(input_code))                              #verify that input is same as code generated, uncomment



# Counter-Based Password
# Values doesn't change, will always remain the same base on the at()
counter = 0
hotp = pyotp.HOTP(key)
#print(hotp.at(counter))                                            #uncomment


for i in range(5):
    #print(hotp.verify(input("Enter OTP code: "), counter))          #verify that input is same as code generated
    counter += 1

# QR Code OTP
uri = pyotp.totp.TOTP(key).provisioning_uri(name="dave47",
                                            issuer_name="Cactus")           #works with Google Authenticator app
print(uri)
qrcode.make(uri).save("totp.png")                                           #qrcode generated