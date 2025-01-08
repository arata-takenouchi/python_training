import os
import sys

import flask

import roboter.contlorller.conversation
# from roboter.contlorller import conversation

import settings

class MainError(Exception):
    pass

def main():
    try:
        roboter.contlorller.conversation.talk_about_restaulant
    except Exception as e:
        print(e)
    raise MainError('error')

x = [(i, x) for i in [1,2,3,4] for x in [1,2,3]]

d = {'key1': 'value1', 'key2', 'value2'}
if 'key1' in d:
    print('test')

if 'key1' in d.keys():
    print('test')

for name, count in ranking.items():
    print(name, count)

if __name__ == 'main':
    main()