#!/bin/bash

package="$1"
name="$(basename ${package} .deb)"

dpkg-deb -x "$package" "$name"
dpkg-deb --control "$package" "$name"/DEBIAN
sed -i -- 's/libappindicator3-1/libayatana-appindicator3-1/g' ./"$name"/DEBIAN/control
new="${name}-debian.deb"
dpkg -b "$name" "$new" 
rm -rf "$name"
sudo apt install ./"$new"
