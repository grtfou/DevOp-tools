#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @date          20151030
"""
Configuration for gunicorn deploy
"""
import multiprocessing

bind = '127.0.0.1:9000'
workers = multiprocessing.cpu_count() * 2 + 1
