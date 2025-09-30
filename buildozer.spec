[app]
title = Cafe Virtual
package.name = cafevirtual
package.domain = org.cafe
source.dir = .
version = 1.0
requirements = python3,kivy
presplash.filename = logo.png
icon.filename = logo.png
orientation = portrait

[buildozer]
log_level = 2

[android]
api = 33
minapi = 21
android.accept_sdk_license = True
android.sdk_build_tools = 33.0.2

[python]
version = 3.10.0
