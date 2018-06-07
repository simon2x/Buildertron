# Buildertron

<img align="left" src="buildertron/buildertron.png?raw=true"/>

Buildertron is a front-end for kivy's buildozer script.

[![Build Status](https://travis-ci.org/swprojects/Buildertron.svg?branch=master)](https://travis-ci.org/swprojects/Buildertron)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


# SCREENSHOTS
<img align="center" src="resources/screenshots/main.png?raw=true"/>


# DOWNLOADS
`sudo pip3 install buildozer`


# FEATURES

- Load, configure and save your buildozer.spec files
- Run the buildozer `distclean, clean, build, deploy, serve, run` commands from the toolbar
- Preview your buildozer.spec file in the GUI
- Override the buildozer with your own including the `terminal` buildozer which is prepended to buildozer commands
- Include additional target names if you want to use modified targets
- Blacklist configuration keys which you don't want to save to the spec
- Substitute configuration keynames with custom (for potential backward/forward compatibility)
- Customise the saved spec layout
