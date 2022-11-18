#!/bin/sh

zip -q -r amiyabot-arknights-hsyhhssyy-quick-action-1.1.zip *
rm -rf ../../amiya-bot-v6/plugins/amiyabot-arknights-hsyhhssyy-quick-action-1_1
mv amiyabot-arknights-hsyhhssyy-quick-action-1.1.zip ../../amiya-bot-v6/plugins/
docker restart amiya-bot 