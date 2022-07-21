#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Reinforcement Learning                                                              #
# Version    : 0.1.0                                                                               #
# Filename   : \agent.py                                                                           #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/reinforcement-learning                             #
# ------------------------------------------------------------------------------------------------ #
# Created    : Friday July 15th 2022 08:26:38 pm                                                   #
# Modified   : Saturday July 16th 2022 12:03:23 am                                                 #
# ------------------------------------------------------------------------------------------------ #
# License    : BSD 3-clause "New" or "Revised" License                                             #
# Copyright  : (c) 2022 John James                                                                 #
# ================================================================================================ #
"""Agent, or learner/decision maker of the finite markov decision process."""
import logging

from policy import Policy

# ------------------------------------------------------------------------------------------------ #
logger = logging.getLogger(__name__)
# ------------------------------------------------------------------------------------------------ #

class Agent:
    """The learner / decision maker in the finite markov decision process."""

    def __init__(self, policy: Policy) -> None:
        self._policy = policy
