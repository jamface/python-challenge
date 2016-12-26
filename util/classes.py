import collections


class ReportingDeque(collections.deque):
    """
    A deque object that reports on its state.
    Can accept a condition function to check, as well as a callback to run.
    """
    def report(self, condition=None, callback=None):
        """
        Report on the state of the deque.

        Args:
            condition: function that should take the state as an argument and return
                True or False if the state satisfies a given condition.
            callback: function that should be executed if the condition function
                returns True, this should take the state as an argument.
        Returns:
            String representation of the deque's state if no condition function is
            provided; True or False if a condition function is provided.
        """
        state = ''.join(self)
        if condition:
            if callback:
                return callback(state) if condition(state) else False
            else:
                return condition(state)
        return state
