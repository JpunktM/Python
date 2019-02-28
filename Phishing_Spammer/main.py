import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + "!@#§$%&*"
random.seed = (os.urandom(1024))

url = 'https://tq2afbm1.apps.lair.io/rbaccess/home/settings/includes/post_log.php'
data_username = 'gs_email'
data_password = 'gs_password'

first_names = json.loads(open('first_names.json').read())
last_names = json.loads(open('last_names.json').read())
mail_providers = json.loads(open('mail_providers.json').read())

random.shuffle(first_names)

for fname in first_names:

    extra = ''.join(random.choice(string.digits) for i in range(int(random.choice([0,1,2,3,4,5,6]))))

    name_extra = ''.join('' + str(random.choice(last_names)) + extra)

    username = fname + random.choice(['','.','-']) + name_extra + '@' + str(random.choice(mail_providers))
    password = ''.join(random.choice(chars) for i in range(int(random.choice([8,9,10,11,12,13,14,15,16]))))

    requests.post(url, allow_redirects=False, data={data_username: username, data_password: password})

    print('Sending username ' + username + ' and password ' + password + '')