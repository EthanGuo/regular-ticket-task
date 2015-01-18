#!/bin/bash


source env/bin/activate
celery beat --app=worker:worker
