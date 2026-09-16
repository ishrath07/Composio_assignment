from dotenv import load_dotenv
load_dotenv()

from composio import Composio

composio = Composio()  # reads COMPOSIO_API_KEY from .env
tools = composio.tools.get(user_id="default", toolkits=["GITHUB"])
print(tools)