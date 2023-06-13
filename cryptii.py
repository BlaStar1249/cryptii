# 20230613


## Transform

# 1. replace(find, replace)
def replace(txt, find, replace):
    skip = -1
    idx = -1
    encrypted = ""
    for s in txt:
        idx += 1
        if skip>=idx: #check
            continue
        if txt[idx:idx+len(find)]==find:
            encrypted += replace
            skip = idx+len(find)-1
        else:
            encrypted += s
    return encrypted

print(replace("hellwo World", "wo", "&&&"))


# 2. reverse(plain) char, line
def reverse(plain):
    decode = ""
    for s in plain:
        decode = s + decode
    return decode

print(reverse("!!ereht iH"))


# 3(ii) upper_case(plain)
def upper_case(plain):
    # converts into upper case
    upper_case = ""
    for s in plain:
        if 97 <= ord(s) <= 122:
            s = chr(ord(s)-32)
        upper_case += s
    return upper_case

print(upper_case("abcdefghiklmnopqrstuvwxyz"))


# 3(iii) capitalize(plain)
def capitalize(plain):
    flag = True
    str1 = ""
    for s in plain:
        if flag:
            if 97 <= ord(s) <= 122:
                s = chr(ord(s)-32)
        str1 += s
        flag = True if s==" " else False
    return str1

print(capitalize("The quick brown fox jumps over the lazy dog"))


# 3(iv) alternating_case(plain)
def alternating_case(plain, flag=True):
    str1 = ""
    for s in plain:
        if flag:
            if 65 <= ord(s) <= 90:
                s = chr(ord(s)+32)
            str1 += s
            flag = False
        else:
            if 97 <= ord(s) <= 122:
                s = chr(ord(s)-32)
            str1 += s
            flag = True
    return str1

print(alternating_case("The quick brown fox jumps over the lazy dog", False))


# 3(v) inverse_case(plain)

def inverse_case(plain):
    str1 = ""
    for s in plain:
        if 65 <= ord(s) <= 90:
            str1 += chr(ord(s)+32)
        elif 97 <= ord(s) <= 122:
            str1 += chr(ord(s)-32)
        else:
            str1 += s
    return str1

print(inverse_case("The quick brown fox jumps over the lazy dog"))


# decimal to others

# def decimal(num, base):
#     num, mod = divmod(num, base)
    
#     #         s_binary = str(mod) + s_binary
#     #     if len(s_binary) == 8:
#     #         binary += s_binary
#     #     else:
#     #         binary += "0"*(8-len(s_binary))+s_binary
#     # return binary

# decimal(120)



## Alphabets


# 1. morse_code(plain)

def morse(plain):
    plain = plain.upper()
    morse_code_chart = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
        ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
        ' ': '/'}
    encrypted = ""
    count = -1
    for s in plain:
        count += 1
        if s in morse_code_chart:
            encrypted += morse_code_chart[s]
            encrypted += " " if count!=len(plain) else ""
    return encrypted

print(morse("The quick brown fox jumps over the lazy dog"))
# .... . .-.. .-.. --- / .-- --- .-. .-.. -..


## Ciphers


# 2. caeser_cipher(plain, shift, alphabet="abcdefghijklmnopqrstuvwxyz")
def caeser(plain, shift=0, alphabet = "abcdefghijklmnopqrstuvwxyz"):
    alphabet = alphabet.lower()
    encrypted = ""
    length = len(alphabet)
    for s in plain:
        if s.lower() in alphabet:
            idx = (alphabet.index(s.lower())+shift) % length
            encrypted += alphabet[idx] if s in alphabet else alphabet[idx].upper()
        else:
            encrypted += s
    return encrypted

print(caeser("The quick brown fox jumps over the lazy dog", 4))


