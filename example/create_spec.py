# -*- coding:utf-8 -*-
from __future__ import print_function

import json


def handle_body_it(it_entries):
    for attr, value in it_entries:
        if attr == 'should':
            pass
        if attr == 'should_not':
            pass

def handle_body_its(its_entries):
    for attr, value in its_entries:
        if attr == ''

def handle_resource_body(resource_body):
    for attr, value in resource_body.items():
        if attr == 'it':
            handle_body_it(value)
        if attr == 'its':
            handle_body_its(value)


def handle_describe(describe):
    for d in describe:
        print("describe {type}({name}) do".format(type=d['resource-type'],name=d['resource-name']))
        handle_resource_body(d['resource-body'])
        print("end")


def handle_spec(spec):
    print("create spec file ./spec/HOSTNAME/{}_spec.rb".format(spec['spec-name']))
    handle_describe(spec['describe'])


def main():
    with open('specdb.json') as f:
        specdb = json.load(f)
        handle_spec(specdb['spec'])

if __name__ == '__main__':
    main()
