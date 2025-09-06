#python script to reverse the encrypted text
def to_identity_map(a): 
    return ord(a) - 0x41

def from_identity_map(a): 
    return chr(a % 26 + 0x41)

def decrypt(m):
    c = '' 
    for i in range(len(m)): 
        ch = m[i] #storing the current character the counter is at in ch
        if not ch.isalpha(): #if ch is NOT an alphanumeric character (a letter)
            ech = ch #unchanged, we store the same value in ech
        else: #otherwise, if it's an alphanumeric character (a letter)
            chi = to_identity_map(ch)
            ech = from_identity_map(chi - i) 
        c += ech 
    return c 

encrypted_message = "DJF_CTA_SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL" #here is the encrypted message from the output.txt file
decrypted_message = decrypt(encrypted_message)

print(decrypted_message) #print the flag!