# 3. affine_cipher(txt, a, b, alphabet="abcdefghijklmnopqrstuvwxyz")
def affine_cipher(txt, a, b, alphabet="abcdefghijklmnopqrstuvwxyz"):
    """a*x + b (mod m)
    The value of a (slope) must be chosen such that it is coprime to the size of the alphabet"""
    length = len(alphabet)
    encrypted = ""
    coprime_flag = False
    for i in range(2, length+1):
        if a%i==0 and length%i==0:
            coprime_flag = True
            break
    if coprime_flag == False:
        for s in txt:
            if s.lower() in alphabet:
                idx = alphabet.find(s.lower())
                encrypted_idx = (a * idx + b) % length
                encrypted += alphabet[encrypted_idx] if s in alphabet else alphabet[encrypted_idx].upper()
            else:
                encrypted += s
    else:
        print("The value of a (slope) must be chosen such that it is coprime to the size of the alphabet")
    return encrypted

print(affine_cipher("The quick brown fox jumps over the lazy dog.", 3, 2))


# 4. ROT13(plain) # ROT5, ROT13, ROT18, ROT47
def ROT13(plain):
    shift = 13
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    length = len(alphabet)
    for s in plain:
        if s.lower() in alphabet:
            idx = (alphabet.index(s.lower())+shift) % length
            encrypted += alphabet[idx] if s in alphabet else alphabet[idx].upper()
        else:
            encrypted += s
    return encrypted

print(ROT13("The quick brown fox jumps over the lazy dog."))


# 5. A1Z26(txt)
def A1Z26(txt):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    txt = txt.lower()
    encrypted = ""
    idx = -1
    for s in txt:
        idx += 1
        if s in alphabet:
            alphabet_idx = str(alphabet.find(s)+1)
            encrypted += alphabet_idx
            encrypted += " " if len(txt)!=idx+1 else ""
    return encrypted

print(A1Z26("The quick brown fox jumps over the lazy dog."))


# 6. vigenere_cipher()


# ???7. bacon_cipher()
# problem with J and v, not matching with cryptii.com
def becon_cipher(txt, letter1 = "A", letter2 = "B"):
    txt = txt.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    _encrypted = ""
    encrypted = ""
    idx = -1
    for s in txt:
        idx += 1
        if s in alphabet:
            char_idx = alphabet.find(s)
            binary_idx = str(bin(char_idx))[2:]
            _encrypted += "0"*(5-len(binary_idx))+binary_idx
            _encrypted += " " if len(txt)!=idx+1 else ""
    for s in _encrypted:
        if s=="0":
            encrypted += letter1
        elif s=="1":
            encrypted += letter2
        else:
            encrypted += s
    return encrypted

print(becon_cipher("abcdefghijklmnopqrstuvwxyz"))


# 8. alphabetical_substitution(txt, plaintext_alphabet, ciphertext_alphabet)
def alphabetical_substitution(txt, plaintext_alphabet="abcdefghijklmnopqrstuvwxyz", ciphertext_alphabet="zyxwvutsrqponmlkjihgfedcba"):
    encrypted = ""
    for s in txt:
        if s.lower() in plaintext_alphabet:
            plain_idx = plaintext_alphabet.find(s.lower())
            encrypted += ciphertext_alphabet[plain_idx] if s in plaintext_alphabet else ciphertext_alphabet[plain_idx].upper()
        else:
            encrypted += s
    return encrypted

print(alphabetical_substitution("The quick brown fox jumps over the lazy dog."))


# 9. rail_fence_cipher(txt, key, offset)
# does not matches with cryptii.com
# didn't work with offset portion
def rail_fence_cipher(txt, key, offset=0):
    """Value of key must be greater than 1"""
    if key==1:
        return f"{txt}"
    row = dict()
    idx = -1
    encrypted = ""
    ring = [i for i in range(key)] + [i for i in range(key-2, 0, -1)]
    for i in range(key):
        row[i] = ""
    for s in txt:
        idx += 1
        row[ring[idx%(2*key-2)]] += s # zikzak
    # filling with "x"
    if idx%key!=0:
        end_key = idx%key
        for i in range(end_key+1, key):
            row[i] += "x"
    for i in range(key):
        encrypted += row[i]
    return encrypted

print(rail_fence_cipher("thankyouverymuch", 3))
# thankyouverymuch = tkvmhnyueyuhaorc


## Polybius square ciphers


