"""
Test 2, problems 2a and 2b.

Authors: Sriram Mohan and PUT_YOUR_NAME_HERE.  January 2016.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math
import simple_testing as st


# ------------------------------------------------------------------
# Students:
#  Do NOT touch the   Point  class below - it has no TODO.
#  Do NOT copy code from this class.
#
# Instead, ** CALL ** method(s) from this class as needed
# in the problems below.
# ------------------------------------------------------------------
class Point(object):
    """ Represents a point in 2-dimensional space. """

    def __init__(self, x, y):
        """
        Sets instance variables  x  and  y  to the given coordinates.
        """
        self.x = x
        self.y = y

    def __repr__(self):
        """ Returns a string representation of this Point. """
        return 'Point({}, {})'.format(self.x, self.y)

    def __eq__(self, p2):
        """
        Defines == for Points:  a == b   is equivalent to  a.__eq__(b).
        """
        return isinstance(p2, Point) and \
            (self.x == p2.x) and (self.y == p2.y)

    def clone(self):
        """  Returns a new Point at the same (x, y) as this Point. """
        return Point(self.x, self.y)

    def distance_from(self, p2):
        """ Returns the distance this Point is from the given Point. """
        dx_squared = (self.x - p2.x) ** 2
        dy_squared = (self.y - p2.y) ** 2

        return math.sqrt(dx_squared + dy_squared)


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem2a()
    test_problem2b()


def test_problem2a():
    """ Tests the   problem2a   function. """
    # ------------------------------------------------------------------
    # These tests use the imported   simple_testing (st)   module.
    # Each test is a SimpleTestCase with 3 arguments:
    #   -- the function to test,
    #   -- a list containing the argument(s) to send to the function,
    #   -- the correct returned value.
    # For example, the first test below will call
    #   problem2a([Point(100, 3), Point(50, 10), Point(7, 11)])
    # and compare the returned value against  157  (the correct answer).
    # ------------------------------------------------------------------
    tests = [st.SimpleTestCase(problem2a,
                               [[Point(100, 3),
                                 Point(50, 10),
                                 Point(7, 11)],
                                ],
                               157),
             st.SimpleTestCase(problem2a,
                               [[Point(77, 555)],
                                ],
                               77),
             st.SimpleTestCase(problem2a,
                               [[Point(10, 5),
                                 Point(10, 8),
                                 Point(10, 8)],
                                ],
                               30),
             st.SimpleTestCase(problem2a,
                               [[Point(200, 200),
                                 Point(500, 500),
                                 Point(400, 400)],
                                ],
                               1100),
             st.SimpleTestCase(problem2a,
                               [[Point(100, 10),
                                 Point(7, 10),
                                 Point(57, 10),
                                 Point(10, 10),
                                 Point(4, 10),
                                 Point(33, 10),
                                 Point(20, 10),
                                 Point(21, 10),
                                 Point(38, 10),
                                 Point(59, 10),
                                 Point(77, 10),
                                 Point(50, 10),
                                 Point(37, 10),
                                 Point(33, 10),
                                 Point(0, 10),
                                 Point(90, 10),
                                 Point(70, 10)],
                                ],
                               706),
             st.SimpleTestCase(problem2a,
                               [[Point(0, 3),
                                 Point(0, 10),
                                 Point(0, 11)],
                                ],
                               0),
             st.SimpleTestCase(problem2a,
                               [[Point(-5, 3),
                                 Point(0, 10),
                                 Point(5, 11),
                                 Point(0, 10),
                                 Point(40, 11),
                                 Point(-30, 11),
                                 Point(-10, 11)],
                                ],
                               0),
             st.SimpleTestCase(problem2a,
                               [[],
                                ],
                               0),
             ]

    # ------------------------------------------------------------------
    # Run the tests in the   tests   list constructed above.
    # ------------------------------------------------------------------
    st.SimpleTestCase.run_tests('problem2a', tests)


def problem2a(points):
    """
    What comes in: A sequence of Point objects.
      [The  Point  class is defined above.]
    What goes out: Returns the sum of the x-coordinates
      of the Points in the given sequence.
    Side effects: None.
    Examples:
      If  points  is [Point(100, 3), Point(50, 10), Point(7, 11)],
        this function returns 100 + 50 + 7, which is 157.

      If  points  is [Point(77, 555)], this function returns 77.

      If  points  is [Point(10, 5), Point(10, 8), Point(10, 8)],
        this function returns 10 + 10 + 10, which is 30.

    Type hints: [The first argument is actually a SEQUENCE of Points.]
      :type points: Point
    """
    # ------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #   We have written tests for you (above).
    # 10 Points
    # ------------------------------------------------------------------


def test_problem2b():
    """ Tests the   problem2b   function. """
    tests = [st.SimpleTestCase(problem2b,
                               [[Point(100, 3),
                                 Point(50, 10),
                                 Point(7, 11)], Point(49, 13),
                                ],
                               Point(50, 10)),
             st.SimpleTestCase(problem2b,
                               [[Point(77, 555),
                                 ], Point(1000, 10000),
                                ],
                               Point(77, 555)),
             st.SimpleTestCase(problem2b,
                               [[Point(100, 50),
                                 Point(10, 8),
                                 Point(10, 8)], Point(11, 7),
                                ],
                               Point(10, 8)),
             st.SimpleTestCase(problem2b,
                               [[Point(100, 20),
                                 Point(1000, 1000),
                                 Point(0, 60)], Point(50, 40),
                                ],
                               Point(100, 20)),
             st.SimpleTestCase(problem2b,
                               [[Point(10, 10),
                                 Point(20, 20),
                                 Point(30, 30),
                                 Point(20, 20),
                                 Point(15, 15),
                                 ], Point(11, 11),
                                ],
                               Point(10, 10)),
             st.SimpleTestCase(problem2b,
                               [[Point(10, 10),
                                 Point(20, 20),
                                 Point(30, 30),
                                 Point(40, 40),
                                 Point(15, 15),
                                 ], Point(14, 14),
                                ],
                               Point(15, 15)),
             st.SimpleTestCase(problem2b,
                               [[Point(10, 57),
                                 Point(10, 56),
                                 Point(10, 53),
                                 Point(10, 56),
                                 Point(9, 55),
                                 ], Point(10, 54),
                                ],
                               Point(10, 53)),
             st.SimpleTestCase(problem2b,
                               [[Point(57, 10),
                                 Point(56, 10),
                                 Point(53, 10),
                                 Point(56, 10),
                                 Point(54, 9),
                                 ], Point(54, 10),
                                ],
                               Point(53, 10)),
             st.SimpleTestCase(problem2b,
                               [[Point(77, 555),
                                 Point(0, 0),
                                 Point(0, 0),
                                 Point(0, 0),
                                 Point(0, 0),
                                 ], Point(1000, 10000),
                                ],
                               Point(77, 555)),
             st.SimpleTestCase(problem2b,
                               [[Point(77, 555),
                                 Point(56, 30),
                                 Point(40, 100),
                                 Point(0, 0),
                                 Point(1, 1),
                                 Point(30, 10),
                                 Point(40, 70),
                                 Point(20, 5)
                                 ], Point(1000, 10000),
                                ],
                               Point(77, 555)),
             st.SimpleTestCase(problem2b,
                               [[Point(77, 555),
                                 Point(56, 30),
                                 Point(40, 100),
                                 Point(0, 0),
                                 Point(1, 1),
                                 Point(30, 10),
                                 Point(40, 70),
                                 Point(20, 5)
                                 ], Point(40, 33),
                                ],
                               Point(56, 30)),
             st.SimpleTestCase(problem2b,
                               [[Point(77, 555),
                                 Point(56, 30),
                                 Point(40, 100),
                                 Point(0, 0),
                                 Point(1, 1),
                                 Point(30, 10),
                                 Point(40, 70),
                                 Point(20, 5)
                                 ], Point(45, 85),
                                ],
                               Point(40, 100)),
             st.SimpleTestCase(problem2b,
                               [[Point(77, 555),
                                 Point(56, 30),
                                 Point(40, 100),
                                 Point(0, 0),
                                 Point(1, 1),
                                 Point(30, 10),
                                 Point(40, 70),
                                 Point(20, 5)
                                 ], Point(45, 84),
                                ],
                               Point(40, 70)),
             st.SimpleTestCase(problem2b,
                               [[Point(77, 555),
                                 Point(56, 30),
                                 Point(40, 100),
                                 Point(0, 0),
                                 Point(1, 1),
                                 Point(30, 10),
                                 Point(40, 70),
                                 Point(20, 5)
                                 ], Point(0, 1),
                                ],
                               Point(0, 0)),
             st.SimpleTestCase(problem2b,
                               [[Point(77, 555),
                                 Point(56, 30),
                                 Point(40, 100),
                                 Point(1, 1),
                                 Point(0, 0),
                                 Point(30, 10),
                                 Point(40, 70),
                                 Point(20, 5)
                                 ], Point(0, 1),
                                ],
                               Point(1, 1)),
             st.SimpleTestCase(problem2b,
                               [[Point(77, 555),
                                 Point(56, 30),
                                 Point(40, 100),
                                 Point(1, 1),
                                 Point(0, 0),
                                 Point(30, 10),
                                 Point(40, 70),
                                 Point(20, 5)
                                 ], Point(25, 7),
                                ],
                               Point(20, 5)),
             ]

    # ------------------------------------------------------------------
    # Run the tests in the   tests   list constructed above.
    # ------------------------------------------------------------------
    st.SimpleTestCase.run_tests('problem2b', tests)


def problem2b(points, my_point):
    """
    What comes in:
      -- points:   A non-empty sequence of Point objects.
      -- my_point: A Point.
      [The  Point  class is defined above.]
    What goes out: Returns the Point in the sequence
      which is closest to the given  my_point.
        -- If two Points in the sequence are tied for closest,
           this function returns the one with a smaller index
           (i.e., the one that is earlier in the list).
    Side effects: None.
    Examples:
      If  points  is [Point(100, 3), Point(50, 10), Point(7, 11)]
        and  my_point  is Point(49, 13),
        then this function returns Point(50, 10)
        because Point(49, 13) is closer to Point(50, 10) than to
        any other Point in the sequence.

      If  points  is [Point(77, 555)]
        and  my_point  is Point(1000, 10000)  (or any other Point),
        then this function returns Point(77, 555).

      If  points  is [Point(100, 50), Point(10, 8), Point(10, 8)]
        and  my_point  is Point(11, 7),
        then this function returns Point(10, 8).

      If  points  is [Point(100, 20), Point(1000, 1000), Point(0, 60)]
        and  my_point  is Point(50, 40),
        then this function returns Point(100, 20)
        (breaking the tie in favor of the earlier point in the sequence)

    Type hints: [The first argument is actually a SEQUENCE of Points.]
      :type points: Point
      :type my_point: Point
    """
    # ------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #   We have written tests for you (above).
    # 5 Points
    #
    ####################################################################
    # IMPORTANT:
    #    **  For full credit you must use (call) appropriate
    #    **  method(s) defined in the Point that is defined above.
    # In my opinion, this is the most difficult problem on the test.
    # Do NOT start this problem until you have problem 3.
    ####################################################################
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
