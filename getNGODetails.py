import Model
import glob
import json
import string
from io import BytesIO
from PIL import Image
import pickle
import pymysql
from tqdm import tqdm
# import nltk
# from nltk.corpus import words as nltk_words
# nltk.download('words')
# dictionary = dict.fromkeys(nltk_words.words(), None)

# def is_english_word(word): #credit https://stackoverflow.com/questions/3788870/how-to-check-if-a-word-is-an-english-word-with-python
#
#     try:
#         x = dictionary[word]
#         return True
#     except KeyError:
#         return False


setofwords = set(line.strip() for line in open(
	'allEnglishWords.txt'))  # credit https://stackoverflow.com/questions/874017/python-load-words-from-file-into-a-set
punctuation = str.maketrans(dict.fromkeys(string.punctuation)) #credit https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string


connection = pymysql.connect(host='',
                             user='',
                             password='',
                             db='',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)




def getImgSize(img):
	return createImageBuffer(img).tell()

def createImageBuffer(img):
	img_file = BytesIO()
	img.save(img_file, 'jpeg', quality=90)
	return img_file

def reduceImageSize(img):

	img_file = createImageBuffer(img)
	return Image.open(img_file)


def getTextFromImage(img):
	text = []


	img_file = BytesIO()
	img.save(img_file, 'jpeg')
	img_file_size = img_file.tell() #credit  https://stackoverflow.com/questions/11904083/how-to-get-image-size-bytes-using-pil


	if img_file_size < 1000000:


		img = Image.open(img_file)

		data = Model.OCR(img).json()

		data = Model.ConvertToJSON(data)

		json_dict = json.loads(data)
		regions = json_dict['regions']

		for region in regions:
			lines = region['lines']
			for line in lines:
				words = line['words']
				for word in words:
					text.append(word['text'])
		return text
	else:
		print("!Warn: file too big to read")

	return []



def getWordsOnPage(page, images, word_exists):
	text = []
	first_page = None
	try:
		first_page = getTextFromImage(images[0][page])
	except:
		return []

	# for img in images[0]:
	#
	#     text = getTextFromImage(img)

	words_on_first_page = []
	banned_words = ["annual", "report", "", " ", "results", "reports"]
	for word in first_page:
		# print(word)
		#print(word)
		# if '@' in word.lower() or "www." in word.lower() or ".org" in word.lower():
		#     print(word)


		word = word.lower().translate(punctuation)

		# if not word_exists:
		#
		#     if word not in setofwords and not word.isdigit():
		#         words_on_first_page.append(word)
		# else:
		#     if not word.isdigit:
		#         words_on_first_page.append(word)
		if word not in banned_words:
			words_on_first_page.append(word)
	return words_on_first_page


def possible_name_in_file_name(word, reportName):
	return word.lower() in reportName.lower()

def get_matching_words_from_urls(images, words_on_first_page):
	words_matching_urls = []

	images[0].reverse()
	for img in images[0]:
		text = getTextFromImage(img)

		urls = []
		for word in text:
			if '@' in word.lower():
				split_word = word.split("@")
				# if word.lower() in split_word[1]:
				#     urls.append(word)
				urls.append(split_word[1])
			elif "www." in word.lower() or ".org" in word.lower():
				split_word = word.split(".")
				if split_word[0] == "www" or "http" in split_word[0]:
					urls.append(split_word[1])
				else:
					urls.append(word)

		for url in urls:
			# print(url)
			for possible_name in words_on_first_page:
				if possible_name in url and len(possible_name) > 3:
					words_matching_urls.append(possible_name)

			if words_matching_urls != []:
				return words_matching_urls

	return []

def get_matching_words_from_file_name(words_on_first_page, reportName):
	words_in_file_name = []
	for word in words_on_first_page:
		if possible_name_in_file_name(word, reportName) and not word.isdigit():
			words_in_file_name.append(word)

	if words_in_file_name != []:
		return words_in_file_name

	return []


def concat_words(i):

	string = ""
	for item in i:
		string = string + item + " "
	return string

