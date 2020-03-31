from tabula import read_pdf
import pandas as pd
import glob

allowed_vals = ["total assets", "fixed assets", "total capital", "total income", "total expenses"]




def check(x):

	for v in allowed_vals:

		if str(x).lower().strip() == v:
			# print("!! " + v + "  " + str(x).lower())
			return True, v


		# for word in str(item).split():
		# 	if word in
	return False, v



def readReport(reportName):
	df = read_pdf(reportName, pages="all")

	print("----------------------------\n" + reportName + "\n----------------------------\n")
	for table in df:

		print(table)


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
				c, v = check(item)
				if c:
					filtered_rows.append([v, row])
		#print(cols)
		print(filtered_rows)
		vals = {
			"2016": -1,
			"2017": -1,
			"2018": -1,
			"2019": -1

		}
		for row in rows:
			for i, item in enumerate(row):
				for val in vals:

					if val in str(item) and vals[val] == -1:
						vals[val] = i


		for obj in filtered_rows:
			row = obj[1]
			object = obj[0]

			for val in vals:
				if vals[val] != -1:
					print("in " + val + ", our organisation's " + object + " was " + row[vals[val]])

		#
		# for row in filtered_rows:
		# 	print(row)
		#
		# if filtered_rows != []:
		# 	print(table)

		# print("---------------Cols---------------")
		# for col in cols:
		#     print(col)
		print("------------------------------")
	print("\n----------------------------------------------------------------------------------\n")



def main():
	pd.set_option('display.max_columns', 300)
	files = glob.glob("reports/*.pdf")

	# for file in files:
	# 	readReport(file)
	readReport("reports left to do/tanzania-2018.pdf")








main()