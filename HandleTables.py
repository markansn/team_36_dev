from tabula import read_pdf
import pandas as pd
import glob

allowed_vals = ["total assets", "fixed assets", "total capital", "total income", "total expenses"]




def check(x):

    for v in allowed_vals:

        if str(x).lower().strip() == v:
            print("!! " + v + "  " + str(x).lower())
            return True


        # for word in str(item).split():
        # 	if word in
    return False



def readReport(reportName):
    df = read_pdf(reportName, pages="all")

    print("----------------------------\n" + reportName + "\n----------------------------\n")
    for table in df:

        
        cols = table.columns.tolist()
        rows = table.values.tolist()


        # rows2 = [x for x in rows if check(x)]
        #
        # print(cols)
        # for row in rows2:
        #     print(row)

        filtered_rows = []
        for row in rows:
            for item in row:
                if check(item):
                    filtered_rows.append(row)
        #print(cols)
        for row in filtered_rows:
            print(row)
    print("\n------------------\n")



def main():
    pd.set_option('display.max_columns', 300)
    files = glob.glob("reports/*.pdf")

    for file in files:
        readReport(file)







main()