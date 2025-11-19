Repo ChatSC - ระบบเต็มฟีเจอร์ของ ChatSC

main bot

from chatsc.handlers.message_handler import handle_message from chatsc.handlers.command_handler import handle_command from chatsc.utils.notification import send_notification from chatsc.utils.metadata import tag_owner from chatsc.database.db import Database

class ChatSC: def init(self): self.name = "ChatSC" self.db = Database() print(f"{self.name} Initialized ✅")

def receive_message(self, message, user_id):
    # วิเคราะห์ข้อความ
    response, suggestion = handle_message(message, user_id)
    # บันทึก Metadata + Tag เจ้าของ
    tag_owner(message, user_id)
    # ส่ง Notification หากมี Action สำคัญ
    if suggestion.get("critical"):
        send_notification(suggestion)
    # ตรวจสอบคำสั่งพิเศษ
    if suggestion.get("command"):
        handle_command(suggestion['command'], user_id)
    return response

if name == "main": bot = ChatSC() user_msg = "ตรวจสอบยอด TPS Global Fund" response = bot.receive_message(user_msg, user_id="Thanva") print(response)
