#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from config import PATH_SQLITE_DB
from app import database
from app.models.entry import Entry

# init database if don't exist
if not os.path.exists(PATH_SQLITE_DB):
    database.create_tables([Entry], safe=True)
