#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Reinforcement Learning                                                              #
# Version    : 0.1.0                                                                               #
# Filename   : \1_tictactoe.py                                                                     #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/reinforcement-learning                             #
# ------------------------------------------------------------------------------------------------ #
# Created    : Wednesday July 13th 2022 01:51:23 pm                                                #
# Modified   : Thursday July 14th 2022 01:06:30 am                                                 #
# ------------------------------------------------------------------------------------------------ #
# License    : BSD 3-clause "New" or "Revised" License                                             #
# Copyright  : (c) 2022 John James                                                                 #
# ================================================================================================ #
import numpy as np
from typing import Union
import logging

# ------------------------------------------------------------------------------------------------ #
logger = logging.getLogger(__name__)
# ------------------------------------------------------------------------------------------------ #


class Player:
    """The agent object w/in the reinforcement learning paradigm."""

    def __init__(self, name: str, mark: str) -> None:
        self._name = name
        self._mark = mark
        self._policies = None


# ------------------------------------------------------------------------------------------------ #
class Board:
    """Represents the current state of the game."""

    def __init__(self, size: int = 3) -> None:
        self._size = size
        self._board = np.empty(size, size)
        self._winner = None
        self._has_winner = False
        self._game_over = False

    def move(self, player: Player, x: int, y: int) -> None:
        try:
            assert not self._board[x, y], logger.error(
                "Position [{},{}] occupied".format(str(x), str(y))
            )
            self._board[x, y] = player.mark
        except KeyError as e:
            logger.error(
                "Invalid coordinates: x,y. Valid values are in {}\n{}".format(
                    str(range(self._size)), e
                )
            )

    @property
    def board(self) -> np.array:
        return self._board

    @property
    def frontier(self) -> np.array:
        return self._frontier

    @property
    def winner(self) -> Union[str, int]:
        return self._winner

    @property
    def has_winner(self) -> bool:
        return self._has_winner

    @property
    def game_over(self) -> bool:
        return self._game_over

    def evaluate(self) -> None:
        self._game_over = self._game_over or not self.frontier()
        self._evaluate_rows()
        self._evaluate_cols()
        self._evaluate_diags()

    def _evaluate_rows(self) -> None:
        if not self._has_winner and not self._game_over:
            for i in range(self._size):
                self._has_winner = np.all(self._board[i] == self._board[i][0])
                if self._has_winner:
                    self._winner = self._board[i][0]
                    self._game_over is True
                break

    def _evaluate_cols(self) -> None:
        if not self._has_winner and not self._game_over:
            for i in range(self._size):
                self._has_winner = np.all(self._board[:, i] == self._board[:, i][0])
                if self._has_winner:
                    self._winner = self._board[:, i][0]
                    self._game_over is True
                break

    def _evaluate_diags(self) -> None:
        if not self._has_winner and not self._game_over:
            diag = np.diagonal(self._board)
            self._evaluate_diag(diag)
            diag = np.fliplr(self._board).diagonal()
            self._evaluate_diag(diag)

    def _evaluate_diag(self, diag) -> None:
        if not self._has_winner and not self._game_over:
            self._has_winner = all(diag[0] == diag)
            if self._has_winner:
                self._winner = diag[0]
                self._game_over is True


class Game:
    """The environment object w/in the reinforcement learning paradigm"""

    def __init__(self, p1: Player, p2: Player, random_state=None) -> None:
        self._p1 = p1
        self._p2 = p2
        self._random_state = random_state
        self._board = np.zeros(3, 3)

    def select_first_mover(self) -> Player:
        rng = np.random.default_rng()
        return rng.choice(np.array(self._p1, self._p2))
