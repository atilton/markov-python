import sys
from markov import Markov

markov = Markov()
if len(sys.argv) < 2:
  markov.print_help()
else:
  markov.run(sys.argv)
