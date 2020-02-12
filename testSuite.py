import Model
import Controller
import HandleDictionary
import os
import filecmp




def setUp():
    configurationFile = open("configuration.txt", "r")
    subscription_key = configurationFile.readline().rstrip("\n\r")
    endpoint = configurationFile.readline().rstrip("\n\r")
    configurationFile.close()
    ocr_url = endpoint + "vision/v2.1/ocr"

    Model.assaginaAuthenticationCredentials(subscription_key, endpoint, ocr_url)



def testTraining():
    output = """{'of': 12, 'programme': 11, 'Total': 11, 'expenses': 10, 'Programme': 9, 'loans': 9, 'income': 9, 'assets': 8, 'Cash': 8, 'Net': 7, 'total': 6, 'balances': 6, 'investments': 6, '-': 6, 'Surplus': 6, 'Income': 6, 'Assets': 5, 'term': 5, 'Social': 5, 'financial': 5, 'grants': 5, 'cash': 5, 'net': 5, 'deposits': 5, 'liabilities': 5, 'equipment': 5, 'bank': 5, 'ASSETS': 4, 'TOTAL': 4, 'Liabilities': 4, 'Grants': 4, 'year': 4, 'deficit': 4, 'Community': 4, 'House': 4, 'expenditure': 4, 'activities': 4, 'property': 4, 'reserves': 3, 'balance': 3, 'project': 3, 'Expenses': 3, 'Current': 3, 'Restricted': 3, 'capital': 3, 'parties': 3, 'LIABILITIES': 3, 'NET': 3, 'Development': 3, 'Property': 3, 'BRAC': 3, 'Education': 3, 'Investment': 3, 'development': 3, 'operating': 3, 'fixed': 3, 'advances': 3, 'taxation': 3, 'Adjustments': 3, 'accounts': 3, 'gross': 2, 'earmarked': 2, 'result': 2, 'benefits': 2, 'Interfund': 2, 'Deferred': 2, 'equivalents': 2, 'increase': 2, 'customers': 2, 'funds': 2, 'sale': 2, 'short': 2, 'Tax': 2, 'deduction': 2, 'ACTIVITIES': 2, 'current': 2, 'Security': 2, 'Enterprises': 2, 'INCOME': 2, 'EXPENDITURE': 2, 'surplus': 2, 'enterprises': 2, 'contribution': 2, 'changes': 2, 'service': 2, 'fund': 2, 'investing': 2, 'Purchase': 2, 'motorcycle': 2, 'Decrease': 2, 'Dépenses': 2, 'totales': 2, 'Project': 1, 'majority': 1, 'IRCS': 1, 'Operating': 1, 'revenue': 1, 'pretax': 1, 'profit': 1, 'USD': 1, 'gren': 1, 'Impairment': 1, 'Losses': 1, 'reserve': 1, 'administrative': 1, 'Financial': 1, 'Position': 1, 'systems': 1, 'Gross': 1, 'portfolio': 1, 'IRCs': 1, 'liquidity': 1, 'profitable': 1, 'encouraging': 1, 'closed': 1, 'general': 1, 'unemployment': 1, 'IRC': 1, 'long-time': 1, 'obligations': 1, 'FINANCIAL': 1, 'HIGHLIGHTS': 1, 'NGO': 1, 'Tanzania': 1, 'website': 1, 'annual': 1, 'growth': 1, 'equity': 1, 'direct': 1, 'costs': 1, 'partner': 1, 'organisations': 1, 'associates': 1, 'Half': 1, 'consultants': 1, 'positive': 1, 'sheet': 1, 'risk': 1, 'bearer': 1, 'unernployment': 1, 'ICT': 1, 'system': 1, 'programe': 1, 'goals': 1, 'NORAD': 1, 'Provisions': 1, 'LEGO': 1, 'Foundation': 1, 'necessary': 1, 'refurbishments': 1, 'bad': 1, 'debt': 1, 'Secunty': 1, 'office': 1, 'budget': 1, 'India': 1, 'profitability': 1, 'mission': 1, 'DGS': 1, 'Programmatic': 1, 'Funding': 1, 'program': 1, 'early': 1, 'disbursements': 1, 'DGIS': 1, 'meeting': 1, 'venues': 1, 'Hogue': 1, 'major': 1, 'adjustments': 1, 'days': 1, 'travel': 1, 'ambitions': 1, 'number': 1, 'borrowers': 1, 'years': 1, 'increment': 1, 'period': 1, 'trend': 1, 'Non-Current': 1, 'Loans': 1, 'gratuity': 1, 'Program': 1, 'oul': 1, 'liability': 1, 'COMMITEMENTS': 1, 'utNized': 1, 'bes': 1, 'Short-term': 1, 'unrestricted': 1, 'Unrealized': 1, 'gain': 1, 'shon': 1, 'investrnent': 1, 'CONTINGENCIES': 1, 'receiv': 1, 'Year': 1, 'CASH': 1, 'FLOWS': 1, 'source': 1}"""
    Controller.train("testing" + os.path.sep + "TrainingInput")
    assert(str(Model.keywordDict) == output)


