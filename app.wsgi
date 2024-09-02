import site
import sys

sys.path.insert(0, '/home/debian/.pyenv/versions/thoth-edu/lib/python3.12/site-packages')

site.addsitedir('/home/debian/.pyenv/versions/thoth-edu/lib/python3.12/site-packages')

sys.path.insert(0, '/var/www/thoth-edu.fr-backend')

from main import app as application
