#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Reinforcement Learning                                                              #
# Version    : 0.1.0                                                                               #
# Filename   : \markov_decision_process_finite.py                                                  #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/reinforcement-learning                             #
# ------------------------------------------------------------------------------------------------ #
# Created    : Saturday July 16th 2022 08:16:42 pm                                                 #
# Modified   : Tuesday July 19th 2022 03:31:46 pm                                                  #
# ------------------------------------------------------------------------------------------------ #
# License    : BSD 3-clause "New" or "Revised" License                                             #
# Copyright  : (c) 2022 John James                                                                 #
# ================================================================================================ #
"""Finite Markov Decision Process Module"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any
import logging
import numpy as np
# ------------------------------------------------------------------------------------------------ #
logger = logging.getLogger(__name__)
# ------------------------------------------------------------------------------------------------ #

class State:
    """State describes the current situation of the environment."""
    def __init__(self, state: Any, time: int) -> None:
        self._state = state
        self._time = time

    @property
    def time(self) -> int:
        return self._time

    @property
    def state(self) -> Any:
        return self._state

class Action:
    """How the agent changes the environment."""
    def __init__(self, action: Any, time: int) -> None:
        self._action = action
        self._time = time

    @property
    def time(self) -> int:
        return self._time

    @property
    def action(self) -> Any:
        return self._action

class Reaction:
    """The environment's response to an action."""
    def __init__(self, state: State, reward: float, time: int) -> None:
        self._state = state
        self._reward = reward
        self._time = time

    @property
    def state(self) -> State:
        return self._state

    @property
    def reward(self) -> float:
        return self._reward

    @property
    def time(self) -> int:
        return self._time

class Environment(ABC):
    """Abstract class defining the interface for the objects with which the Agent interacts."""
    def __init__(self, state: State) -> None:
        self._state = state
        self._reward = 0
        self._time = 0
        self._reaction = None

    @abstractmethod
    def act(self, action: Action) -> Reaction:
        pass





class Agent:
    """The learner / decision maker in the finite markov decision process."""

    def __init__(self, policy: Policy) -> None:
        self._policy = policy

    def get_action(self, state: State, reward: float) -> np.array:
        return self._policy.get_action(state, reward)

class Policy:
    """Relationship between states, actions, and rewards"""
    def __init__(self) -> None:
        pass

    def value(self, state: State)