def readReport(reportName):
	images = Model.pdfsIterator([reportName])

	words_on_first_page = getWordsOnPage(0, images, True) + getWordsOnPage(1, images, True) + getWordsOnPage(2, images, True)

	words_on_first_page = list(dict.fromkeys(words_on_first_page))

	# if len(words_on_first_page) == 0:
	#     return "no names found on first page"



	# print(words_on_first_page)

	matching_words_from_urls = get_matching_words_from_urls(images, words_on_first_page)

	if matching_words_from_urls == []:
		matching_words_from_file_name = get_matching_words_from_file_name(words_on_first_page, reportName)

		if matching_words_from_urls != []:
			return concat_words(matching_words_from_file_name), words_on_first_page

	if matching_words_from_urls != []:
		return concat_words(matching_words_from_urls), words_on_first_page



	return "none", words_on_first_page






	# return "found " + str(words_on_first_page) + " but none could be verified"


def upload_pdf(file, answer):
	try:
		with connection.cursor() as cursor:
			# Create a new record
			sql = "INSERT INTO `pdfs` (`PDF_NAME`, `NGO_NAME`) VALUES (%s, %s)"
			cursor.execute(sql, (file, answer))
		connection.commit()

	except:
		print("ERR")


def main():
	configurationFile = open("configuration.txt", "r")
	subscription_key = configurationFile.readline().rstrip("\n\r")
	endpoint = configurationFile.readline().rstrip("\n\r")
	configurationFile.close()
	ocr_url = endpoint + "vision/v2.1/ocr"

	Model.assaginaAuthenticationCredentials(subscription_key, endpoint, ocr_url)



	# files = glob.glob("reports/*.pdf")
	# # print(files)
	# data = {}
	# for file in files:
	# 	print(file)
	# 	name, output = readReport(file)
	# 	data[file.replace("reports/", "")] = [name, output]
	#
	# 	# answer = input("\n")
	# 	#
	# 	# if answer == "":
	# 	# 	upload_pdf(file.replace("reports/", ""), name)
	# 	# elif answer == "a":
	# 	# 	print(output)
	# 	# 	answer = input("\n")
	# 	# 	upload_pdf(file.replace("reports/", ""), answer)
	# 	# else:
	# 	# 	upload_pdf(file.replace("reports/", ""), answer)
	#
	#
	#
	# 	print("\n-----------------------------------------------------\n")
	#
	# with open("data.pickle", 'wb') as handle:
	# 	pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)



	# print("output " + readReport("reports/271083-FB-Annual-Report-PROOF3.pdf"))





	# images = Model.pdfsIterator(["reports/EDUCO-Accountability-Report-2018.pdf"])
	#
	# text = ""
	# for img in images[0]:
	#     for item in getTextFromImage(img):
	#         text += item + " "
	# print(text.replace("\"","'"))

	with open("data.pickle", 'rb') as handle:
		p = pickle.load(handle)
	#
	# for item in p:
	#
	#
	# 	name = p[item][0]
	# 	words = p[item][1]
	#
	# 	answer = "-"
	# 	out = name
	# 	print(item)
	# 	print(name)
	# 	while answer != "":
	# 		if answer == "a":
	# 			print(words)
	# 		elif answer == "n":
	# 			break
	# 		elif answer != "-":
	# 			out = answer
	# 			break
	# 		answer = input("")
	#
	# 	if answer != "n":
	# 		upload_pdf(item, out)

	with connection.cursor() as cursor:
		# Read a single record
		sql = "SELECT `PDF_NAME` FROM `pdfs`"
		cursor.execute(sql)
		result = cursor.fetchall()
		# print(result)

	results  = []
	for r in result:
		results.append(r["PDF_NAME"])

	# for a in results:
	# 	if a not in p:
	# 		print(a)
	#
	# 		for item in p:
	# 			if a in item:
	# 				print("!!" + item)
	for item in p:
		if item not in results:
			name = p[item][0]
			words = p[item][1]

			answer = "-"
			out = name
			print(item)
			print(name)
			while answer != "":
				if answer == "a":
					print(words)
				elif answer == "n":
					break
				elif answer != "-":
					out = answer
					break
				answer = input("")

			if answer != "n":
				upload_pdf(item, out)





	connection.close()
main()

