#!/bin/bash
ps -ef |grep manage.py |awk '{print $2}'|xargs kill -9
