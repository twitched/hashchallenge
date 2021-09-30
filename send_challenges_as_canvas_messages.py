import importlib.util, csv
from importlib.machinery import SourceFileLoader

import sys
sys.path.append("../../canvasapi")

spec = importlib.util.spec_from_loader("localcanvasapi", SourceFileLoader("localcanvasapi","../../canvasapi/localcanvasapi.py"))
localcanvasapi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(localcanvasapi)

spec = importlib.util.spec_from_loader("sendmessage", SourceFileLoader("sendmessage", "../../canvasapi/send_message.py"))
sendmessage = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sendmessage)

from canvasapi import Canvas

localcanvasapi.debug()

def main():
    args = getargparser().parse_args()
    canvas = localcanvasapi.startcanvasapi(args)
    send_messages(canvas, args.file)
    
def getargparser():
    p = localcanvasapi.get_argparser()
    p.description = "Send passwords for encryption assignment in ITM 455"
    p.add_argument('-f', '--file', required=True, help='A csv file with "user_id" and "challenge_file" columns')
    return p

def send_messages(canvas: Canvas, file: str):
    my_user = canvas.get_current_user();
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            message = f'The attached file contains the password hashes you should attempt to crack for the Password Cracking assignment'
            subject = 'ITM 455 Password Cracking'
            attachment = open(row['challenge_file'], 'r')
            sendmessage.send_message_with_attachment(canvas, row['user_id'], subject, message, True, attachment, my_user)
            print(f'Sent {message} with subject {subject} to {row["name"]}-{row["user_id"]} with attachment {attachment.name}')
    
if __name__ == '__main__':
   main()