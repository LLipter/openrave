#!/usr/bin/env python
"""Examples showing common planning and usage scenarios.

Unlike the tutorials, python examples are installed with openravepy and their list can be retrieved with:

.. code-block:: bash

  openrave.py --listexamples

Execute example ``X`` using:

.. code-block:: bash

  openrave.py --example X

Each sub-module contains a 'run' function that can be called directly with options to configure the example.
"""

# tutorials showing a single functionality (simple)
import tutorial_001
import tutorial_002
import tutorial_003
import tutorial_004
import tutorial_grasptransform
import tutorial_ik5d
import tutorial_iklookat
import tutorial_iklookat_multiple
import tutorial_iksolutions
import tutorial_iktranslation
import tutorial_iktranslation2d
import tutorial_inversereachability
import tutorial_plotting

# examples showing complex demos
import calibrationviews
import checkconvexdecomposition
import checkvisibility
import collision
import collision2
import constraintplanning
import dualarmdemo_schunk
import fastgrasping
import hanoi
import graspplanning
import movehandstraight
import movehandstraight2
import showsensors
import simplenavigation
import testphysics
import testphysics_controller
import testphysics_diffdrive
import testupdatingbodies
import testviewercallback
import visibilityplanning
