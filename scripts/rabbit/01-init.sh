#!/bin/sh

# https://www.rabbitmq.com/access-control.html
# https://stackoverflow.com/questions/42003640/how-to-configure-rabbitmq-config-inside-docker-containers

( rabbitmqctl wait --timeout 60 $RABBITMQ_PID_FILE ; \
rabbitmqctl add_user $RABBITMQ_USER $RABBITMQ_PASSWORD 2>/dev/null ; \
rabbitmqctl set_user_tags $RABBITMQ_USER administrator ; \
rabbitmqctl set_permissions -p $RABBITMQ_VHOST $RABBITMQ_USER  ".*" ".*" ".*" ; \
rabbitmqctl add_vhost $RABBITMQ_VHOST ; \
rabbitmq-plugins enable rabbitmq_management ; \
) &

rabbitmq-server $@