# 1. polybius_square(txt, alp="abcdefghiklmnopqrstuvwxyz", row="12345",column="12345", sep="")
def polybius_square(txt, alp="abcdefghiklmnopqrstuvwxyz", row="12345",column="12345", sep=""):
    """"Alphabet must contain 25 english letters once except 'j'.
Each row and column must contain 5 characters"""
    if len(alp) != 25:
        raise ValueError("alphabet must contain 25 english letters once except 'j'")
    if len(row) != 5 and len(row) != 5:
        raise ValueError("each row and column must contain 5 characters")
    txt = txt.lower()
    encrypted = ""
    idx = -1
    for s in txt:
        idx += 1
        if s=="j":
            s="i"
        if s in alp:
            alphabet_idx = alp.find(s)
            row_idx, column_idx = divmod(alphabet_idx, 5)
            encrypted += row[row_idx]+column[column_idx]
            encrypted += sep if len(txt)!=idx+1 else ""
    return encrypted

print(polybius_square("The quick brown fox jumps over the lazy dog", sep = " "))

# decrypting
# polybius_list = [[""]*5 for i in range(5)]
# alphabet="abcdefghiklmnopqrstuvwxyz"
# alphabet_idx = -1
# for r in range(5):
#     for c in range(5):
#         alphabet_idx += 1
#         polybius_list[int(r)][int(c)] = alphabet[alphabet_idx]
# print(polybius_list)


# 2. ADFGX_cipher(txt, alp="abcdefghiklmnopqrstuvwxyz", key="key")
# Add an option which will provide an option to take input from the user. The program will remove the dublicate and also add the rest of the alphabet after that.
def ADFGX_cipher(txt, alp="abcdefghiklmnopqrstuvwxyz", key="key"):
    """"Alphabet must contain 25 english letters once except 'j'"""
    row = column = "ADFGX"
    key_dict = dict()
    if len(alp) != 25:
        raise ValueError("alphabet must contain 25 english letters once except 'j'")
    txt = txt.lower()
    encrypted = ""
    encrypted2 = ""
    encrypted3 = ""
    idx = -1
    for s in txt:
        idx += 1
        if s=="j":
            s="i"
        if s in alp:
            alphabet_idx = alp.find(s)
            row_idx, column_idx = divmod(alphabet_idx, 5)
            encrypted2 += row[row_idx] + column[column_idx]
    key_dict = {s: "" for s in key}
    idx = -1
    key_length = len(key)
    for s in encrypted2:
        idx += 1
        key_dict[key[idx%key_length]] += s
    # sort a dictionary by keys
    key_dict = dict(sorted(key_dict.items()))
    for d in key_dict:
        encrypted3 += key_dict[d]
    # insert " " after every 5 characters
    idx = 0
    length = len(encrypted3)
    for s in encrypted3:
        idx += 1
        encrypted += s
        encrypted += " " if idx%5==0 and idx!=length else ""
    return encrypted

print(ADFGX_cipher("The quick brown fox jumps over the lazy dog"))


# 3. bifid_cipher()


# 4. nihilist_cipher()


# 5. tap_code()


# 6. trifid_cipher()


## Encoding


