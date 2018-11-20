from fetch_data import get_data
from markov_python.cc_markov_py3 import MarkovChain

""" Get a song lyrics and reurn a new song lyrics by using a Makov Chain Generator"""

mc = MarkovChain()
mc.add_string(get_data())
mctext = mc.generate_text()
print('\n'.join(mctext))
print('Thanks for useing, see you next time')
