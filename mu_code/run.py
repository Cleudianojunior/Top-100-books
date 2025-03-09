import sys
from streamlit.web import cli as stcli

sys.argv = ["streamlit", "run", "Top 100 books.py"]
sys.exit(stcli.main())