# test
def base32(txt):
    txt = txt.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
    bin8 = ""
    bin5 = ""
    encrypted = ""
    for i in range(0, len(txt)//5):
        # take 5 byte
        # convert into ascii value & concatinate
        # convert into 8 byte
        # asign corresponding base32 table value
        chr5 = txt[i*5: i*5+5]
        for s in chr5:
            binary = str(bin(ord(s)))[2:]
            bin8 += "0"*(8-len(str(binary))) + binary
        for i in range(0, len(bin8)//5):
            bin5 = bin8[i*5: i*5+5]
            encrypted += alphabet[int(bin5, 2)]
    return encrypted

print(base32("The quick brown fox jumps over the lazy dog"))


# 1. base32()

# 2. base64()

# 3. ascii85()

# 4. baudot_code()

# 5. unicode_code_points()

# 6. URL_encoding()

# 7. punycode()

# 8. bootstring()

# 9. integer()


## Modern cryptography


# 1. block_cipher()

# 2. RC4()

# 3. hash_function()

# 4. HMAC()


## Transliteration

# 20230531
def _transliterate_BtoE(txt):
    """1. Follow instructions strictly.
2. The purpose of this programme is not to transliterate but to encrypt text in a special format.
3. Will be inserted "o" to separate two consonents and to ensure that they are not compound consonent.
4. Don't use foreign character (if you do so it will appear into this format `<text>`). It should remain unchanged.
5. "`": <1> forcefully written short_vowel will be converted and followed by accute(`), <2> literally accute (`) will be converted into double "`", <3> "." will be converted to ".`" <4> (not applicable) "`<text>`" to keep text unchanged. Ex. "`<সোমবার>`"
6. In case of Bangla to English transliteration {"।":".", "...": "..." , ".": ".`"} will be changed this way.
While transliterating from Bangla into English if any text is written in exactly "`<text>`" format then the word will remain unchanged. Vice versa."""
# ======================================================================================================
    vowel_BtoE = {'অ': 'o', 'আ': 'a', 'ই': 'i', 'ঈ': 'I', 'উ': 'u', 'ঊ': 'U', 'ঋ': 'rri', 'এ': 'e', 'ঐ': 'OI', 'ও': 'O', 'ঔ': 'OU'}
    short_vowel_BtoE = {'া': 'a', 'ি': 'i', 'ী': 'I', 'ু': 'u', 'ূ': 'U', 'ৃ': 'rri', 'ে': 'e', 'ৈ': 'OI', 'ো': 'O', 'ৌ': 'OU'}
    consonent_BtoE = {'ক': 'k', 'খ': 'kh', 'গ': 'g', 'ঘ': 'gh', 'ঙ': 'Ng', 'চ': 'c', 'ছ': 'ch', 'জ': 'j', 'ঝ': 'jh', 'ঞ': 'NG', 'ট': 'T', 'ঠ': 'Th', 'ড': 'D', 'ঢ': 'Dh', 'ণ': 'N', 'ত': 't', 'থ': 'th', 'দ': 'd', 'ধ': 'dh', 'ন': 'n', 'প': 'p', 'ফ': 'f', 'ব': 'b', 'ভ': 'v', 'ম': 'm', 'য': 'z', 'র': 'r', 'ল': 'l', 'শ': 'sh', 'ষ': 'Sh', 'স': 's', 'হ': 'h', 'ড়': 'R', 'ঢ়': 'Rh', 'য়': 'y', 'ৎ': 'TH', 'ং': 'ng', 'ঃ': ':`', 'ঁ': 'qq', '্': 'hs'} # "র"+chr(2509)+"ক", "ক"+chr(2509)+"য", "জ"+chr(2509)+"ব" # র্ক ক্য জ্ব # rrk kZ jw
    special_consonent = "কখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমযরলশষসহড়ঢ়য়"
    number_BtoE = {'০': '0', '১': '1', '২': '2', '৩': '3', '৪': '4', '৫': '5', '৬': '6', '৭': '7', '৮': '8', '৯': '9'}
    # word_separators = "`~!@#$%^&*()-=+[{]}\\|।;:'\",.<>/?"
# =====================================================================================================
    idx = -1
    skip = -1
    unchange_flag = False
    encrypt = ""
# =====================================================================================================
    for s in txt:
        idx += 1
        # some special case and feature
        if True:
            if idx<=skip: # skip iteration
                continue
        # if s has vowel
        if s in vowel_BtoE or s in short_vowel_BtoE:
            if s in vowel_BtoE:
                encrypt += vowel_BtoE[txt[idx]]
            else:
                encrypt += short_vowel_BtoE[txt[idx]]
                if txt[idx-1] in short_vowel_BtoE:
                    encrypt += "`"
        # if s has consonent
        elif s in consonent_BtoE:
            if idx!=0 and txt[idx-1] in special_consonent and txt[idx] in special_consonent:
                encrypt += "o" # separates two consonents
            if len(txt)-1>=idx+1 and txt[idx+1]==chr(2509):
                # special characters
                if txt[idx:idx+2]=="র"+chr(2509):
                    encrypt += "rr"
                    skip = idx+1 
                elif len(txt)-1>=idx+2 and txt[idx+1:idx+3]==chr(2509)+"য":
                    encrypt += consonent_BtoE[txt[idx]]+"Z"
                    skip = idx+2
                elif len(txt)-1>=idx+2 and txt[idx+1:idx+3]==chr(2509)+"ব":
                    encrypt += consonent_BtoE[idx]+"w"
                    skip = idx+2
                elif txt[idx:idx+3]=="ক্ষ":
                    encrypt += "kkh"
                    skip = idx+2
                elif txt[idx:idx+3]=="জ্ঞ":
                    encrypt += "gg"
                    skip = idx+2
                # normal compound consonent
                elif len(txt)-1>=idx+2 and txt[idx] in special_consonent and txt[idx+2] in special_consonent:
                    encrypt += consonent_BtoE[txt[idx]]
                    skip = idx+1
                else: # weather 'hs' is the last character or 'hs' is followed by any character but consonent.
                    if txt[idx] in special_consonent:
                        encrypt += "o" # need to vidualise
                    encrypt += consonent_BtoE[txt[idx]]
            else:
                encrypt += consonent_BtoE[txt[idx]]
        # if variable s is neither vowel nor consonent
        else:
            if s=="।": # check
                encrypt += "."
                if txt[idx+1]=="`":
                    encrypt += "।"
                    skip = idx+1
            elif 65<=ord(s)<=90 or 97<=ord(s)<=122: # check
                if not (65<=ord(txt[idx-1])<=90 or 97<=ord(txt[idx-1])<=122):
                    encrypt += "`<"
                encrypt += s
                if not (65<=ord(txt[idx+1])<=90 or 97<=ord(txt[idx+1])<=122):
                    encrypt += ">`"
            elif s in number_BtoE:
                encrypt += number_BtoE[txt[idx]]
            else:
                encrypt += s
    return encrypt

print(_transliterate_BtoE("""
`<প্রবাদ>` a b cde...  
"""))


# 20230531
def _transliterate_EtoB(txt):
    """1. Follow instructions strictly.
2. The purpose of this programme is not to transliterate but to encrypt text in a special format.
3. Must use "o" to separate two consonents and to ensure that they are not compound consonent.
4. Don't use foreign character (if you do so it will appear into this format `<text>`). It should remain unchanged. # May create problem with short_vowel or "hs"
5. use of "`": <1> forcefully write short_vowel against rules, <2> double "`" literally types "`", <3> ".`" types literally "." <4> "`<text>` to keep text unchanged. Ex. "`<Monday>`"
6. Forcefully type short vowel by writing the vowel followed by an accute (`) sign
7. In case of Bangla to English transliteration {".":"।", "...":"..." , ".`": "."} will be changed this way.
8. While transliterating English into Bangla if any text is written in exactly `< unchanged text >` format then the word will remain unchanged."""
# =====================================================================================================
    vowel_EtoB = {'o': 'অ', 'a': 'আ', 'i': 'ই', 'I': 'ঈ', 'u': 'উ', 'U': 'ঊ', 'rri': 'ঋ', 'e': 'এ', 'OI': 'ঐ', 'O': 'ও', 'OU': 'ঔ'}
    short_vowel_EtoB = {'o': '', 'a': 'া', 'i': 'ি', 'I': 'ী', 'u': 'ু', 'U': 'ূ', 'rri': 'ৃ', 'e': 'ে', 'OI': 'ৈ', 'O': 'ো', 'OU': 'ৌ'}
    consonent_EtoB = {'k': 'ক', 'kh': 'খ', 'g': 'গ', 'gh': 'ঘ', 'Ng': 'ঙ', 'c': 'চ', 'ch': 'ছ', 'j': 'জ', 'jh': 'ঝ', 'NG': 'ঞ', 'T': 'ট', 'Th': 'ঠ', 'D': 'ড', 'Dh': 'ঢ', 'N': 'ণ', 't': 'ত', 'th': 'থ', 'd': 'দ', 'dh': 'ধ', 'n': 'ন', 'p': 'প', 'f': 'ফ', 'b': 'ব', 'v': 'ভ', 'm': 'ম', 'z': 'য', 'r': 'র', 'l': 'ল', 'sh': 'শ', 'Sh': 'ষ', 's': 'স', 'h': 'হ', 'R': 'ড়', 'Rh': 'ঢ়', 'y': 'য়', 'TH': 'ৎ', 'ng': 'ং', ":`": "ঃ", 'qq': 'ঁ', 'w':'ব', 'Z': 'য', 'kkh': 'ক্ষ', 'gg': 'জ্ঞ', 'hs': chr(2509)} # 'ShN': 'ষ্ণ'
    special_consonent = "কখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমযরলশষসহড়ঢ়য়"
    number_EtoB = {'0': '০', '1': '১', '2': '২', '3': '৩', '4': '৪', '5': '৫', '6': '৬', '7': '৭', '8': '৮', '9': '৯', }
    word_separators = " `~!@#$%^&*()-=+[{]}\\|।;:'\",.<>/?"
# ======================================================================================================
    idx = -1
    word_idx = -1
    skip = -1
    short_vowel_flag = False
    unchange_flag = False
    encrypt = ""
# ======================================================================================================
    for s in txt:
        idx += 1
        word_idx += 1
        # some special case and feature
        if True:
            if skip>=idx:
                continue
            if unchange_flag: # check
                if s==">":
                    if txt[idx+1]=="`":
                        skip = idx+1
                        unchange_flag = False
                        continue
                    else:
                        encrypt += s
                if s!="`":
                    encrypt += s
                continue
        # vowel detection
        if txt[idx: idx+3] in vowel_EtoB or txt[idx: idx+2] in vowel_EtoB or txt[idx] in vowel_EtoB:
            if encrypt:
                short_vowel_flag = word_idx!=0 and encrypt[-1] in special_consonent
            if txt[idx: idx+3] in vowel_EtoB: # "rri"
                skip = idx+2
                if short_vowel_flag or txt[idx+3]=="`":
                    encrypt += short_vowel_EtoB[idx: idx+3]
                    skip += 1
                else:
                    encrypt += vowel_EtoB[idx: idx+3]
            elif txt[idx: idx+2] in vowel_EtoB:
                skip = idx+1
                if short_vowel_flag or txt[idx+2]=="`":
                    encrypt += short_vowel_EtoB[txt[idx:idx+2]]
                    skip += 1
                else:
                    encrypt += vowel_EtoB[txt[idx:idx+2]]
            else:
                encrypt += short_vowel_EtoB[txt[idx]] if short_vowel_flag or txt[idx+1]=="`" else vowel_EtoB[txt[idx]]
        # consonent detection
        elif txt[idx: idx+3] in consonent_EtoB or txt[idx: idx+2] in consonent_EtoB or txt[idx] in consonent_EtoB:
            if word_idx!=0 and encrypt[-1] in special_consonent and txt[idx-1]!="o": # check: "word_idx!=0 and " needed?
                encrypt += chr(2509)
            if txt[idx: idx+3] in consonent_EtoB: # 'kkh'
                encrypt += consonent_EtoB[txt[idx: idx+3]]
                skip = idx+2
            elif txt[idx: idx+2] in consonent_EtoB:
                encrypt += consonent_EtoB[txt[idx: idx+2]]
                skip = idx+1
            else:
                encrypt += consonent_EtoB[txt[idx]]
        # other character detection
        else:
            if s==".": # also apply in English to Bangla literation
                if txt[idx:idx+3]=="...":
                    encrypt += txt[idx:idx+3]
                    skip = idx+2
                elif txt[idx:idx+2]==".`":
                    encrypt += "."
                    skip = idx+1
                else:
                    word_idx = 0
                    encrypt += "।"
            # accute case
            # check
            elif s=="`": # check: and txt[idx+1]!="`" needed?
                if txt[idx+1]=="`":
                    encrypt += "`"
                    skip = idx+1
                elif txt[idx+1]=="<":
                    unchange_flag = True
                    skip = idx+1
            elif s in word_separators:
                word_idx = 0
                encrypt += s
            elif s in number_EtoB:
                encrypt += number_EtoB[txt[idx]] # s=txt[idx]
            else:
                encrypt += s
    return encrypt

print(_transliterate_EtoB("""
`<Monday>`
amader desher nam bangladesh
"""))
