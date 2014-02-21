# -*- coding:utf-8 -*-
from __future__ import print_function

import json


def flatten(structure, key="", path="", flattened=None):
    if flattened is None:
        flattened = {}
    if type(structure) is not dict:
        flattened[((path + " ") if path else "") + key] = structure
    else:
        for new_key, value in structure.items():
            flatten(value, new_key, path + " " + key, flattened)
    return flattened


def handle_it(it_entries):
    for e in it_entries:
        print("    it {{ {e} }}".format(e=flatten(e)))


def handle_its(its_entries):
    for e in its_entries:
        print("    its ({e[param-name]}) {{ {body} }}".format(e=e, body=flatten(e['body'])))


def handle_resource_body(resource_body):
    for item in resource_body:
        if 'it' in item.keys():
            handle_it(item['it'])
        if 'its' in item.keys():
            handle_its(item['its'])


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
