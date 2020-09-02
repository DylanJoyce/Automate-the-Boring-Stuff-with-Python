#!/usr/bin/env python

import random

messages = ['It is certain.', 'It is uncertain.', 'Yes, definitely.', 'OK', 'Noooooooo']

print(messages[random.randint(0, len(messages) - 1)])