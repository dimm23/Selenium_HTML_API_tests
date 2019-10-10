from locators import MainPageLocators
import settings
import json
from selenium.webdriver.support.ui import Select
from selenium.common import exceptions
import time
import pyperclip
import pyautogui as p

class MainPage(object):
    def __init__(self, driver):
        self.driver = driver
    
    def getSystemInfo(self):
        self.driver.find_element(*MainPageLocators.lnk_getSystemInfo).click()

    def getProfileStatus(self):
        self.driver.find_element(*MainPageLocators.lnk_getProfileStatus).click()

    def setProfileStatus(self):
        self.driver.find_element(*MainPageLocators.lnk_setProfileStatus).click()
        statusSelector = Select(self.driver.find_element(*MainPageLocators.slct_setProfileStatusValue))
        statusSelector.select_by_value("Available")
        self.driver.find_element(*MainPageLocators.fld_setProfileStatusMood).send_keys("QA Engineer")

    def getOwnContact(self):
        self.driver.find_element(*MainPageLocators.lnk_getOwnContact).click()

    def getContacts(self):
        self.driver.find_element(*MainPageLocators.lnk_getContacts).click()
        self.driver.find_element(*MainPageLocators.fld_getContactsFilter).send_keys("a")

    def getContactAvatar(self):
        self.driver.find_element(*MainPageLocators.lnk_getContactAvatar).click()
        self.driver.find_element(*MainPageLocators.fld_getContactAvatarPk).send_keys(settings.contactPk)

    def getChannelAvatar(self):
        self.driver.find_element(*MainPageLocators.lnk_getChannelAvatar).click()
        self.driver.find_element(*MainPageLocators.fld_getChannelAvatar_channelid).send_keys(settings.channelid)

    def setContactGroup(self):
        self.driver.find_element(*MainPageLocators.lnk_setContactGroup).click()
        self.driver.find_element(*MainPageLocators.fld_setContactGroupContactPublicKey).send_keys(settings.contactPk)
        self.driver.find_element(*MainPageLocators.fld_setContactGroupGroupName).send_keys("HTML-API-GROUP")

    def setContactNick(self):
        self.driver.find_element(*MainPageLocators.lnk_setContactNick).click()
        self.driver.find_element(*MainPageLocators.fld_setContactNickСontactPublicKey).send_keys(settings.contactPk)
        self.driver.find_element(*MainPageLocators.fld_setContactNickNewNick).send_keys(settings.contactName)

    def sendInstantMessage(self):
        self.driver.find_element(*MainPageLocators.lnk_sendInstantMessage).click()
        self.driver.find_element(*MainPageLocators.fld_sendInstantMessageTo).send_keys(settings.contactName)
        self.driver.find_element(*MainPageLocators.fld_sendInstantMessageText).send_keys("Message from html api automated test")

    def sendInstantQuote(self):
        self.getContactMessages()
        self.enter_access_token()
        self.execute()
        contact_msgs = self.getResponse()
        if len(contact_msgs["result"]) == 0:
            self.sendInstantMessage()
            self.enter_access_token()
            self.execute()
            self.getContactMessages()
            self.enter_access_token()
            self.execute()
            contact_msgs = self.getResponse()
        self.driver.find_element(*MainPageLocators.lnk_sendInstantQuote).click()
        self.driver.find_element(*MainPageLocators.fld_sendInstantQuote_to).send_keys(settings.contactPk)
        self.driver.find_element(*MainPageLocators.fld_sendInstantQuote_text).send_keys("This is quote from html api")
        self.driver.find_element(*MainPageLocators.fld_sendInstantQuote_id_message).send_keys(contact_msgs["result"][0]["id"])

    def sendInstantSticker(self):
        self.driver.find_element(*MainPageLocators.lnk_sendInstantSticker).click()
        self.driver.find_element(*MainPageLocators.fld_sendInstantSticker_to).send_keys(settings.contactPk)
        self.driver.find_element(*MainPageLocators.fld_sendInstantSticker_collection).send_keys("Default Stickers")
        self.driver.find_element(*MainPageLocators.fld_sendInstantSticker_name).send_keys("1984")

    def sendInstantBuzz(self):
        self.driver.find_element(*MainPageLocators.lnk_sendInstantBuzz).click()
        self.driver.find_element(*MainPageLocators.fld_sendInstantBuzz_to).send_keys(settings.contactPk)

    def sendInstantInvitation(self):
        self.driver.find_element(*MainPageLocators.lnk_sendInstantInvitation).click()
        self.driver.find_element(*MainPageLocators.fld_sendInstantInvitation_to).send_keys(settings.contactPk)
        self.driver.find_element(*MainPageLocators.fld_sendInstantInvitation_channelid).send_keys(settings.channelid)
        #self.driver.find_element(*MainPageLocators.fld_sendInstantInvitation_description).send_keys("this description from api")
        self.driver.find_element(*MainPageLocators.fld_sendInstantInvitation_comments).send_keys("This comment from api")

    def removeInstantMessages(self):
        self.driver.find_element(*MainPageLocators.lnk_removeInstantMessages).click()
        self.driver.find_element(*MainPageLocators.fld_removeInstantMessages_hex_contact_public_key).send_keys(settings.contactPk)

    def getContactMessages(self):
        self.driver.find_element(*MainPageLocators.lnk_getContactMessages).click()
        self.driver.find_element(*MainPageLocators.fld_getContactMessages_pk).send_keys(settings.contactPk)

    def sendEmailMessage(self):
        self.driver.find_element(*MainPageLocators.lnk_sendEmailMessage).click()
        self.driver.find_element(*MainPageLocators.fld_sendEmailMessageTo).send_keys(settings.contactName)
        self.driver.find_element(*MainPageLocators.fld_sendEmailMessageSubject).send_keys("HTML API Subject")
        self.driver.find_element(*MainPageLocators.fld_sendEmailMessageBody).send_keys("HTML API Body")

    def sendPaymentPkToPk(self):
        self.driver.find_element(*MainPageLocators.lnk_sendPayment).click()
        self.driver.find_element(*MainPageLocators.fld_sendPaymentTo).send_keys(settings.contactPk)
        self.driver.find_element(*MainPageLocators.fld_sendPaymentAmount).send_keys("0.02")
        self.driver.find_element(*MainPageLocators.fld_sendPaymentComment).send_keys("Payment Pk to Pk")

    def sendPaymentCardToPk(self):
        self.driver.find_element(*MainPageLocators.lnk_sendPayment).click()
        self.driver.find_element(*MainPageLocators.fld_sendPaymentTo).send_keys(settings.contactPk)
        self.driver.find_element(*MainPageLocators.fld_sendPaymentAmount).send_keys("0.01")
        self.driver.find_element(*MainPageLocators.fld_sendPaymentComment).send_keys("Payment Card to Pk")
        self.driver.find_element(*MainPageLocators.fld_sendPaymentCardId).send_keys(settings.selfCard)

    def sendPaymentCardToCard(self):
        self.driver.find_element(*MainPageLocators.lnk_sendPayment).click()
        self.driver.find_element(*MainPageLocators.fld_sendPaymentTo).send_keys(settings.contactCard)
        self.driver.find_element(*MainPageLocators.fld_sendPaymentAmount).send_keys("0.01")
        self.driver.find_element(*MainPageLocators.fld_sendPaymentComment).send_keys("Payment Card to Pk")
        self.driver.find_element(*MainPageLocators.fld_sendPaymentCardId).send_keys(settings.selfCard)

    def getEmailFolder(self):
        self.driver.find_element(*MainPageLocators.lnk_getEmailFolder).click()
        self.driver.find_element(*MainPageLocators.fld_getEmailFolder_folderType).send_keys("1")
        self.driver.find_element(*MainPageLocators.fld_getEmailFolder_filter).send_keys("")

    def getEmails(self):
        self.driver.find_element(*MainPageLocators.lnk_getEmails).click()
        self.driver.find_element(*MainPageLocators.fld_getEmails_folderType).send_keys("1")
        self.driver.find_element(*MainPageLocators.fld_getEmails_filter).send_keys("")

    def getEmailById(self):
        self.getEmails()
        self.enter_access_token()
        self.execute()
        InboxEmails = self.getResponse()
        self.driver.find_element(*MainPageLocators.lnk_getEmailById).click()
        self.driver.find_element(*MainPageLocators.fld_getEmailById_id).send_keys(InboxEmails['result'][0]['id'])

    def deleteEmail(self):
        self.getEmails()
        self.enter_access_token()
        self.execute()
        InboxEmails = self.getResponse()
        self.driver.find_element(*MainPageLocators.lnk_deleteEmail).click()
        self.driver.find_element(*MainPageLocators.fld_deleteEmail_id).send_keys(InboxEmails['result'][-1]['id'])

    def sendReplyEmailMessage(self):
        self.getEmails()
        self.enter_access_token()
        self.execute()
        InboxEmails = self.getResponse()
        self.driver.find_element(*MainPageLocators.lnk_sendReplyEmailMessage).click()
        self.driver.find_element(*MainPageLocators.fld_sendReplyEmailMessage_id).send_keys(InboxEmails['result'][1]['id'])
        self.driver.find_element(*MainPageLocators.fld_sendReplyEmailMessage_body).send_keys("HTML API Reply body \n testing method: sendReplyEmailMessage")

    def sendForwardEmailMessage(self):
        self.getEmails()
        self.enter_access_token()
        self.execute()
        InboxEmails = self.getResponse()
        self.driver.find_element(*MainPageLocators.lnk_sendForwardEmailMessage).click()
        self.driver.find_element(*MainPageLocators.fld_sendForwardEmailMessage_id).send_keys(InboxEmails['result'][0]['id'])
        self.driver.find_element(*MainPageLocators.fld_sendForwardEmailMessage_to).send_keys(settings.contactName)
        self.driver.find_element(*MainPageLocators.fld_sendForwardEmailMessage_body).send_keys("HTML API Forward Email ===> \n testing method: sendForwardEmailMessage")

    def getFinanceSystemInformation(self):
        self.driver.find_element(*MainPageLocators.lnk_getFinanceSystemInformation).click()
        
    def getBalance(self):
        self.driver.find_element(*MainPageLocators.lnk_getBalance).click()

    def getFinanceHistory(self):
        self.driver.find_element(*MainPageLocators.lnk_getFinanceHistory).click()
        self.driver.find_element(*MainPageLocators.fld_getFinanceHistory_filters).send_keys("ALL_TRANSACTIONS")
        self.driver.find_element(*MainPageLocators.fld_getFinanceHistory_referenceNumber).send_keys("")

    def getCards(self):
        self.driver.find_element(*MainPageLocators.lnk_getCards).click()

    def addCard(self):
        self.driver.find_element(*MainPageLocators.lnk_addCard).click()
        self.driver.find_element(*MainPageLocators.fld_addCard_name).send_keys("DefaultCardName")
        self.driver.find_element(*MainPageLocators.fld_addCard_color).send_keys("#FFFFFF")

    def deleteCard(self):
        self.getCards()
        self.enter_access_token()
        self.execute()
        MyCards = self.getResponse()
        self.driver.find_element(*MainPageLocators.lnk_deleteCard).click()
        for card in MyCards['result']:
            if card['name'] == "DefaultCardName":
                self.driver.find_element(*MainPageLocators.fld_deleteCard_cardId).send_keys(card['cardid'])
                break

    def enableMining(self):
        self.driver.find_element(*MainPageLocators.lnk_enableMining).click()
        self.driver.find_element(*MainPageLocators.fld_enableMining_enable).send_keys("true")

    def enableInterest(self):
        self.driver.find_element(*MainPageLocators.lnk_enableInterest).click()
        self.driver.find_element(*MainPageLocators.fld_enableInterest_enable).send_keys("true")

    def enableHistoryMining(self):
        self.driver.find_element(*MainPageLocators.lnk_enableHistoryMining).click()
        self.driver.find_element(*MainPageLocators.fld_enableHistoryMining_enable).send_keys("true")

    def statusHistoryMining(self):
        self.driver.find_element(*MainPageLocators.lnk_statusHistoryMining).click()

    def getMiningBlocks(self):
        self.driver.find_element(*MainPageLocators.lnk_getMiningBlocks).click()

    def getMiningInfo(self):
        self.driver.find_element(*MainPageLocators.lnk_getMiningInfo).click()

    def getVouchers(self):
        self.driver.find_element(*MainPageLocators.lnk_getVouchers).click()

    def createVoucher(self):
        self.driver.find_element(*MainPageLocators.lnk_createVoucher).click()
        self.driver.find_element(*MainPageLocators.fld_createVoucherValue).send_keys("10")

    def useVoucher(self):
        self.getVouchers()
        self.enter_access_token()
        self.execute()
        MyVouchers = self.getResponse()
        if len(MyVouchers["result"]) < 1:
            self.createVoucher()
            self.enter_access_token()
            self.execute()
            time.sleep(3)
            self.getVouchers()
            self.enter_access_token()
            self.execute()
            MyVouchers = self.getResponse()
        self.driver.find_element(*MainPageLocators.lnk_useVoucher).click()
        self.driver.find_element(*MainPageLocators.fld_useVoucherVoucherId).send_keys(MyVouchers['result'][0]['voucherid'])

    def deleteVoucher(self):
        self.getVouchers()
        self.enter_access_token()
        self.execute()
        MyVouchers = self.getResponse()
        if len(MyVouchers["result"]) < 1:
            self.createVoucher()
            self.enter_access_token()
            self.execute()
            time.sleep(2)
            self.getVouchers()
            self.enter_access_token()
            self.execute()
            MyVouchers = self.getResponse()
        self.driver.find_element(*MainPageLocators.lnk_deleteVoucher).click()
        self.driver.find_element(*MainPageLocators.fld_deleteVoucherVoucherId).send_keys(MyVouchers['result'][0]['voucherid'])

    def getInvoices(self):
        self.driver.find_element(*MainPageLocators.lnk_getInvoices).click()

    def getInvoiceByReferenceNumber(self):
        self.driver.find_element(*MainPageLocators.lnk_getFinanceHistory).click()
        self.driver.find_element(*MainPageLocators.fld_getFinanceHistory_filters).send_keys("ALL_REQUESTS")
        self.enter_access_token()
        self.execute()
        MyInvoices = self.getResponse()
        self.driver.find_element(*MainPageLocators.lnk_getInvoiceByReferenceNumber).click()
        self.driver.find_element(*MainPageLocators.fld_getInvoiceByReferenceNumber_referenceNumber).send_keys(MyInvoices['result'][0]['referenceNumber'])

    def getTransactionIdByReferenceNumber(self):
        self.getFinanceHistory()
        self.enter_access_token()
        self.execute()
        MyTransactions = self.getResponse()
        self.driver.find_element(*MainPageLocators.lnk_getTransactionIdByReferenceNumber).click()
        self.driver.find_element(*MainPageLocators.fld_getTransactionIdByReferenceNumber_referenceNumber).send_keys(MyTransactions['result'][0]['referenceNumber'])

    def sendInvoice(self):
        self.driver.find_element(*MainPageLocators.lnk_sendInvoice).click()
        self.driver.find_element(*MainPageLocators.fld_sendInvoiceCardId).send_keys(settings.contactCard)
        self.driver.find_element(*MainPageLocators.fld_sendInvoiceAmount).send_keys("10")
        self.driver.find_element(*MainPageLocators.fld_sendInvoiceComment).send_keys("Дай денех")

    def acceptInvoice(self):
        self.getInvoices()
        self.enter_access_token()
        self.execute()
        MyInvoices = self.getResponse()
        self.driver.find_element(*MainPageLocators.lnk_acceptInvoice).click()
        self.driver.find_element(*MainPageLocators.fld_acceptInvoiceId).send_keys(MyInvoices['result'][0]['invoiceid'])

    def declineInvoice(self):
        self.getInvoices()
        self.enter_access_token()
        self.execute()
        MyInvoices = self.getResponse()
        self.driver.find_element(*MainPageLocators.lnk_declineInvoice).click()
        self.driver.find_element(*MainPageLocators.fld_declineInvoiceId).send_keys(MyInvoices['result'][0]['invoiceid'])

    def cancelInvoice(self):
        self.getInvoices()
        self.enter_access_token()
        self.execute()
        MyInvoices = self.getResponse()
        self.driver.find_element(*MainPageLocators.lnk_cancelInvoice).click()
        self.driver.find_element(*MainPageLocators.fld_cancelInvoiceId).send_keys(MyInvoices['result'][0]['invoiceid'])

    def requestUnsTransfer(self):
        self.unsRegisteredNames()
        self.enter_access_token()
        self.execute()
        MyUNS = self.getResponse()
        self.driver.find_element(*MainPageLocators.lnk_requestUnsTransfer).click()
        self.driver.find_element(*MainPageLocators.fld_requestUnsTransfer_name).send_keys(MyUNS['result'][-1]['nick'])
        self.driver.find_element(*MainPageLocators.fld_requestUnsTransfer_NewOwnerPk).send_keys(settings.contactPk)

    def acceptUnsTransfer(self):
        self.incomingUnsTransfer()
        self.enter_access_token()
        self.execute()
        MyIncomingUnsTransfers = self.getResponse()
        if len(MyIncomingUnsTransfers["result"]) > 0:
            self.driver.find_element(*MainPageLocators.lnk_acceptUnsTransfer).click()
            self.driver.find_element(*MainPageLocators.fld_acceptUnsTransfer_requestId).send_keys(MyIncomingUnsTransfers['result'][0]['id'])
        else:
            raise AssertionError("There is no Incoming uNS Transfers")

    def declineUnsTransfer(self):
        self.incomingUnsTransfer()
        self.enter_access_token()
        self.execute()
        MyIncomingUnsTransfers = self.getResponse()
        if len(MyIncomingUnsTransfers["result"]) > 0:
            self.driver.find_element(*MainPageLocators.lnk_declineUnsTransfer).click()
            self.driver.find_element(*MainPageLocators.fld_declineUnsTransfer_requestId).send_keys(MyIncomingUnsTransfers['result'][0]['id'])
        else:
            raise AssertionError("There is no Incoming uNS Transfers")

    def incomingUnsTransfer(self):
        self.driver.find_element(*MainPageLocators.lnk_incomingUnsTransfer).click()

    def outgoingUnsTransfer(self):
        self.driver.find_element(*MainPageLocators.lnk_outgoingUnsTransfer).click()

    def sendAuthorizationRequest(self):
        self.driver.find_element(*MainPageLocators.lnk_sendAuthorizationRequest).click()
        self.driver.find_element(*MainPageLocators.fld_sendAuthorizationRequestPk).send_keys(settings.random_public_key)
        self.driver.find_element(*MainPageLocators.fld_sendAuthorizationRequestMessage).send_keys("Send Auth request to random user")

    def acceptAuthorizationRequest(self):
        self.driver.find_element(*MainPageLocators.lnk_acceptAuthorizationRequest).click()
        self.driver.find_element(*MainPageLocators.fld_acceptAuthorizationRequestPk).send_keys(settings.random_public_key)
        self.driver.find_element(*MainPageLocators.fld_acceptAuthorizationRequestMessage).send_keys("Accept Auth request for random user")

    def rejectAuthorizationRequest(self):
        self.driver.find_element(*MainPageLocators.lnk_rejectAuthorizationRequest).click()
        self.driver.find_element(*MainPageLocators.fld_rejectAuthorizationRequestPk).send_keys(settings.random_public_key)
        self.driver.find_element(*MainPageLocators.fld_rejectAuthorizationRequestMessage).send_keys("Reject Auth resuest for random user")

    def deleteContact(self):
        self.driver.find_element(*MainPageLocators.lnk_deleteContact).click()
        self.driver.find_element(*MainPageLocators.fld_deleteContactPk).send_keys(settings.random_public_key)

    def getChannels(self):
        self.driver.find_element(*MainPageLocators.lnk_getChannels).click()
        self.driver.find_element(*MainPageLocators.fld_getChannels_filter).send_keys("") 
        self.driver.find_element(*MainPageLocators.fld_getChannels_channel_type).send_keys("2") # get my channels

    def getJoinedChannels(self):
        self.driver.find_element(*MainPageLocators.lnk_getJoinedChannels).click()

    def sendChannelMessage(self):
        self.joinChannel()
        self.enter_access_token()
        self.execute()
        self.driver.find_element(*MainPageLocators.lnk_sendChannelMessage).click()
        self.driver.find_element(*MainPageLocators.fld_sendChannelMessageId).send_keys(settings.channelid)
        self.driver.find_element(*MainPageLocators.fld_sendChannelMessageMessage).send_keys("html api automated test sending message to the channel")

    def joinChannel(self):
        self.driver.find_element(*MainPageLocators.lnk_joinChannel).click()
        self.driver.find_element(*MainPageLocators.fld_joinChannelIdent).send_keys(settings.channelid)
        self.driver.find_element(*MainPageLocators.fld_joinChannelPassword).send_keys(settings.channelPwd)

    def leaveChannel(self):
        self.driver.find_element(*MainPageLocators.lnk_leaveChannel).click()
        self.driver.find_element(*MainPageLocators.fld_leaveChannelId).send_keys(settings.channelid)

    def getChannelMessages(self):
        self.driver.find_element(*MainPageLocators.lnk_getChannelMessages).click()
        self.driver.find_element(*MainPageLocators.fld_getChannelMessages_channelid).send_keys(settings.channelid)

    def getChannelInfo(self):
        self.driver.find_element(*MainPageLocators.lnk_getChannelInfo).click()
        self.driver.find_element(*MainPageLocators.fld_getChannelInfo_channelid).send_keys(settings.channelid)

    def getChannelModerators(self):
        self.driver.find_element(*MainPageLocators.lnk_getChannelModerators).click()
        self.driver.find_element(*MainPageLocators.fld_getChannelModerators_channelid).send_keys(settings.channelid)

    def getChannelModeratorRight(self):
        self.getChannelModerators()
        self.enter_access_token()
        self.execute()
        ChannelModerators = self.getResponse()
        self.driver.find_element(*MainPageLocators.lnk_getChannelModeratorRight).click()
        self.driver.find_element(*MainPageLocators.fld_getChannelModeratorRight_channelid).send_keys(settings.channelid)
        self.driver.find_element(*MainPageLocators.fld_getChannelModeratorRight_moderator).send_keys(ChannelModerators['result'][0])

    def unsCreateRecordRequest(self):
        self.driver.find_element(*MainPageLocators.lnk_unsCreateRecordRequest).click()
        self.driver.find_element(*MainPageLocators.fld_unsCreateRecordRequestNick).send_keys(settings.random_uns)

    def unsModifyRecordRequest(self):
        self.unsRegisteredNames()
        self.enter_access_token()
        self.execute()
        MyUns = self.getResponse()
        self.driver.find_element(*MainPageLocators.lnk_unsModifyRecordRequest).click()
        self.driver.find_element(*MainPageLocators.fld_unsModifyRecordRequestNick).send_keys(MyUns['result'][-1]['nick'])
        self.driver.find_element(*MainPageLocators.fld_unsModifyRecordRequestValid).send_keys("")

    def unsDeleteRecordRequest(self):
        self.unsRegisteredNames()
        self.enter_access_token()
        self.execute()
        MyUns = self.getResponse()
        self.driver.find_element(*MainPageLocators.lnk_unsDeleteRecordRequest).click()
        self.driver.find_element(*MainPageLocators.fld_unsDeleteRecordRequestNick).send_keys(MyUns['result'][-1]['nick'])

    def unsSearchByPk(self):
        self.driver.find_element(*MainPageLocators.lnk_unsSearchByPk).click()
        self.driver.find_element(*MainPageLocators.fld_unsSearchByPkFilter).send_keys(settings.contactPk)

    def unsSearchByNick(self):
        self.driver.find_element(*MainPageLocators.lnk_unsSearchByNick).click()
        self.driver.find_element(*MainPageLocators.fld_unsSearchByNickFilter).send_keys("a")

    def getUnsSyncInfo(self):
        self.driver.find_element(*MainPageLocators.lnk_getUnsSyncInfo).click()

    def unsRegisteredNames(self):
        self.driver.find_element(*MainPageLocators.lnk_unsRegisteredNames).click()

    def summaryUnsRegisteredNames(self):
        self.driver.find_element(*MainPageLocators.lnk_summaryUnsRegisteredNames).click()
        self.driver.find_element(*MainPageLocators.fld_summaryUnsRegisteredNames_dateFrom).send_keys("1980-01-01")
        self.driver.find_element(*MainPageLocators.fld_summaryUnsRegisteredNames_dateTo).send_keys("2099-01-01")

    def clearTrayNotifications(self):
        self.driver.find_element(*MainPageLocators.lnk_clearTrayNotifications).click()

    def getNetworkConnections(self):
        self.driver.find_element(*MainPageLocators.lnk_getNetworkConnections).click()

    def getProxyMappings(self):
        self.driver.find_element(*MainPageLocators.lnk_getProxyMappings).click()

    def createProxyMapping(self):
        self.unsRegisteredNames()
        self.enter_access_token()
        self.execute()
        MyUns = self.getResponse()
        self.driver.find_element(*MainPageLocators.lnk_createProxyMapping).click()
        self.driver.find_element(*MainPageLocators.fld_createProxyMappingSrcHost).send_keys(MyUns['result'][-1]['nick'])
        self.driver.find_element(*MainPageLocators.fld_createProxyMappingSrcPort).send_keys("80")
        self.driver.find_element(*MainPageLocators.fld_createProxyMappingDstHost).send_keys("127.0.0.1")
        self.driver.find_element(*MainPageLocators.fld_createProxyMappingDstPort).send_keys("80")
        self.driver.find_element(*MainPageLocators.fld_createProxyMappingEnabled).send_keys("true")

    def enableProxyMapping(self):
        self.getProxyMappings()
        self.enter_access_token()
        self.execute()
        MyMapings = self.getResponse()
        self.driver.find_element(*MainPageLocators.lnk_enableProxyMapping).click()
        self.driver.find_element(*MainPageLocators.fld_enableProxyMappingMappingId).send_keys(MyMapings['result'][-1]['id'])

    def disableProxyMapping(self):
        self.getProxyMappings()        
        self.enter_access_token()
        self.execute()
        MyMapings = self.getResponse()
        self.driver.find_element(*MainPageLocators.lnk_disableProxyMapping).click()
        self.driver.find_element(*MainPageLocators.fld_disableProxyMappingMappingId).send_keys(MyMapings['result'][-1]['id'])

    def removeProxyMapping(self):
        self.getProxyMappings()
        self.enter_access_token()
        self.execute()
        MyMapings = self.getResponse()
        self.driver.find_element(*MainPageLocators.lnk_removeProxyMapping).click()
        self.driver.find_element(*MainPageLocators.fld_removeProxyMappingMappingId).send_keys(MyMapings['result'][-1]['id'])

    def lowTrafficMode(self):
        self.driver.find_element(*MainPageLocators.lnk_lowTrafficMode).click()

    def setLowTrafficMode(self):
        self.driver.find_element(*MainPageLocators.lnk_setLowTrafficMode).click()
        self.driver.find_element(*MainPageLocators.fld_setLowTrafficMode_bEnabled).send_keys("false")

    def getWhoIsInfo(self):
        self.driver.find_element(*MainPageLocators.lnk_getWhoIsInfo).click()
        self.driver.find_element(*MainPageLocators.fld_getWhoIsInfo_owner).send_keys(settings.contactPk)

    def requestTreasuryInterestRates(self):
        self.driver.find_element(*MainPageLocators.lnk_requestTreasuryInterestRates).click()

    def getTreasuryInterestRates(self):
        self.driver.find_element(*MainPageLocators.lnk_getTreasuryInterestRates).click()

    def requestTreasuryTransactionVolumes(self):
        self.driver.find_element(*MainPageLocators.lnk_requestTreasuryTransactionVolumes).click()

    def getTreasuryTransactionVolumes(self):
        self.driver.find_element(*MainPageLocators.lnk_getTreasuryTransactionVolumes).click()

    def getLicenses(self):
        self.driver.find_element(*MainPageLocators.lnk_getLicenses).click()

    def getContactLicenses(self):
        self.driver.find_element(*MainPageLocators.lnk_getContactLicenses).click()
        self.driver.find_element(*MainPageLocators.fld_getContactLicenses_pk).send_keys(settings.contactPk)

    def ucodeEncode(self):
        self.driver.find_element(*MainPageLocators.lnk_ucodeEncode).click()
        self.driver.find_element(*MainPageLocators.fld_ucodeEncode_hex_code).send_keys(settings.contactPk)
        self.driver.find_element(*MainPageLocators.fld_ucodeEncode_size_image).send_keys("200")
        self.driver.find_element(*MainPageLocators.fld_ucodeEncode_coder).clear()
        self.driver.find_element(*MainPageLocators.fld_ucodeEncode_coder).send_keys("HEX")
        self.driver.find_element(*MainPageLocators.fld_ucodeEncode_format).clear()
        self.driver.find_element(*MainPageLocators.fld_ucodeEncode_format).send_keys("PNG")

    def ucodeDecode(self):
        self.driver.find_element(*MainPageLocators.lnk_ucodeEncode).click()
        self.driver.find_element(*MainPageLocators.fld_ucodeEncode_hex_code).send_keys(settings.contactPk)
        #self.driver.find_element(*MainPageLocators.fld_ucodeEncode_size_image).send_keys("200")        
        self.enter_access_token()
        self.execute()
        base64_ucode = self.getResponse()
        self.driver.find_element(*MainPageLocators.lnk_ucodeDecode).click()
        self.driver.find_element(*MainPageLocators.fld_ucodeDecode_base64_image).send_keys(base64_ucode['result'])

    def createChannel(self):
        self.getChannels() # enshure that channel type is 2 (My channels)
        self.enter_access_token()
        self.execute()
        my_channels = self.getResponse()
        if len(my_channels["result"]) == 3:
            self.deleteChannel()
        try:
            self.driver.find_element(*MainPageLocators.lnk_createChannel).click()
            self.driver.find_element(*MainPageLocators.fld_createChannel_channel_name).send_keys("autotesting" + str(time.gmtime()))
            self.driver.find_element(*MainPageLocators.fld_createChannel_description).send_keys("This is channels was created by autotated api test")
            self.driver.find_element(*MainPageLocators.fld_createChannel_geoTag).send_keys("33.6373, 44.4690")
            self.driver.find_element(*MainPageLocators.fld_createChannel_hashtags).send_keys("tag1")
            self.driver.find_element(*MainPageLocators.fld_createChannel_languages).send_keys("")
            self.driver.find_element(*MainPageLocators.fld_createChannel_password).send_keys("")
            self.driver.find_element(*MainPageLocators.fld_createChannel_read_only).send_keys("")
            self.driver.find_element(*MainPageLocators.fld_createChannel_base64_avatar_image).send_keys("")
        except Exception:
            raise Exception("Can't create more then 3 channels")

    def modifyChannel(self):
        self.driver.find_element(*MainPageLocators.lnk_modifyChannel).click()
        self.driver.find_element(*MainPageLocators.fld_modifyChannel_channelid).send_keys(settings.channelid)
        self.driver.find_element(*MainPageLocators.fld_modifyChannel_description).send_keys("Channel was modifyed at: " + str(time.gmtime()))
        self.driver.find_element(*MainPageLocators.fld_modifyChannel_geoTag).send_keys("")
        self.driver.find_element(*MainPageLocators.fld_modifyChannel_hashtags).send_keys("")
        self.driver.find_element(*MainPageLocators.fld_modifyChannel_languages).send_keys("")
        self.driver.find_element(*MainPageLocators.fld_modifyChannel_read_only).send_keys("")

    def deleteChannel(self):
        self.getChannels() # enshure that channel type is 2 (My channels)
        self.enter_access_token()
        self.execute()
        my_channels = self.getResponse()
        channel_for_deleting = ""
        if len(my_channels["result"]) < 3:
            self.createChannel()
            res = self.getResponse()
            if not "error" in res:
                channel_for_deleting = res["result"]
            else:
                raise AssertionError("There is error in response")
        else:
            for channel in my_channels["result"]:
                if "autotesting" in channel["name"]:
                    channel_for_deleting = channel["channelid"]
        if channel_for_deleting != "":
            self.driver.find_element(*MainPageLocators.lnk_deleteChannel).click()
            self.driver.find_element(*MainPageLocators.fld_deleteChannel_channelid).send_keys(channel_for_deleting)
        else:
            raise Exception("Nothing available for deleting")

    def sendChannelPicture(self):
        self.joinChannel()
        self.enter_access_token()
        self.execute()
        self.driver.find_element(*MainPageLocators.lnk_sendChannelPicture).click()
        self.driver.find_element(*MainPageLocators.fld_sendChannelPicture_channelid).send_keys(settings.channelid)
        pyperclip.copy(settings.picture)
        self.driver.find_element(*MainPageLocators.fld_sendChannelPicture_base64_image).click()
        p.hotkey('ctrl', 'v')
        self.driver.find_element(*MainPageLocators.fld_sendChannelPicture_filename_image).send_keys("Python test image.png")

    def getChannelSystemInfo(self):
        self.driver.find_element(*MainPageLocators.lnk_getChannelSystemInfo).click()

    def setWebSocketState(self):
        self.driver.find_element(*MainPageLocators.lnk_setWebSocketState).click()
        self.driver.find_element(*MainPageLocators.fld_setWebSocketStatePort).send_keys(settings.wsPort)
        self.driver.find_element(*MainPageLocators.fld_setWebSocketStateEnabled).send_keys("true")

    def getWebSocketState(self):
        self.driver.find_element(*MainPageLocators.lnk_getWebSocketState).click()

    def getChannelContacts(self):
        self.driver.find_element(*MainPageLocators.lnk_getChannelContacts).click()
        self.driver.find_element(*MainPageLocators.fld_getChannelContacts_channelid).send_keys(settings.channelid)
    
    def enter_access_token(self):
        self.driver.find_element(*MainPageLocators.fld_token).clear()
        self.driver.find_element(*MainPageLocators.fld_token).send_keys(settings.token)

    def execute(self):
        time.sleep(0.2)
        self.driver.find_element(*MainPageLocators.btn_Execute).click()
        time.sleep(0.5)

    def no_errors_in_response(self):
        response = self.getResponse()
        if (settings.debug):
            print("***DEBUG: response result: " + str(response["result"]))
        if not "error" in response:
            return response["result"] != ""                
        else:
            if (settings.debug):
                print("***DEBUG: check errors in response: " + str(response))
            return False

    def getResponse(self):
        timer = 10
        res = "error"
        while (self.driver.find_element(*MainPageLocators.txt_Response).text == "-"):
            if timer != 0:
                time.sleep(0.5)
                timer -= 0.5
            else:
                break
        try:
            self.driver.find_element(*MainPageLocators.txt_Response).click() # check if response is available
            res = json.loads(self.driver.find_element(*MainPageLocators.txt_Response).text)
        except exceptions.ElementNotVisibleException:       
            raise Exception("Response is not available") from None  
        except json.JSONDecodeError:
            if (settings.debug):
                print("***DEBUG: response: " + str(self.driver.find_element(*MainPageLocators.txt_Response).text))
            raise Exception("Can't read response as JSON") from None
        except Exception:
            if (settings.debug):
                print("***DEBUG: response: " + str(self.driver.find_element(*MainPageLocators.txt_Response).text))
            raise Exception("unknown exception when read responce") from None        
        self.driver.refresh() # костыль
        return res