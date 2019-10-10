import unittest
import selenium
from selenium import webdriver
import page

class MyTestResult(unittest.TestResult):
    def addFailure(self, test, err):
        #print(str(test) + ": " + str(err))
        test_name = str(test).split(" ")[0]
        print(str(test_name) + ": Failed")
        super(MyTestResult, self).addFailure(test, err)

    def addError(self, test, err):
        test_name = str(test).split(" ")[0]
        print(str(test_name) + ": " + str(err[1]))        
        super(MyTestResult, self).addError(test, err)


class AllMethodsTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("driver/chromedriver.exe")
        #self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://127.0.0.1:"+page.settings.apiPort+"/api/help")        
        self.main_page = page.MainPage(self.driver)

    def test_getSystemInfo(self):        
        self.main_page.getSystemInfo()
        
    def test_getProfileStatus(self):
        self.main_page.getProfileStatus()
    
    def test_setProfileStatus(self):
        self.main_page.setProfileStatus()
    
    def test_getOwnContact(self):
        self.main_page.getOwnContact()

    def test_getContacts(self):
        self.main_page.getContacts()

    def test_getContactAvatar(self):
        self.main_page.getContactAvatar()

    def test_getChannelAvatar(self):
        self.main_page.getChannelAvatar()

    def test_setContactGroup(self):
        self.main_page.setContactGroup()

    def test_setContactNick(self):
        self.main_page.setContactNick()

    def test_sendInstantMessage(self):
        self.main_page.sendInstantMessage()

    def test_sendInstantQuote(self):
        self.main_page.sendInstantQuote()

    def test_sendInstantSticker(self):
        self.main_page.sendInstantSticker()

    def test_sendInstantBuzz(self):
        self.main_page.sendInstantBuzz()

    def test_sendInstantInvitation(self):
        self.main_page.sendInstantInvitation()

    def test_removeInstantMessages(self):
        self.main_page.removeInstantMessages()

    def test_getContactMessages(self):
        self.main_page.getContactMessages()

    def test_sendEmailMessage(self):
        self.main_page.sendEmailMessage()

    def test_sendPaymentPkToPk(self):
        self.main_page.sendPaymentPkToPk()

    def test_sendPaymentCardToPk(self):
        self.main_page.sendPaymentCardToPk()

    def test_sendPaymentCardToCard(self):
        self.main_page.sendPaymentCardToCard()

    def test_getEmailFolder(self):
        self.main_page.getEmailFolder()

    def test_getEmails(self):
        self.main_page.getEmails()

    def test_getEmailById(self):
        self.main_page.getEmailById()

    def test_deleteEmail(self):
        self.main_page.deleteEmail()

    def test_sendReplyEmailMessage(self):
        self.main_page.sendReplyEmailMessage()

    def test_sendForwardEmailMessage(self):
        self.main_page.sendForwardEmailMessage()

    def test_getFinanceSystemInformation(self):
        self.main_page.getFinanceSystemInformation()

    def test_getBalance(self):
        self.main_page.getBalance()

    def test_getFinanceHistory(self):
        self.main_page.getFinanceHistory()

    def test_getCards(self):
        self.main_page.getCards()

    def test_addCard(self):
        self.main_page.addCard()

    def test_deleteCard(self):
        self.main_page.deleteCard()

    def test_enableMining(self):
        self.main_page.enableMining()

    def test_enableInterest(self):
        self.main_page.enableInterest()

    def test_enableHistoryMining(self):
        self.main_page.enableHistoryMining()

    def test_statusHistoryMining(self):
        self.main_page.statusHistoryMining()

    def test_getMiningBlocks(self):
        self.main_page.getMiningBlocks()

    def test_getMiningInfo(self):
        self.main_page.getMiningInfo()

    def test_getVouchers(self):
        self.main_page.getVouchers()

    def test_createVoucher(self):
        self.main_page.createVoucher()

    def test_useVoucher(self):
        self.main_page.useVoucher()

    def test_deleteVoucher(self):
        self.main_page.deleteVoucher()

    def test_getInvoices(self):
        self.main_page.getInvoices()

    def test_getInvoiceByReferenceNumber(self):
        self.main_page.getInvoiceByReferenceNumber()

    def test_getTransactionIdByReferenceNumber(self):
        self.main_page.getTransactionIdByReferenceNumber()

    def test_sendInvoice(self):
        self.main_page.sendInvoice()

    def test_acceptInvoice(self):
        self.main_page.acceptInvoice()

    def test_declineInvoice(self):
        self.main_page.declineInvoice()

    def test_cancelInvoice(self):
        self.main_page.cancelInvoice()

    def test_requestUnsTransfer(self):
        self.main_page.requestUnsTransfer()

    def tyst_acceptUnsTransfer(self):
        self.main_page.acceptUnsTransfer()

    def test_declineUnsTransfer(self):
        self.main_page.declineUnsTransfer()

    def test_outgoingUnsTransfer(self):
        self.main_page.outgoingUnsTransfer()

    def test_sendAuthorizationRequest(self):
        self.main_page.sendAuthorizationRequest()

    def test_acceptAuthorizationRequest(self):
        self.main_page.acceptAuthorizationRequest()

    def test_rejectAuthorizationRequest(self):
        self.main_page.rejectAuthorizationRequest()

    def test_deleteContact(self):
        self.main_page.deleteContact()

    def test_getChannels(self):
        self.main_page.getChannels()
    
    def test_sendChannelMessage(self):
        self.main_page.sendChannelMessage()
            
    def test_leaveChannel(self):
        self.main_page.leaveChannel()

    def test_joinChannel(self):
        self.main_page.joinChannel()

    def test_getChannelMessages(self):
        self.main_page.getChannelMessages()

    def test_getChannelInfo(self):
        self.main_page.getChannelInfo()

    def test_getChannelModerators(self):
        self.main_page.getChannelModerators()

    def test_getChannelModeratorRight(self):
        self.main_page.getChannelModeratorRight()

    def test_unsCreateRecordRequest(self):
        self.main_page.unsCreateRecordRequest()

    def test_unsModifyRecordRequest(self):
        self.main_page.unsModifyRecordRequest()

    def test_unsDeleteRecordRequest(self):
        self.main_page.unsDeleteRecordRequest()

    def test_unsSearchByPk(self):
        self.main_page.unsSearchByPk()

    def test_unsSearchByNick(self):
        self.main_page.unsSearchByNick()

    def test_getUnsSyncInfo(self):
        self.main_page.getUnsSyncInfo()

    def test_unsRegisteredNames(self):
        self.main_page.unsRegisteredNames()

    def test_summaryUnsRegisteredNames(self):
        self.main_page.summaryUnsRegisteredNames()

    def test_clearTrayNotifications(self):
        self.main_page.clearTrayNotifications()

    def test_getNetworkConnections(self):
        self.main_page.getNetworkConnections()

    def test_getProxyMappings(self):
        self.main_page.getProxyMappings()

    def test_createProxyMapping(self):
        self.main_page.createProxyMapping()

    def test_enableProxyMapping(self):
        self.main_page.enableProxyMapping()

    def test_disableProxyMapping(self):
        self.main_page.disableProxyMapping()

    def test_removeProxyMapping(self):
        self.main_page.removeProxyMapping()

    def test_lowTrafficMode(self):
        self.main_page.lowTrafficMode()

    def test_setLowTrafficMode(self):
        self.main_page.setLowTrafficMode()

    def test_getWhoIsInfo(self):
        self.main_page.getWhoIsInfo()

    def test_requestTreasuryInterestRates(self):
        self.main_page.requestTreasuryInterestRates()

    def test_getTreasuryInterestRates(self):
        self.main_page.getTreasuryInterestRates()

    def test_requestTreasuryTransactionVolumes(self):
        self.main_page.requestTreasuryTransactionVolumes()

    def test_getTreasuryTransactionVolumes(self):
        self.main_page.getTreasuryTransactionVolumes()
        
    def test_ucodeEncode(self):
        self.main_page.ucodeEncode()

    def test_ucodeDecode(self):
        self.main_page.ucodeDecode()

    def test_createChannel(self):
        self.main_page.createChannel()

    def test_modifyChannel(self):
        self.main_page.modifyChannel()

    def test_deleteChannel(self):
        self.main_page.deleteChannel()

    def test_sendChannelPicture(self):
        self.main_page.sendChannelPicture()

    def test_getChannelSystemInfo(self):
        self.main_page.getChannelSystemInfo()

    def test_setWebSocketState(self):
        self.main_page.setWebSocketState()

    def test_getWebSocketState(self):
        self.main_page.getWebSocketState()

    def test_clearTrayNotifications(self):
        self.main_page.clearTrayNotifications()

    def test_getChannelContacts(self):
        self.main_page.getChannelContacts()

    def tearDown(self):
        self.main_page.enter_access_token()
        self.main_page.execute()
        assert self.main_page.no_errors_in_response(), "There is Error in Response"
        self.driver.close()


            
if __name__ == "__main__":
    unittest.main(testRunner=unittest.TextTestRunner(resultclass=MyTestResult))