def testExtraction():
    assert(str(Controller.extract("testing" + os.path.sep + "ExtractionInput")) == """[['1:2.0', '2:15.0', '3:18.5', '4:26.0', '5:7.0', '6:36.0', '7:28.0', '8:57.5', '9:18.0', '10:18.0', '11:11.5', '12:1.0', '13:57.5', '14:31.5', '15:1.5', '16:55.5', '17:19.5', '18:1.5', '19:54.0', '20:17.5', '21:1.5', '22:51.0', '23:30.5', '24:11.0', '25:26.5', '26:53.5', '27:51.0', '28:58.5', '29:62.5', '30:59.5', '31:69.5', '32:100.5', '33:72.0', '34:70.5', '35:81.5', '36:74.5', '37:68.5', '38:70.0', '39:27.0', '40:28.0', '41:34.5', '42:74.5', '43:96.0', '44:75.0', '45:79.5', '46:38.0', '47:17.5', '48:69.5', '49:22.5', '50:30.5', '51:25.5', '52:22.5', '53:52.0', '54:22.0']]""")


def testStoreTrainingData():
    try:
        os.remove("/Users/markanson/dev/team_36_dev/testing/pickles/store.pickle")
    except:
        pass
    print(Model.keywordDict)
    print(Model.generalDict)
    Controller.storeTrainingData("/Users/markanson/dev/team_36_dev/testing/pickles", "store")
    assert(filecmp.cmp("/Users/markanson/dev/team_36_dev/testing/pickles/store.pickle", "/Users/markanson/dev/team_36_dev/testing/pickles/storeExample.pickle"))


