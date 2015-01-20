#!/bin/bash


source env/bin/activate
celery worker --beat --app=worker:worker
