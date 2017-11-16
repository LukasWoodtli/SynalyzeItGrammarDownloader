#!/usr/bin/env python

from lxml import etree
import urllib
import os

script_folder = os.path.abspath(os.path.split(__file__)[0])

xml_url = 'http://www.synalysis.net/formats.xml'

output_dir = script_folder + '/formats/'

root = etree.parse(xml_url)

grammar_urls = root.xpath("/formats/format/grammar/@url")

# Check if output dir exists, create it otherwise
d = os.path.dirname(output_dir)
if not os.path.exists(d):
    os.makedirs(d)

num_gramars = len(grammar_urls)
for i in range(num_gramars):
    print "Loading grammar %i of %i" % (i + 1, num_gramars)
    file_name = grammar_urls[i].split('/')[-1]
    file_name = output_dir + file_name
    urllib.urlretrieve(grammar_urls[i], file_name)
