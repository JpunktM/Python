import os
import random
import string
import json

random.seed = (os.urandom(1024))

first_names = json.loads(open('first_names.json').read())
last_names = json.loads(open('last_names.json').read())
mail_providers = json.loads(open('mail_providers.json').read())
generated_mail = open("generated_mails.txt", "a")


while True:
    random.shuffle(first_names)
    for fname in first_names:

        extra = ''.join(random.choice(string.digits) for i in range(int(random.choice([0,1,2,3,4,5,6]))))

        name_extra = ''.join(str(random.choice(last_names)) + extra)

        username = fname + random.choice(['','.','-']) + name_extra + '@' + str(random.choice(mail_providers))

        generated_mail.write(username + '\r')