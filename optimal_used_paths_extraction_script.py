#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from __future__ import print_function

import os
import numpy as np
from absl import app
from absl import flags

import tensorflow as tf
from env import Environment
from game import CFRRL_Game
from model import Network
from config import get_config


# In[ ]:




FLAGS = flags.FLAGS
flags.DEFINE_string('ckpt', '', 'apply a specific checkpoint')
flags.DEFINE_boolean('eval_delay', False, 'evaluate delay or not')

def sim(game):
    for tm_idx in game.tm_indexes:
        _, solution = game.optimal_routing_mlu(tm_idx)
        optimal_mlu, optimal_mlu_delay = game.eval_optimal_routing_mlu(tm_idx, solution, eval_delay=False)

        for item,v in solution.items():
            print('flow index %s from node %s to the next node %s ratio %s'%(item[0],item[1],item[2],v))
        import pdb
        pdb.set_trace()
        #game.evaluate(tm_idx, actions, eval_delay=FLAGS.eval_delay) 

def main(_):
    #Using cpu for testing
    tf.config.experimental.set_visible_devices([], 'GPU')
    tf.get_logger().setLevel('INFO')

    config = get_config(FLAGS) or FLAGS
    env = Environment(config, is_training=False)
    game = CFRRL_Game(config, env)
    network = Network(config, game.state_dims, game.action_dim, game.max_moves)

    sim(game)


if __name__ == '__main__':
    app.run(main)