def testFetchTrainingData():
    Model.keywordDict = {}
    Model.generalDict = {}

    Controller.fetchTrainingData("/Users/markanson/dev/team_36_dev/testing/pickles", "storeExample")
    assert(str(Model.keywordDict) == """{'of': 12, 'programme': 11, 'Total': 11, 'expenses': 10, 'Programme': 9, 'loans': 9, 'income': 9, 'assets': 8, 'Cash': 8, 'Net': 7, 'total': 6, 'balances': 6, 'investments': 6, '-': 6, 'Surplus': 6, 'Income': 6, 'Assets': 5, 'term': 5, 'Social': 5, 'financial': 5, 'grants': 5, 'cash': 5, 'net': 5, 'deposits': 5, 'liabilities': 5, 'equipment': 5, 'bank': 5, 'ASSETS': 4, 'TOTAL': 4, 'Liabilities': 4, 'Grants': 4, 'year': 4, 'deficit': 4, 'Community': 4, 'House': 4, 'expenditure': 4, 'activities': 4, 'property': 4, 'reserves': 3, 'balance': 3, 'project': 3, 'Expenses': 3, 'Current': 3, 'Restricted': 3, 'capital': 3, 'parties': 3, 'LIABILITIES': 3, 'NET': 3, 'Development': 3, 'Property': 3, 'BRAC': 3, 'Education': 3, 'Investment': 3, 'development': 3, 'operating': 3, 'fixed': 3, 'advances': 3, 'taxation': 3, 'Adjustments': 3, 'accounts': 3, 'gross': 2, 'earmarked': 2, 'result': 2, 'benefits': 2, 'Interfund': 2, 'Deferred': 2, 'equivalents': 2, 'increase': 2, 'customers': 2, 'funds': 2, 'sale': 2, 'short': 2, 'Tax': 2, 'deduction': 2, 'ACTIVITIES': 2, 'current': 2, 'Security': 2, 'Enterprises': 2, 'INCOME': 2, 'EXPENDITURE': 2, 'surplus': 2, 'enterprises': 2, 'contribution': 2, 'changes': 2, 'service': 2, 'fund': 2, 'investing': 2, 'Purchase': 2, 'motorcycle': 2, 'Decrease': 2, 'Dépenses': 2, 'totales': 2, 'Project': 1, 'majority': 1, 'IRCS': 1, 'Operating': 1, 'revenue': 1, 'pretax': 1, 'profit': 1, 'USD': 1, 'gren': 1, 'Impairment': 1, 'Losses': 1, 'reserve': 1, 'administrative': 1, 'Financial': 1, 'Position': 1, 'systems': 1, 'Gross': 1, 'portfolio': 1, 'IRCs': 1, 'liquidity': 1, 'profitable': 1, 'encouraging': 1, 'closed': 1, 'general': 1, 'unemployment': 1, 'IRC': 1, 'long-time': 1, 'obligations': 1, 'FINANCIAL': 1, 'HIGHLIGHTS': 1, 'NGO': 1, 'Tanzania': 1, 'website': 1, 'annual': 1, 'growth': 1, 'equity': 1, 'direct': 1, 'costs': 1, 'partner': 1, 'organisations': 1, 'associates': 1, 'Half': 1, 'consultants': 1, 'positive': 1, 'sheet': 1, 'risk': 1, 'bearer': 1, 'unernployment': 1, 'ICT': 1, 'system': 1, 'programe': 1, 'goals': 1, 'NORAD': 1, 'Provisions': 1, 'LEGO': 1, 'Foundation': 1, 'necessary': 1, 'refurbishments': 1, 'bad': 1, 'debt': 1, 'Secunty': 1, 'office': 1, 'budget': 1, 'India': 1, 'profitability': 1, 'mission': 1, 'DGS': 1, 'Programmatic': 1, 'Funding': 1, 'program': 1, 'early': 1, 'disbursements': 1, 'DGIS': 1, 'meeting': 1, 'venues': 1, 'Hogue': 1, 'major': 1, 'adjustments': 1, 'days': 1, 'travel': 1, 'ambitions': 1, 'number': 1, 'borrowers': 1, 'years': 1, 'increment': 1, 'period': 1, 'trend': 1, 'Non-Current': 1, 'Loans': 1, 'gratuity': 1, 'Program': 1, 'oul': 1, 'liability': 1, 'COMMITEMENTS': 1, 'utNized': 1, 'bes': 1, 'Short-term': 1, 'unrestricted': 1, 'Unrealized': 1, 'gain': 1, 'shon': 1, 'investrnent': 1, 'CONTINGENCIES': 1, 'receiv': 1, 'Year': 1, 'CASH': 1, 'FLOWS': 1, 'source': 1}""")
    assert(str(Model.generalDict) == """{'and': 59, 'in': 50, 'of': 31, 'the': 26, 'to': 22, 'for': 20, 'USD': 14, 'from': 13, 'cash': 12, 'Total': 12, 'by': 11, '2018': 10, 'programme': 10, 'loans': 10, 'on': 10, 'deposits': 10, 'expenses': 10, '€': 9, 'Programme': 9, '-': 9, 'assets': 9, 'Net': 9, 'income': 9, 'as': 9, 'against': 8, 'year': 8, 'Cash': 8, 'is': 7, 'total': 7, 'other': 7, 'liabilities': 7, 'grants': 7, 'net': 7, 'Income': 7, 'a': 6, 'was': 6, 'at': 6, 'balances': 6, 'Grants': 6, 'with': 6, 'operating': 6, 'received': 6, '2017.': 5, 'Assets': 5, 'The': 5, 'equivalents': 5, 'ASSETS': 5, 'TOTAL': 5, 'Social': 5, 'financial': 5, 'Increase': 5, 'This': 4, 'IRC': 4, 'earmarked': 4, 'increase': 4, 'an': 4, 'Deferred': 4, 'LIABILITIES': 4, 'NET': 4, 'term': 4, 'Investments': 4, 'Community': 4, 'House': 4, 'investments': 4, 'before': 4, 'expenditure': 4, 'property,': 4, 'plant': 4, '2017': 3, 'were': 3, 'balance': 3, 'gross': 3, 'million': 3, 'during': 3, 'project': 3, 'Operating': 3, 'Expenses': 3, 'Current': 3, 'capital': 3, 'Restricted': 3, 'Tax': 3, 'deduction': 3, 'source': 3, 'Development': 3, 'BRAC': 3, 'Education': 3, 'development': 3, 'activities': 3, 'over': 3, 'taxation': 3, 'activities:': 3, 'equipment': 3, 'fixed': 3, 'accounts': 3, '/': 3, 'Tanzania': 2, 'due': 2, 'impairment': 2, '8%': 2, 'amount': 2, 'In': 2, '2018,': 2, 'increased': 2, '12%': 2, 'result': 2, 'being': 2, 'its': 2, 'partner': 2, 'associates': 2, 'consultants.': 2, 'revenue': 2, 'went': 2, 'including': 2, 'almost': 2, 'closed': 2, 'reserves.': 2, 'ICT': 2, '2018.': 2, 'reserves': 2, 'IRCs': 2, 'liquidity': 2, '&': 2, 'Interfund': 2, 'customers': 2, 'used': 2, 'CASH': 2, 'FLOWS': 2, 'FROM': 2, 'ACTIVITIES': 2, 'sale': 2, 'current': 2, 'generated': 2, 'in)': 2, 'paid': 2, 'short': 2, 'third': 2, 'parties': 2, 'AND': 2, 'INCOME': 2, 'Enterprises': 2, 'Property': 2, 'EXPENDITURE': 2, 'Liabilities': 2, 'enterprises': 2, 'contribution': 2, 'property': 2, 'flows': 2, 'Adjustments': 2, 'provided': 2, 'disposal': 2, 'investment': 2, 'motorcycle': 2, 'Interest': 2, 'bank': 2, 'microfinance': 2, 'Decrease/0ncrease)': 2, 'related': 2, 'undertakings': 2, 'totales': 2, 'du': 2, 'completed': 1, 'profitable': 1, 'registering': 1, 'pretax': 1, 'profit': 1, '6,900,841': 1, 'compared': 1, '6,571': 1, ',041': 1, 'mainly': 1, 'number': 1, 'borrowers': 1, '183,103': 1, '197,172': 1, '8%.': 1, '10,365,788': 1, 'Provisions': 1, 'Impairment': 1, 'Losses': 1, 'reserve': 1, '2,377,559': 1, '2,206,978': 1, '2017,': 1, 'increment': 1, 'representing': 1, '3%': 1, 'Gross': 1, 'portfolio': 1, 'charged': 1, '768,128': 1, '1,398,838': 1, 'Portfolio': 1, 'Risk': 1, '(PAR>30': 1, 'days)': 1, 'has': 1, 'gone': 1, 'down': 1, '2.69%': 1, '3': 1}""")



def testVersioning():
   Model.keywordDict = {1: test}
   Model.generalDict = {2: test}

   Controller.storeTrainingData("/Users/markanson/dev/team_36_dev/testing/pickles", "store")

   print(Model.keywordDict)
   print(Model.keywordDict)

   Controller.revert("/Users/markanson/dev/team_36_dev/testing/pickles", "store")

   print(Model.keywordDict)
   print(Model.keywordDict)



def test(name, f):
    print(name + "...")
    f()
    print("done\n")



if __name__ == "__main__":
    test("setting up", setUp)

    test("testing training", testTraining)

    test("testing extraction", testExtraction)

    test("testing storing", testStoreTrainingData)

    test("testing fetching", testFetchTrainingData)

    test("testing versioning", testVersioning)