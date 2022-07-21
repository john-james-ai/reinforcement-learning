#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Reinforcement Learning                                                              #
# Version    : 0.1.0                                                                               #
# Filename   : \policy.py                                                                          #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/reinforcement-learning                             #
# ------------------------------------------------------------------------------------------------ #
# Created    : Friday July 15th 2022 08:28:29 pm                                                   #
# Modified   : Friday July 15th 2022 11:09:40 pm                                                   #
# ------------------------------------------------------------------------------------------------ #
# License    : BSD 3-clause "New" or "Revised" License                                             #
# Copyright  : (c) 2022 John James                                                                 #
# ================================================================================================ #
"""Policy module that maps states and rewards to actions."""
import numpy as np
import logging

# ------------------------------------------------------------------------------------------------ #
logger = logging.getLogger(__name__)
# ------------------------------------------------------------------------------------------------ #


class PolicyMapping:
    """Defines a mapping from states to probabilities of selecting each possible action."""

    id: int
    state: np.array
    reward: float
    action: np.array
    
