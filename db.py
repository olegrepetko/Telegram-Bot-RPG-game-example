#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

client = MongoClient("mongodb+srv://game:iyU5V8PleOHLYZl8@suslon-jtinu.mongodb.net/test?retryWrites=true&w=majority")

db = client['game']


