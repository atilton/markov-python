# Austin Tilton February 2019

class Markov(object):
  def run(self, argv):
    for arg in arv:
      print arg
  
  def print_help(self):
    print "Usage: <operation> <arguments...>\n",
    "operations:\n",
    "  create <wordlist> <link size> <dictionary>:\n",
    "    Generates a dictionary from a given wordlist file & link\n",
    "    size. The resulting dictionary is saved into <dictionary>.\n",
    "  load <dictionary>:\n"
    "    Loads a given dictionary file and then enters command line\n",
    "    mode.\n",
    "  print <dictionary> <length>:\n",
    "    Loads a given dictionary file then generates text of <length>\n",
    "    size output.\n",
    "  start <dictionary>(OPTIONAL):\n",
    "    Begins the program in command line mode. If a dictionary file\n",
    "    is provided, it will be loaded first.\n",
    "  help:\n",
    "    Prints this usage prompt\n"
