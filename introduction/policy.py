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
# Created    : Thursday July 14th 2022 08:50:11 pm                                                 #
# Modified   : Friday July 15th 2022 03:50:28 am                                                   #
# ------------------------------------------------------------------------------------------------ #
# License    : BSD 3-clause "New" or "Revised" License                                             #
# Copyright  : (c) 2022 John James                                                                 #
# ================================================================================================ #
from abc import ABC, abstractmethod
from dataclasses import dataclass
import numpy as np
from typing import Union
import logging

# ------------------------------------------------------------------------------------------------ #
logger = logging.getLogger(__name__)
# ------------------------------------------------------------------------------------------------ #
class Policy:
    """Defines a reinforcement learning policy object."""
    id: int 
    state: np.array
    value: float
    action: np.array

class PolicySpace(ABC):

    def __init__(self, policies: dict) -> None:
        self._policy = None

    """

    def __init__(self, id: int, state: np.array, value: float = 0.5) -> None:
        self._id = id
        self._state = None
        self._value = None
        self._action = None

    @property
    def id(self) -> int:
        return self._id

    @property
    def state(self) -> np.array:
        return self._state

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value: float) -> None:
        self._value = value

    def move(self) -> np.array:



# ------------------------------------------------------------------------------------------------ #
class PolicySpace(ABC):
    """Abstract base class for Policy subclasses in the reinforcement learning framework."""

    def __init__(self) -> None:
        self._id
        self._policies = None

    def generate_policies(self) -> None:
        """Generates the policy space.

        The policy space defines our reinforcement learning value function and contains
        a policy for each possible state i.e., configuration of X's and O's. Additionally,
        each policy is a assigned a value which represents the latest estimate of the probability
        of winning the game from that state.

        There are 9 factorial (362,880) possible states on a nine-cell tic-tac-toe board if we
        play each game until all cells are filled. But wait, the nine-cell board is filled by
        alternating moves between two players. Assuming we start the game with player X,
        the filled board would then contain five Xs and four Os. To compute the total number of
        possible states, we must divide
        begins, we have nine locations to
        place the X, our board game alternates between
        the two players; therefore, the  , this includes invalid states
        states, such as those including all Xs or all Os. Rather, players fill the board by taking
        turns. Let's assume that player X begins by placing an X in one of the nine cells. Player O
        is left with eight choices. The players continue to make moves in an alternate fashion
        until the board is filled. Hence, Player X had five possible moves to make, and Player O
        had four.

        Since we don't care about order of the Xs and Os

        Unlike the

        five  Assuming we begin the game with a move by player X, we have nine possible placements
        for the X.  begins
        alternating moves.  Rather, let's assume that playAs the game alternates between
        two players, a filled nine-cell board would have at most five Xs and four Os, assumingour nine-cell board would Rather, the players Rather, the game fills the board via nine,
        alternating moves yielding  player takes his or her
        turn making moves. So the total number of possible states Since the players take turns making
        moves until the board is filled, our nine-cell board  conduct alternating  states include games terminate when a row, column,
        or diagonal is comprised solely of a player's (or opponent's) mark. Hence, There are three rows,
        three columns, and two diagonals that

        We initialize the policy states acco

        Probabilities, i.e. the policy values are intialized based upon the existence
        of a winning (or losing) state i.e, a row, column, or diagonal comprised solely of
        the player's (or opponent's) mark. . The current player's mark across a row, column,
        or diagonal
        with values in [0,1,0.5] subject to the winning condition



        A row, column, or diagonal containing the
        current player's mark indicates a win, the estimate of the probability of a win
        at that stage is 1, hence the policy value would be set to 1. Conversely, the estimated
        probability of a win from that state is zero if should a row, column, or diagonal be comprised solely of
        the opponent's markthe opponent's
        mark
        the probability of winning is 0; as such, the probability of a win  the value for that policy is set
        to 1. Conversely, the value prEach policy defines
        a single state configurationa vector specifying one of the possible states of the game. Each policy, encodes a value
        associated with the encoded state configuration, which is the latest estimate
        of the probability of winning the game from that state. This method generates
        the policy space and the winning probabilities for each state. If each element of
        a row, column, or diagonal is equal to the current player's mark (X or O), the probability of
        winning from that state, and the policy value is 1. Should the row, column, or diagonal
        contain the opponent's mark, the probability of winning, and the policy value, is set to 0. The
        estimated probabilities for all other states are initialized at 0.5.
        """


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
