#!/bin/bash

#clean sample code
cd plugin/ && rm -rf SamplePlugin && cd ..
rm init/test.py init/loggercfg.py

#prepare DB
cp DB\ -\ clean.db DB.db

#download plugin & extract
cd plugin/ && wget https://bitbucket.org/maxisoft/maxivote/downloads/packed_plugin.zip && unzip packed_plugin.zip && cd ..
