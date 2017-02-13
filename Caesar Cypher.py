def Main ():
#Create a dictionary with all the numbers and characters that we want 
#Letter to code
    L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ",range(63)))
#Code to letter
    I2L = dict(zip(range(63),"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 "))

#Get the message string and the key from the user
    plaintext = input("Enter a message to encode:")
    key = int(input("Enter a value for the key:"))
#Encode the message
    ciphertext = ""
    for c in plaintext:
                if c.isalpha():
                    ciphertext += I2L[ (L2I[c] + key)%63 ]
                else:
                    ciphertext += c
#Print out the encoded message                    
    print ("Ecrypted:" ,ciphertext,",", key)
    Main ()
    

