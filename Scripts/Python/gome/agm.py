# -*- coding: utf-8 -*-

# GoMe - AGM
# Handles the AGM-specific commands.

from Plasma import *
from PlasmaConstants import *
from PlasmaNetConstants import *
from PlasmaTypes import *

import time

kModerators = {"Doobes", "GoMeDoobes", "GoMeLyrositor", "Lyrositor"}

# Chat log formatting.
kHeader = """<html>
    <head>
        <title>All Guilds Meeting - {0}</title>
        <style type="text/css">
        html, body {{
            background-color: #FFF68F;
            font: 14px Arial, sans-serif;
            margin: 0;
            padding: 0;
            text-align: center;
        }}
        
        h1 {{
            border-bottom: dotted 1px #CD9B1D;
            color: #8B6914;
            font-family: "Times New Roman", Times, "Liberation Serif", serif;
            font-size: 38px;
            letter-spacing: 2px;
            margin: 20px auto;
            padding: 10px 0;
            text-align: center;
            width: 80%;
        }}
        
        p {{
            margin: 5px 0;
        }}
        
        span.date {{
            margin-right: 10px;
        }}
        
        div#main {{
            background-color: #FFFFFF;
            border: solid 1px #CCCCCC;
            border-radius: 3px;
            margin: 10px auto;
            padding: 10px;
            text-align: justify;
            width: 80%;
        }}
        </style>
    </head>
    <body>
        <h1>All Guilds Meeting - {0}</h1>
        <div id="main">
            <p style=\"margin-bottom: 20px;\">
                <strong style=\"text-decoration: underline;\">KEY:</strong><br />
                <strong>Speaker</strong><br />
                <strong><em style=\"color: #23b8dc;\">Question</em></strong><br />
                <strong style=\"color: #b80047;\">Moderator</strong>
            </p>\n"""

kFooter = """        </div>
    </body>
</html>"""


## The class for handling the AGM.
class AGM:

    ## Start the AGM.
    def __init__(self, chatMgr):

        self.chatMgr = chatMgr

        # Set up the constant values.
        self.header = kHeader.format(time.strftime("%B %Y"))
        self.footer = kFooter
        self.rawLogFile = time.strftime("%B_all_guilds_meeting_%Y_raw.txt").lower()
        self.cleansedLogFile = time.strftime("%B_all_guilds_meeting_%Y_cleansed.html").lower()

        # Set up the variables.
        self.questions = []
        self.speakers = []

        # Prepare the log files.
        self.logRaw = open(self.rawLogFile, "w+")
        self.logCleansed = open(self.cleansedLogFile, "w+")
        self.logCleansed.write(self.header)

    ## Finishes writing the data to the log files.
    # If there are still some questions in the queue, notify the manager.
    def End(self):

        if self.questions:
            self.chatMgr.DisplayStatusMessage("The question queue is not empty!")
            if not force:
                return

        self.logRaw.close()
        self.logCleansed.write(self.footer)
        self.logCleansed.close()

    ## Asks a stored question.
    def AskQuestion(self, id=0):

        playerName, playerMessage = self.questions[id - 1]

        msg1 = f"Our next question is from {playerName}."
        PtSendRTChat(PtGetLocalPlayer(), PtGetPlayerList(), msg1, 0)
        self.chatMgr.AddChatLine(PtGetLocalPlayer(), msg1, 0, True)

        msg2 = f"[{playerName}] {playerMessage}"
        PtSendRTChat(PtGetLocalPlayer(), PtGetPlayerList(), msg2, 0)
        self.chatMgr.AddChatLine(PtGetLocalPlayer(), msg2, 0, True, True)

        del self.questions[id - 1]

    ## Deletes a stored question.
    def DeleteQuestion(self, id):

        del self.questions[id - 1]
        self.chatMgr.DisplayStatusMessage(f"Deleted question #{id}.")

    ## Lists all stored questions.
    def ListQuestions(self):

        self.chatMgr.DisplayStatusMessage("-- QUESTIONS --")
        if self.questions:
            for i, q in enumerate(self.questions):
                self.chatMgr.DisplayStatusMessage("{}) {}: {}".format(i + 1, *q))
        else:
            self.chatMgr.DisplayStatusMessage("The question queue is empty.")

    ## Writes a new log entry.
    def WriteLogs(self, player, msg, isStatus, isQuestion=False):

        if isinstance(player, str) or isinstance(player, unicode):
            playerName = player
        else:
            playerName = player.getPlayerName()
        tupTime = time.gmtime(PtGMTtoDniTime(long(time.time())))
        curTime = time.strftime("%H:%M:%S", tupTime)
        curDate = time.strftime("%Y-%m-%d", tupTime)
        theTime = f"({curDate} {curTime})"
        isSpeaker = playerName.lower() in [s.lower() for s in self.speakers] or isQuestion

        # Write the raw log data.
        if isStatus:
            self.logRaw.write(f"{theTime} {msg}\n")
        else:
            self.logRaw.write(f"{theTime}  {playerName}: {msg}\n")

        # Write the cleansed log data (escape the text, since it's HTML).
        msg = msg.encode("ascii", "xmlcharrefreplace")
        playerName = playerName.encode("ascii", "xmlcharrefreplace")
        if isSpeaker or isQuestion:
            if isStatus and ("claps his hand" in msg or "claps her hands" in msg or "cheers" in msg):
                return
            cleansedMsg = "<p><strong>{}".format("<em style=\"color: #23b8dc;\">" if isQuestion else "")
            cleansedMsg += f"<span class=\"date\">{theTime}</span><span class=\"message\">"
            cleansedMsg += msg if isStatus else f"{playerName}: {msg}"
            cleansedMsg += "</span>{}</strong></p>".format("</em>" if isQuestion else "")
        else:
            if isStatus and ("claps his hand" in msg or "claps her hands" in msg or "cheers" in msg):
                return
            cleansedMsg = "<p{}><span class=\"date\">{}</span><span class=\"message\">".format(" style=\"color: #b80047; font-weight: bold;\"" if playerName == PtGetLocalPlayer().getPlayerName() else "", theTime)
            cleansedMsg += msg if isStatus else f"{playerName}: {msg}"
            cleansedMsg += "</span></p>"
        self.logCleansed.write(f"            {cleansedMsg}\n")
