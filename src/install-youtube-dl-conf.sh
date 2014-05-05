#!/usr/bin/env bash
mkdir ~/.config || true
cp youtube-dl.conf ~/.config/
pip install rfc3339 --pre
pip install oauth2client google-api-python-client
