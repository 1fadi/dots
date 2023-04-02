#!/bin/bash


if [ "$(ip link show wlan0 | grep -c UP)" -eq 1 ]; then
	sudo ip link set wlan0 down
	notify-send "WiFi off"
else
	sudo ip link set wlan0 up
	notify-send "WiFi on"
fi
