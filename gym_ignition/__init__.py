# Copyright (C) 2019 Istituto Italiano di Tecnologia (IIT). All rights reserved.
# This software may be modified and distributed under the terms of the
# GNU Lesser General Public License v2.1 or any later version.

# Import gympp bindings
# See https://github.com/robotology/gym-ignition/issues/7
import sys
if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    import ctypes
    sys.setdlopenflags(sys.getdlopenflags() | ctypes.RTLD_GLOBAL)
import gympp

from gym.envs.registration import register
from gym_ignition.envs.base.ignition_env import IgnitionEnv
from gym_ignition.envs.base.ignition_python_env import IgnitionPythonEnv

register(
    id='CartPoleIgnition-v0',
    entry_point='gym_ignition.envs.cpp.cartpole:CartPoleEnv')

register(
    id='CartPoleIgnitionPython-v0',
    entry_point='gym_ignition.envs.python.cartpole:CartPolePythonEnv')
