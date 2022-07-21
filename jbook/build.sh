#!/bin/sh
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Reinforcement Learning                                                              #
# Version    : 0.1.0                                                                               #
# Filename   : \build.sh                                                                           #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/reinforcement-learning                             #
# ------------------------------------------------------------------------------------------------ #
# Created    : Wednesday July 13th 2022 12:59:41 pm                                                #
# Modified   : Wednesday July 13th 2022 01:37:36 pm                                                #
# ------------------------------------------------------------------------------------------------ #
# License    : BSD 3-clause "New" or "Revised" License                                             #
# Copyright  : (c) 2022 John James                                                                 #
# ================================================================================================ #

# Delete prior build
#echo "Removing prior jupyter-book build artifacts..."
#rm -r jbook/_build/
#Prepare notebook display customizations
echo "Preparing notebook tags..."
python jbook/prep_notebooks.py
# Rebuilds the book
echo "Building book..."
jb build jbook/
# Commit book to gh-pages
echo "Committing changes to github pages..."
ghp-import -o -n -p -f jbook/_build/html
