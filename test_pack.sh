#!/bin/sh

zip -q -r amiyabot-arknights-hsyhhssyy-quick-action-1.2.zip *
rm -rf ../../amiya-bot-v6/plugins/amiyabot-arknights-hsyhhssyy-quick-action-1_2
mv amiyabot-arknights-hsyhhssyy-quick-action-1.2.zip ../../amiya-bot-v6/plugins/
docker restart amiya-bot 