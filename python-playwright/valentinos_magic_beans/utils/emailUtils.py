import os
import time

from dotenv import load_dotenv
from mailslurp_client import Configuration, ApiClient, InboxControllerApi
load_dotenv()

class emailUtils:
    def __init__(self):
        self.configuration = Configuration()
        self.configuration.api_key["x-api-key"] = os.getenv("MAIL_SLURP_API_KEY")
        self.inbox_controller = InboxControllerApi(ApiClient(self.configuration))

    def createInbox(self):
        return self.inbox_controller.create_inbox()

    async def waitForMail(self, inbox_id):
        return await self.inbox_controller.get_latest_email_in_inbox(inbox_id,timeout_millis=30000)