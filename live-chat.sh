#!/usr/bin/env bash
matrixcli -c live-matrixcli-cfg.py listen | sed -u 's/./&\n/36' >live-stream-chat.log
