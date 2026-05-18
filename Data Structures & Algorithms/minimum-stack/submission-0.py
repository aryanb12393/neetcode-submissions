class MinStack:

    def __init__(self):
        self.actual_stack = []
        self.the_min = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.actual_stack.append(val)

        curr_len_tm = len(self.the_min)

        if curr_len_tm == 0:
            self.the_min.append(val)
        else:
            curr_min = self.the_min[curr_len_tm-1]
            # found a new min
            if curr_min >= val:
                self.the_min.append(val)

        print("completed push")

    def pop(self):
        """
        :rtype: None
        """
        curr_val = self.top()
        self.actual_stack = self.actual_stack[:len(self.actual_stack)-1]

        # the min is the same
        if curr_val == self.the_min[len(self.the_min)-1]:
            self.the_min = self.the_min[:len(self.the_min)-1]

        # return curr_val

    def top(self):
        """
        :rtype: int
        """
        return self.actual_stack[len(self.actual_stack)-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        print(self.the_min)
        return self.the_min[len(self.the_min)-1]
        
        
