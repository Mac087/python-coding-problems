# Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

# For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.

class Reader:
    def __init__(self):
        self.remainder = ''

    def readN(self, n):
        result = self.remainder
        text = None

        while len(result) < n and (text is None or len(text) >= 5):
            text = read7()
            result += text

        self.remainder = result[n:]

        return result[:n]